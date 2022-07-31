import PySimpleGUI as sg
import funcionOrdenar
import funcionEliminar

#Establecer tema:
sg.theme("DarkBlack")

#Crear diseño:
layout = [
    [sg.Radio('Ordenar en carpetas', "RADIO1", default=True, key="ordenar"), sg.Radio('Eliminar carpetas vacias', "RADIO1", default=False, key="eliminar")],
    [sg.Text("Ingresa la ruta:")],
    [sg.InputText(do_not_clear=False), sg.FolderBrowse("Buscar...")],
    [sg.Button("Aceptar"), sg.Button("Cancelar")]
]

#Creamos la ventana:
window = sg.Window("Super Explorer", layout, icon="F:\Proyectos de git\Super-Explorer\icono.ico")

#Event loop:
while True:
    event, values = window.read()
    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break
    if event == "Aceptar" and values["ordenar"]:
        try:
            funcionOrdenar.ordenar(values[0])
            sg.popup("Se ordenaron los archivos correctamente.")
        except:
            sg.popup_error("ERROR","NO HAS INTRODUCIDO UNA RUTA VALIDA O LA RUTA ES INCORRECTA.", background_color="red", text_color="white")
    elif event == "Aceptar" and values["eliminar"]:
        try:
            funcionEliminar.eliminarVacio(values[0])
            sg.popup("Las carpetas vacias se eliminaron correctamente.")
        except:
            sg.popup_error("ERROR","LA RUTA NO ES VALIDA O ES INCORRECTA.", background_color="red", text_color="white")

#Cerramos la ventana:
window.close()