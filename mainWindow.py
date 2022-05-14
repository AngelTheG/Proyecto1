import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from about import About

class MainWindow(Gtk.Window):
    def __init__(self):
        #Edición de la ventana principal
        super().__init__(title="Morse for Coders")
        self.set_size_request(850, 600)
        self.set_resizable(False)

        super().__init__(title="Grid Example")

        #Boton limpiar
        btn_clear = Gtk.Button(label="LIMPIAR")
        btn_clear.connect("clicked", self.clearAll)

        #Boton Cambio Alfanumerico-Morse a Morse-Alfanumerico
        btn_switch = Gtk.Button(label="<---\--->")
        btn_switch.connect("clicked", self.switchFunction)

        #Entrada de texto
        self.ent_entrada = Gtk.Entry()
        self.ent_entrada.set_text("Ingrese palabra/s a traducir")
        self.ent_entrada.set_alignment(0.5)
        self.ent_entrada.connect("changed", self.entryInput)

        #Labels
        self.lbl_left = Gtk.Label()
        self.lbl_left.set_text("Alfanumerico")

        self.lbl_right = Gtk.Label()
        self.lbl_right.set_text("Morse")

        self.lbl_status = Gtk.Label()

        self.lbl_entry_DEBUG = Gtk.Label()

        self.lbl_translate_info = Gtk.Label()

        self.lbl_result = Gtk.Label()
        self.lbl_result.set_text("El resultado se verá aquí")
        self.lbl_result.set_selectable(True)

        #Boton ? para acceder a la información
        btn_about = Gtk.Button(label="?")
        btn_about.connect("clicked", self.about)

        #Boton para acceder al diccionario completo de traduccion
        btn_diccionary = Gtk.Button(label="⌨")
        btn_diccionary.connect("clicked", self.diccionary)


        #Config del Grid como contenedor principal
        grid = Gtk.Grid()
        grid.set_column_spacing(50)
        grid.set_row_spacing(30)

        grid.attach(btn_about, 0, 0, 1, 1)
        grid.attach_next_to(self.lbl_status, btn_about, Gtk.PositionType.RIGHT, 6, 1)
        grid.attach_next_to(btn_diccionary, btn_about, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(self.lbl_left, self.lbl_status,Gtk.PositionType.BOTTOM, 6,1)
        grid.attach_next_to(btn_switch, self.lbl_left,Gtk.PositionType.RIGHT, 2 , 1)
        grid.attach_next_to(self.lbl_right, btn_switch, Gtk.PositionType.RIGHT, 3, 1)
        grid.attach_next_to(self.ent_entrada, self.lbl_left, Gtk.PositionType.BOTTOM, 6, 12)
        grid.attach_next_to(self.lbl_translate_info, btn_switch, Gtk.PositionType.BOTTOM, 2, 3)
        grid.attach_next_to(self.lbl_result, self.lbl_right, Gtk.PositionType.BOTTOM, 3, 12)
        grid.attach_next_to(btn_clear, self.lbl_translate_info, Gtk.PositionType.BOTTOM, 2, 3)

        self.add(grid)

    def switchFunction(self, widget):
        print("Switch de traduccion")
        if self.lbl_left.get_text() == "Alfanumerico":
            self.lbl_left.set_text("Morse")
            self.lbl_right.set_text("Alfanumerico")
        else:
            self.lbl_left.set_text("Alfanumerico")
            self.lbl_right.set_text("Morse")

    def clearAll(self, widget):
        self.ent_entrada.set_text("")
        self.lbl_result.set_text("El resultado se verá aquí")

    def about(self, widget):
        print("Dialogo - ABOUT:type")
        win_about = About()
        win_about.connect("destroy", Gtk.Widget.destroy)
        win_about.show_all()

    def diccionary(self, widget):
        print("Dialogo - DICCIONARY:type")

    def entryInput(self, widget):
        print("Cambio detectado")

        