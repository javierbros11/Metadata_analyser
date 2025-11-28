
# Metadata analyser

Se trata de un programa que permite el análisis de los metadatos almacenados en los archivos, ya sea una imagen o un documento de texto (pdf o docx) o incluso de emails.

Esta conformado con dos scripts principales, el archivo **main.py**, donde se encuentra la función principal encargada de ejecutar el programa, y el archivo **metadata_analyser.py**, que contiene el script donde reside el programa en sí.
## Instalación

Para poder ejecutar correctamente el script se requiere instalar algunos paquetes externos de Python, todas las referencias se ubican en el archivo **requirements.txt**.

Instalar Python en caso de que no lo tenga:

[Download Python](https://www.python.org/downloads/)

Instalación de paquetes externos:

```bash
  pip install pillow pdfminer.six python-docx
```



## Funcionalidades

- **Análisis de metadatos**: Como se ha mencionado anteriormente, la funcionalidad principal de este programa es el análisis de metadatos. Tras realizar el análisis, los resultados obtenidos se muestran de forma clara y breve por pantalla.

- **Diferenciación entre archivos**: El programa es capaz de distinguir el formato asociado a un archivo sin necesidad de indicarlo expresamente, únicamente requerimos de indicarle el archivo que deseemos análizar en ese momento. Esto entre otras cosas permite que en función de su formato, devolverá unos metadatos u otros.




## Ejemplo de uso

A continuación se muestra un ejemplo de como se ve el programa al ejecutarlo. Todos los metadatos extraidos se ha obtenido a partir de esta imagen **DSCN0010.png** ubicada en este repositorio de github https://github.com/ianare/exif-samples/blob/master/jpg/gps/DSCN0010.jpg (este repositorio se ha creado expresamente para el análisis de metadatos con los archivos que proporciona)

```bash
└─$ python main.py
                       
Dime la ruta del archivo a analizar: DSCN0010.jpg
GPSInfo : 926
ResolutionUnit : 2
ExifOffset : 268
ImageDescription :                                
Make : NIKON
Model : COOLPIX P6000
Software : Nikon Transfer 1.1 W
Orientation : 1
DateTime : 2008:11:01 21:15:07
YCbCrPositioning : 1
XResolution : 300.0
YResolution : 300.0
```


## Posibles excepciones durante la ejecución del programa

Es posible que al intentar llevar a cabo el análisis de metadatos nos salte algunas de estas excepciones:

- **No EXIF metadata found**: El programa ha identificado que el archivo se trata de una imagen JPG o JPEG, pero no ha sido capaz de extraer los metadatos.

- **No PNG metadata found**: Se ha identificado el archivo como una imagen en formato PNG pero el programa no ha conseguido los metadatos asociados a ese archivo.

- **Unsopported image format**: El programa no ha sido capaz de averiguar el formato del archivo proporcionado.

- **Error retrieving metadata from the document**: El programa ha interpretado el archivo como un documento de texto pero no ha sido capaz de extraer los metadatos asociados.

- **Unsopported file type**: El programa no ha conseguido identificar el formato del archivo proporcionado.
## Desarrollo

El script presentado se encuentra desarrollado en **Python**.


## Disclaimer

El script fue creado únicamente por motivos educativos, principalmente para aprender a realizar scripts o programas desarrollados en Python que involucren conceptos o casos prácticos a la Ciberseguridad o al Hacking Ético.

Se ruega utilizar los programas añadidos a este repositorios para dicho fin sobre equipos aislados o virtuales para simular el entorno, en caso contrario, no nos hacemos responsables de su uso fuera de ese ámbito.

