#!/usr/bin/python3

import gi

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
        self.window.set_default_size(240, 320)
        self.window.show()
        self.window.fullscreen()


    def assign_motor_clicked(self,widget):
        print("assign Click")
        self.stack.set_visible_child_name("motor-assign-right-left-menu")

    def test_motor_clicked(self,widget):
        print("test Click")

    def assign_left_button_clicked(self,widget):
        print("Assign Left")

    def assign_right_button_clicked(self,widget):
        print("Assign Right")


    def on_destroy(self, widget):
        print("Destroyed!")
        gtk.main_quit()
    def on_clicked(self, widget):
        print(widget)

if __name__ == "__main__":
    main = DynTestApp()
    Gtk.main()
