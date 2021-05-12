import PySimpleGUI as sg

class telaPI:
    def __init__(self):
        #layote
        layot = [[sg.Text('X')],[sg.Text("Z")],[sg.Text("Y")]]

        #janela
        janela = sg.Window('XYZ').layout(layot)

        # Extrair dados
        self.button, self.values = janela.read()
        
    def iniciar(self):
        print(self.values)

xv = telaPI()
xv.iniciar()