# Modules
from metadata_analyser import extract_metadata

# Inicio del programa

if __name__ == "__main__":
    filepath = input("Dime la ruta del archivo a analizar: ")
    metadata = extract_metadata(filepath)
    
    for key, value in metadata.items():
        print(f"{key} : {value}")
