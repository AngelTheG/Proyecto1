import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class About(Gtk.Window):
    def __init__(self):
        super().__init__(title="About")
        self.set_size_request(100, 150)
        self.set_resizable(False)
        self.set_border_width(6)

        #Label que muestra información básica del proyecto
        lbl_info = Gtk.Label()
        lbl_info.set_justify(2)
        lbl_info.set_text("Morse for Coders\nversion 1\n\nCreado por:\nAngel Guerrero\nYostin Sepulveda")

        #Boton que abre el repositorio en el que se aloja el proyecto
        btn_openGit = Gtk.Button(label="GitHub")
        btn_openGit.connect("clicked", self.openGit)

        grid = Gtk.Grid()
        grid.set_row_spacing(20)
        grid.set_row_baseline_position(1,1)

        grid.attach(lbl_info, 0, 0, 5, 3)
        grid.attach_next_to(btn_openGit, lbl_info, Gtk.PositionType.BOTTOM, 5,3)

        self.add(grid)
    
    def openGit(self, widget):
        print("GITHUB Abierto")
        os.system("sensible-browser https://github.com/AngelTheG/Proyecto1")

