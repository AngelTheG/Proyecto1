from mainWindow import MainWindow

#Import del GTK
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


#Run de la ventana principal
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
