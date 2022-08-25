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
    've': 'B',
    'de': 'D',
    'te': 'T'
}

formario = ['cadete', 'vedete', 'hola', 'bedete']
frases = ['de jefe', 'te cabe']

lista = []
for key in digraphs_to_letters:
    lista.append(key)

#if ''.join(lista[0:3]) in formario:
#    for i in range(0,3):
#        print(digraphs_to_letters[lista[i]])
#
#if ''.join(lista[1:4]) in formario:
#    for i in range(1,4):
#        print(digraphs_to_letters[lista[i]])

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


for i in range(len(lista)+1):
    sigla = check_digraphs(i, (len(lista)-(len(lista)-3)), digraphs_to_letters, lista, formario)
    print(str(i), sigla)

''' Todas las formas de combinar ABCD - 24 porque es 4.3.2.1
ABCD

ABC
BCD
CDA
DAB

DCB
CBA
BAD
ADC

ACD
BDA
CAB
DBC

ADB
BAC
CBD
DCA

ABD
BCA
CDB
DAC

ACB
BDC
CAD
DBA
'''

