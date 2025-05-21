# En este ejercicio se emplea un patrón de diseño que permite crear clases que pueden extenderse de forma modular denominada factory,


# External Packages
from PIL import Image
import mimetypes
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import docx

# Local Packages
import re
from abc import ABC,abstractmethod

# Creamos una clase abstracta para obligar a las clases hijas emplear los métodos abstractos (teniendo una interfaz similar).

class MetadataExtractor(ABC):
    """
    Clase padre donde almacena el método constructor principal.
    """
    @abstractmethod
    def extract(self, filepath):
        pass

class ImageMetadataExtractor(MetadataExtractor):
    """
    Clase encargada de la extracción de los metadatos de una imagen.
    """

    def extract(self, filepath):
        with Image.open(filepath) as img:
            if img.format in ["JPG", "JPEG"]:
                exif = img.getexif()
                if exif:
                    return {Image.ExifTags.TAGS.get(key, key): value
                            for key,value in exif.items() if key in Image.ExifTags.TAGS}
                
                else:
                    return{"Error" : "No EXIF metadata found."}
            
            elif img.format in ["PNG"]:
                if img.info:
                    return img.info
                else:
                    return{"Error" : "No PNG metadata found."}
                
            else:
                return{"Error" : "Unsopported image format."}
            
class PdfMetadataExtractor(MetadataExtractor):
    """
    Clase encargada de la extracción de los metadatos de un documento PDF.
    """

    def extract(self, filepath):
        metadata = {}
        with open(filepath, "rb") as f:
            parser = PDFParser(f)
            doc = PDFDocument(parser)

            if doc.info:
                for info in doc.info:
                    for key,value in info.items():
                        # A veces los metadatos vienen representados en bytes
                        # Verificamos si el valor de la clave son bytes
                        if isinstance(value,bytes):
                            try:
                                # Intentar decodificarlo en UTF-16BE
                                decoded_value = value.decode("utf-16be")
                            except UnicodeDecodeError:
                                # Intentar decodificarlo en UTF-8
                                decoded_value = value.decode("utf-8",errors="ignore")
                        else:
                            decoded_value = value
                        metadata[key] = decoded_value
            else:
                print("Error al sacar los metadatos")
            # Procesamos el texto del pdf para obtener otros datos de interes
            text = extract_text(filepath)
            metadata["Emails"] = self._extract_emails(text)
            return metadata


    def _extract_emails(self, text):
        """
        Permite la extracción de métadatos en emails empleando expresiones regulares.

        Args:
            text(str): Consta del correo a analizar.
        """

        email_regex = r"[a-zA-Z0-9._%+-] + @[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        return re.findall(email_regex, text)
    

class DocxMetadataExtractor(MetadataExtractor):
    """
    Clase encargada de la extracción de metadatos en documentos Word.
    """

    def extract(self, filepath):
        doc = docx.Document(filepath)
        prop = doc.core_properties
        attributes = [
                "author", "category", "comments", "content_status",
                "created", "identifier", "keywords", "last_modified_by",
                "language", "modified", "subject", "title", "version"
        ]

        metadata = {attr: getattr(prop, attr, None) for attr in attributes}
        return metadata
    
class MetadataExtractorFactory:
    """
    Clase encargada de comprobar el tipo de archivo antes de extraer sus metadatos.
    """
    @staticmethod
    def get_extractor(filepath):
        """
        Invoca los principales métodos de extracción de metadatos en función del tipo de fichero.

        Args:
            filepath(str): Ruta de acceso local al fichero que se quiere analizar.
        """

        mime_type, _ = mimetypes.guess_type(filepath) # Si sacamos una variable que no vamos a emplear en nuestro código se suele nombrar como "_"
        if mime_type:
            if mime_type.startswith("image"):
                return ImageMetadataExtractor()
            if mime_type == "application/pdf": # <- En el caso de que sea un PDF
                return PdfMetadataExtractor()
            if mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                return DocxMetadataExtractor()
        raise ValueError("Unsopported file type")
            

def extract_metadata(filepath):
    """
    Función inicial para extraer los metadatos.

    Args:
            filepath(str): Ruta de acceso local al fichero que se quiere analizar.
    """
    extractor = MetadataExtractorFactory.get_extractor(filepath)
    return extractor.extract(filepath)