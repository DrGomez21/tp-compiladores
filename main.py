import re
import tabla_de_simbolos as simbolos

def main():

    archivo = open("entrada.txt", 'r')  
    
    content = archivo.read().split('\n')
    separadores = r'([,:])' # Expresión regular que matchea con los simbolos separadores del json.

    for texto in content:   # Se recorren las lineas del contenido del archivo.
        texto_sin_espacios = texto.replace(' ', '')
        listado_de_elementos = re.split(separadores, texto_sin_espacios)    # Obtenemos un listado de los componentes del json.

        for lexema in listado_de_elementos:
            if lexema.strip():
                print(simbolos.get_comp_lex(lexema.strip()))

if __name__ == "__main__":
    main()