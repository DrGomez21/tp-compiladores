import re

def get_comp_lex(lexema): 
    ''' buscar un lexema y retorna el componente lexico '''
    for expresion, valor in tabla_de_simbolos.items():
        if re.search(expresion, lexema):
            return valor

# diccionario con simbolos iniciales 
tabla_de_simbolos = {
   r'\[': "L_CORCHETE",
   r'\]': "R_CORCHETE",
   r'\{': "L_LLAVE",
   r'\}': "R_LLAVE",
   r',': "COMA",
   r':': "DOS_PUNTOS",
   r'".*"': "STRING",
   r'[0-9]+(\.[0-9]+)?((e|E)(\+|-)?[0-9]+)?': "NUMBER",
   r'true|TRUE': "PR_TRUE", # puede ser mayúscula o minúscula
   r'false|FALSE': "PR_FALSE", # puede ser mayúscula o minúscula
   r'null': "PR_NULL"
}