#!/usr/bin/python3

import gi
import serial

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DynTestApp:
    def assign_motor_clicked(self,widget):
        print("Click")

    def __init__(self):
        

        self.gladefile = "ui.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("dyn-tester")
        self.stack = self.builder.get_object("dyn-stack")

        # main menu bottons
        self.button_assign = self.builder.get_object("assign-motor")
        self.button_assign.connect("clicked", self.assign_motor_clicked)

        self.button_test = self.builder.get_object("test-motor")
        self.button_test.connect("clicked", self.test_motor_clicked)

        # ID Assign selection buttons
        self.assign_left_button = self.builder.get_object("motor-assign-left-button")
        self.assign_left_button.connect("clicked", self.assign_left_button_clicked)

        self.assign_right_button = self.builder.get_object("motor-assign-right-button")
        self.assign_right_button.connect("clicked", self.assign_right_button_clicked)

        # Test Motor selection buttons
        self.test_left_button = self.builder.get_object("motor-test-left-button")
        self.test_left_button.connect("clicked", self.test_left_button_clicked)

        self.test_right_button = self.builder.get_object("motor-test-right-button")
        self.test_right_button.connect("clicked", self.test_right_button_clicked)

        # Return to menu buttons
        self.test_fail_menu = self.builder.get_object("error-motor-test")
        self.test_fail_menu.connect("clicked", self.return_to_main_menu)
        self.assign_ok_menu = self.builder.get_object("assign-ok-menu")
        self.assign_ok_menu.connect("clicked", self.return_to_main_menu)
        self.assign_fail_menu = self.builder.get_object("assign-fail-menu")
        self.assign_fail_menu.connect("clicked", self.return_to_main_menu)
        self.testing_motor_menu = self.builder.get_object("testing-motor-menu")
        self.testing_motor_menu.connect("clicked", self.stop_motor_test)

        self.window.set_default_size(240, 320)
        self.window.show()

        # Connect to the tester
        # send a return to get the menu
        try:
            self.ser = serial.Serial("/dev/ttyACM0")
            self.ser.timeout = 1.0
            self.ser.write(b'\r')
            self.ser.flush()
            response = self.ser.read(100)

            if b'right motor' in response:
                print("Programmer OK")
            else:
                print("Programmer returned bad data")               
                self.stack.set_visible_child_name("error-menu-serial")
        except (serial.SerialException,serial.SerialTimeoutException):
            print("Serial exception or timeout") 
            self.stack.set_visible_child_name("error-menu-serial")

        #self.window.fullscreen()

    def return_to_main_menu(self,widget):
        self.stack.set_visible_child_name("menu-assign-test")

    def assign_motor_clicked(self,widget):
        print("assign Click")
        self.stack.set_visible_child_name("motor-assign-menu")

    def test_motor_clicked(self,widget):
        print("test Click")
        self.stack.set_visible_child_name("motor-test-menu")

    def assign_left_button_clicked(self,widget):
        print("Assign Left")
        self.assign_motor(1)

    def assign_right_button_clicked(self,widget):
        print("Assign Right")
        self.assign_motor(2)
        

    def test_left_button_clicked(self,widget):
        print("Test Left")
        self.test_motor(1)

    def test_right_button_clicked(self,widget):
        print("Test Right")
        self.test_motor(2)


    def assign_motor(self,id):
        print("Assigning ID: %s to motor"%(str(id)))
        if True:
           self.stack.set_visible_child_name("assign-ok-menu") 
        else:
           self.stack.set_visible_child_name("assign-fail-menu")

    def test_motor(self,id):
        print("Testing Motor ID: %s"%(str(id)))
        if id==2:
            self.ser.write(b'4')
        elif id==1:
            self.ser.write(b'3')

        self.ser.flush()
        response = self.ser.read(100)
        if b'not found' in response:
            self.stack.set_visible_child_name("error-motor-test")
        else:
            self.stack.set_visible_child_name("testing-motor-menu")
    
    def stop_motor_test(self,widget):
        self.ser.write(b'\r')
        self.ser.flush()
        self.stack.set_visible_child_name("menu-assign-test")

    def on_destroy(self, widget):
        print("Destroyed!")
        gtk.main_quit()
    def on_clicked(self, widget):
        print(widget)

if __name__ == "__main__":
    main = DynTestApp()
    Gtk.main()
