letters_to_digraphs = {
    'b': ['be', 've'],
    'c': ['ce', 'ze'],
    'd': ['de'],
    'f': ['efe', 'fe'],
    'k': ['ca'],
    't': ['te']
    }

digraphs_to_letters = {
    'ca': 'K',
    'de': 'D',
    'te': 'T',
    've': 'B'
}

formario = ['cadete', 'vedete', 'hola', 'bedete']
frases = ['de jefe', 'te cabe']

lista_candidatas = ['ca', 'de', 'te', 've', 'de', 'te'] # debería extraerse de todas las combinaciones posibles de las claves del diccionario digraphs_to_letters (de 1, 2 y 3 claves)

def check_digraphs(start, end, digraphs, lista, formario):
    ''' Mira si hay alguna palabra en lista[start, end] que esté en formario
    y devuelve las letras correspondientes a las sílabas'''
    candidata = ''.join(lista[start:end])
    if candidata in formario:
        print("Se ha encontrado una palabra!", candidata)
        sigla = []
        for i in range(start,end):
            sigla.append(digraphs[lista[i]])
        return ''.join(sigla)

for i in range(len(lista_candidatas)+1):
    sigla = check_digraphs(i, (len(lista_candidatas)+i-3), digraphs_to_letters, lista_candidatas, formario)
    if sigla is not None:
        print(sigla)
