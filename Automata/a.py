import re

# ---------------------------
# Definición de patrones de tokens
# ---------------------------
token_specs = [
    ('NUMBER',      r'\b\d+(\.\d+)?\b'),                   # Números enteros y decimales
    ('KEYWORD',     r'\b(fun|num|input|print|for|to)\b'),  # Palabras clave reservadas
    ('EQ',          r'=='),                                # Igualdad
    ('NEQ',         r'!='),                                # Diferente
    ('GTE',         r'>='),                                # Mayor o igual
    ('LTE',         r'<='),                                # Menor o igual
    ('GT',          r'>'),                                 # Mayor
    ('LT',          r'<'),                                 # Menor
    ('ASSIGN',      r'='),                                 # Asignación (después de ==)
    ('MULT',        r'\*'),                                # Multiplicación
    ('MINUS',       r'-'),                                 # Resta
    ('LPAREN',      r'\('),                                # Paréntesis izquierdo
    ('RPAREN',      r'\)'),                                # Paréntesis derecho
    ('COLON',       r':'),                                 # Dos puntos
    ('SEMICOLON',   r';'),                                 # Punto y coma
    ('NEWLINE',     r'\n'),                                # Fin de línea
    ('IDENTIFIER',  r'\b[a-zA-Z_]\w*\b'),                  # Identificadores (nombres de variables, etc.)
    ('SKIP',        r'[ \t]+'),                            # Espacios y tabs
    ('UNKNOWN',     r'.'),                                 # Cualquier otro carácter
]

# Compilación del patrón maestro
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
get_token = re.compile(tok_regex).match

# ---------------------------
# Función principal del analizador léxico
# ---------------------------
def tokenize(code):
    """
    Toma un string con el código fuente y devuelve una lista de tokens.
    Imprime errores si encuentra caracteres desconocidos.
    """
    pos = 0
    tokens = []
    line_num = 1
    while pos < len(code):
        match = get_token(code, pos)
        if not match:
            print(f"[Línea {line_num}] No se pudo identificar carácter en posición {pos}")
            pos += 1
            continue

        kind = match.lastgroup
        value = match.group()

        if kind == 'NEWLINE':
            line_num += 1
        elif kind == 'SKIP':
            pass  # ignoramos espacios
        elif kind == 'UNKNOWN':
            print(f"[Línea {line_num}] No se pudo identificar: {value!r}")
        else:
            tokens.append((kind, value))
        pos = match.end()
    return tokens

# ---------------------------
# Ejecución principal del archivo
# ---------------------------
if __name__ == "__main__":
    with open("programaerr.txt", "r", encoding="utf-8") as f:
        code = f.read()

    tokens = tokenize(code)
    for token in tokens:
        print(token)
