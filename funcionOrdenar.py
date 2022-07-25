def ordenar(path):
    import os
    import glob
    import shutil

    #Ruta a ordenar:
    os.chdir(path)

    #Extensiones de los archivos:
    tiposDeArchivos = {
    "--Documentos--":["*.pdf", "*.docx", "*.txt", "*.doc", "*.odt", "*.docm", "*.rtf", "*.csv", "*.xls", "*.xlsx", "*.xlsm", "*.ods", "*.pps", "*.ppt", "*.ppsx", "*.pptx", "*.ppsm", "*.pptm", "*.potx", "*.odp"],
    "--Videos--":["*.mp4", "*.mkv", "*.avi", "*.mov", "*divx", "*.flv", "*.mpg", "*.wmv", "*.wpl", "*.mpeg"],
    "--Fotos--":["*.png", "*.jpg", "*jpeg", "*.svg", "*.bmp", "*.ico", "*.webp", "*.gif", "*.heic", "*.nef", "*.crw", "*.id"],
    "--Audios--":["*.wav", "*.mp3", "*.acc", "*.wma", "*.flac", "*.midi", "*.ogg", "*.m3u"],
    "--Photoshop--":["*.psd"],
    "--Ilustrator--":["*.ai"],
    "--Comprimidos--":["*.rar", "*.zip", "*.rar5", "*.7z", "*.ace", "*.gz"],
    "--Imagenes CD o DVD--":["*.iso", "*.cue", "*.img", "*.rom"],
    "--Internet--":["*.html", "*.xml", "*.url", "*.css", "*.css", "*.js", "*.php", "*.swf"],
    "--Ejecutables--":["*.exe"],
    "--Archivos temporales--":["*.sfk"]
    }


    #Organizar los archivos:
    for tipoArchivo in tiposDeArchivos: #Recorre la clave de los diccionarios y si no existe una carpeta llamada asi la crea
        for formato in tiposDeArchivos[tipoArchivo]: #Recorre las extensiones
            formatoGlobal = glob.glob(formato) #Crea un array con los archivos que sean de la misma clave
            if(len(formatoGlobal) != 0 and not os.path.exists(tipoArchivo)):
                os.mkdir(tipoArchivo)
            for archivo in formatoGlobal:
                shutil.move(archivo, tipoArchivo) #Va moviendo todos esos archivos