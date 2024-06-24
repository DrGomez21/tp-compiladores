import re
from tabla_de_simbolos import tabla_de_simbolos

class Token:
    def __init__(self, comp_lexico, nro_linea, lexema):
        self.comp_lexico = comp_lexico
        self.nro_linea = nro_linea
        self.lexema = lexema    # Para revisar.

def get_comp_lex(lexema): 
    ''' buscar un lexema y retorna el componente lexico '''
    for expresion, valor in tabla_de_simbolos.items():
        if re.search(expresion, lexema):
            return valor
    return 'FAIL'   # En caso de error.

def abrir_archivo(nombre_archivo, modo):
    file = open(nombre_archivo, modo)
    return file

def leer_archivo(archivo):
    content = archivo.read().split('\n')
    return content

def error(nro_linea, lex):
    print("### Dr. JSON detectó ###")
    print(f'  * Ocurrió un error inesperado en la linea {nro_linea}')
    print(f'  * Se encontró: {lex}')
    print("-------------------------------------------")
    # exit(-1)

def lexer(ruta_archivo):

    archivo = abrir_archivo(ruta_archivo, 'r')
    
    content = leer_archivo(archivo)
    separadores = r'([,:])' # Expresión regular que matchea con los simbolos separadores del json.

    # Crear un array de todos los tokens.
    tokens_array = []
    nro_linea = 0
    
    archivo_salida = abrir_archivo("output.txt", "w")

    for texto in content:   # Se recorren las lineas del contenido del archivo.
        texto_sin_espacios = texto.replace(' ', '')
        listado_de_elementos = re.split(separadores, texto_sin_espacios)    # Obtenemos un listado de los componentes del json.
        nro_linea += 1  # Actualizamos el número de línea.
        
        for lexema in listado_de_elementos:
            if lexema.strip():
                comp_lexico = get_comp_lex(lexema.strip())
                if comp_lexico == 'FAIL': error(nro_linea, lexema)
                else:
                    t = Token(comp_lexico, nro_linea, lexema)
                    tokens_array.append(t)
                archivo_salida.write(t.comp_lexico + '\n')  # Agregamos el Token al archivo de salida

    tokens_array.append(Token("EOF", nro_linea, "EOF"))
    archivo_salida.write("EOF") # Fin del archivo.
    return tokens_array