def eliminarVacio(path):
    import os
    from pathlib import Path

    #Ruta a ordenar:
    os.chdir(path)

    dir = os.listdir(path)
    print(dir)

    for carpeta in dir:
        if os.path.isdir(carpeta):
            pathTemp = path + "\\" + carpeta
            if len(os.listdir(pathTemp)) == 0:
                eliminar = Path(pathTemp)
                eliminar.rmdir()