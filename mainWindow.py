import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from about import About
from alfanumerico_morse import Alfanumerico_morse

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
        btn_switch = Gtk.Button(label="⇄")
        btn_switch.connect("clicked", self.switchFunction)

        #Entrada de texto
        
        self.ent_entrada = Gtk.Entry()
        self.ent_entrada.set_placeholder_text("Ingrese palabra/s a traducir")
        self.ent_entrada.set_alignment(0.5)
        self.ent_entrada.connect("changed", self.entryInput)
        self.ent_entrada.set_max_length(25)

        
        


        #Labels
        self.lbl_left = Gtk.Label()
        self.lbl_left.set_markup("<b><big>Alfanumerico</big></b>")


        self.lbl_right = Gtk.Label()
        self.lbl_right.set_markup("<b><big>Morse</big></b>")

        self.lbl_status = Gtk.Label()

        self.lbl_translate_info = Gtk.Label()

        self.lbl_result = Gtk.Label()
        self.lbl_result.set_markup("<b>El resultado se verá aquí</b>")
        self.lbl_result.set_selectable(True)

        #Boton ? para acceder a la información
        btn_about = Gtk.Button(label="?")
        btn_about.connect("clicked", self.about)

        #Config del Grid como contenedor principal
        grid = Gtk.Grid()
        grid.set_column_spacing(50)
        grid.set_row_spacing(30)

        grid.attach(btn_about, 0, 0, 1, 1)
        grid.attach_next_to(self.lbl_status, btn_about, Gtk.PositionType.RIGHT, 6, 1)
        
        grid.attach_next_to(self.lbl_left, self.lbl_status,Gtk.PositionType.BOTTOM, 6,1)
        grid.attach_next_to(btn_switch, self.lbl_left,Gtk.PositionType.RIGHT, 2 , 1)
        grid.attach_next_to(self.lbl_right, btn_switch, Gtk.PositionType.RIGHT, 3, 1)
        grid.attach_next_to(self.ent_entrada, self.lbl_left, Gtk.PositionType.BOTTOM, 6, 12)
        grid.attach_next_to(self.lbl_translate_info, btn_switch, Gtk.PositionType.BOTTOM, 2, 3)
        grid.attach_next_to(self.lbl_result, self.lbl_right, Gtk.PositionType.BOTTOM, 3, 12)
        grid.attach_next_to(btn_clear, self.lbl_translate_info, Gtk.PositionType.BOTTOM, 2, 3)

        self.add(grid)

    # Cambiar la modalidad de traducción
    def switchFunction(self, widget):
        print("Switch de traduccion")
        self.ent_entrada.set_text("")
        self.lbl_result.set_markup("<b>El resultado se verá aquí</b>")
        if self.lbl_left.get_text() == "Alfanumerico":
            self.lbl_left.set_markup("<b><big>                Morse</big></b>")
            self.lbl_right.set_markup("<b><big>                Alfanumerico</big></b>")
            self.ent_entrada.set_max_length(45)
        else:
            self.lbl_left.set_markup("<b><big>Alfanumerico</big></b>")
            self.lbl_right.set_markup("<b><big>Morse</big></b>")
            self.ent_entrada.set_max_length(25)

    # Limpiar todos los datos Entrada-Salida
    def clearAll(self, widget):
        self.ent_entrada.set_text("")
        self.lbl_result.set_markup("<b>El resultado se verá aquí</b>")

    #Desplegar ventana ABOUT
    def about(self, widget):
        print("Dialogo - ABOUT:type")
        win_about = About()
        win_about.connect("destroy", Gtk.Widget.destroy)
        win_about.show_all()
    
    # Detectar cambios en la entrada
    def entryInput(self, widget):
        self.lbl_status.set_text("")
        texto= self.ent_entrada.get_text()
        if self.lbl_left.get_text() == "Alfanumerico":
            codificado = self.codificar_morse(texto)
            self.lbl_result.set_text(codificado)
        else:
            for letter in self.ent_entrada.get_text():
                if letter.capitalize() in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890,:?'@=!":
                    self.lbl_status.set_text("Recuerda que estás traduciendo morse")
                

            #ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890,:?'@=!

            decodificado = self.decodificar_morse(texto)
            self.lbl_result.set_text(decodificado)
            print(decodificado)
    
    

    # Procesos de Decodificación
    def morse_a_caracter_plano(self,morse):
        for caracter in Alfanumerico_morse:
            if Alfanumerico_morse[caracter] == morse:
                return caracter
        return ""
    

    # Decodifica 
    def decodificar_morse(self,morse):
        texto_plano = ""  
        for caracter_morse in morse.split("/"):
            if caracter_morse== "":
                texto_plano += " "
            caracter_plano = self.morse_a_caracter_plano(caracter_morse)
            texto_plano += caracter_plano
        return texto_plano


    #
    def caracter_plano_a_morse(self,caracter):
        if caracter in Alfanumerico_morse:
            return Alfanumerico_morse[caracter]
        else:
            return ""


    def codificar_morse(self,texto_plano):
        texto_plano = texto_plano.upper()
        morse = "" 
        for caracter in texto_plano:
            caracter_codificado = self.caracter_plano_a_morse(caracter)
            morse += caracter_codificado + "/"
        return morse
