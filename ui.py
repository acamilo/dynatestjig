import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello World")
        self.set_default_size(240, 320)

        button_id_prog_right = Gtk.Button(label="Program ID Right",expand=True)
        button_id_prog_left = Gtk.Button(label="Program ID Left",expand=True)
        button_id_test_right = Gtk.Button(label="Test Motor Right",expand=True)
        button_id_test_left = Gtk.Button(label="Test Motor Left",expand=True)
        
        grid = Gtk.Grid()
        grid.add(button_id_prog_right)
        grid.attach_next_to(button_id_prog_left,button_id_prog_right,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(button_id_test_right,button_id_prog_left,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(button_id_test_left,button_id_test_right,Gtk.PositionType.BOTTOM,1,1)
        self.add(grid)
    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow()
win.fullscreen()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
