def get_comp_lex(lexema): 
    ''' buscar un lexema y retorna el componente lexico '''
    try: 
        return tabla_de_simbolos[lexema]
    except: 
        return -1


# diccionario con simbolos iniciales 
tabla_de_simbolos = {
    "[": "L_CORCHETE",
    "]": "R_CORCHETE",
    "{": "L_LLAVE",
    "}": "R_LLAVE",
    ",": "COMA",
    ":": "DOS_PUNTOS",
    '"': "LITERAL_CADENA",
    "number": "LITERAL_NUM",
    "true": "PR_TRUE", # puede ser mayuscula o minuscula
    "false": "PR_FALSE", # puede ser mayuscula o minuscula
    "null": "PR_NULL",
    "eof": "EOF"
}
 