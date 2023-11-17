import re

def to_lowercase(query):
    return query.lower()

def replace_non_keywords(query):
    keywords = ['input', 'substr', 'format', 'proc', 'distinct', 'max', 'sql', 'quit', 'run', 'end', 'then', 'else', 'between', 'yymmdd8','datepart','put','case', 'when', 'in','as', 'create', 'table', 'select', 'from', 'where', 'and', 'or', 'join', 'inner', 'left', 'right', 'outer', 'on', 'group', 'by', 'order', 'having']

    replacement_prefix = 'x'
    replacement_counter = 1
    replacements = {}

    lines = query.split('\n')
    legend = {}

    for i in range(len(lines)):
        line = lines[i]
        tokens = re.split(r'(\b\w+\b|[.,;()=<>]| |\n|\t)', line)

        for j in range(len(tokens)):
            current_token = tokens[j]
            if current_token.strip().lower() not in keywords and current_token.isalnum():
                if current_token not in replacements:
                    replacements[current_token] = f'{replacement_prefix}{replacement_counter}'
                    legend[current_token] = replacements[current_token]
                    replacement_counter += 1
                tokens[j] = replacements[current_token]

        lines[i] = ''.join(tokens)

    return '\n'.join(lines), legend

sql_query = """
YOUR SQL QUERY
;quit;
"""

# Convertir la consulta a minúsculas
sql_query_minusculas = to_lowercase(sql_query)

# Eliminar guiones bajos antes de llamar a la función para reemplazar los nombres
sql_query_sin_guiones = sql_query_minusculas.replace('_', '')

# Llama a la función para reemplazar los nombres
sql_query_modificado, legend = replace_non_keywords(sql_query_sin_guiones)

# Imprime la consulta SQL modificada respetando las tabulaciones
print("QUERY MODIFICADA:\n", sql_query_modificado)
print("\nLEYENDA DE VARIABLES:")
for original, replacement in legend.items():
    print(f"{original} -> {replacement}")