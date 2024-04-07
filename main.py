import re
import tabla_de_simbolos as simbolos

def main():
    archivo = open("entrada.txt", 'r')  
    contenido = archivo.readlines() # Leer las lineas del archivo.

    bool_espacio = '\n' or ' ' or '\t'
    for linea in contenido:
        for letra in linea:
            if letra not in bool_espacio:

                if letra == '"' and bool_es_string == False: #se esta iniciando un string 
                    func_es_string()    
                if letra == '"' and bool_es_string == True: # se esta terminando el string 
                    func_not_string()
                simbolos.get_comp_lex(letra)


    print(contenido)

if __name__ == "__main__":
    main()