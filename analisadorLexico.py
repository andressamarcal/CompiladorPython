import ply.lex as lex
import re
import codecs
import os
import sys

# lista de tokens
tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD','ASSIGN','NE',
'LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']

#dicionario de palavras reservadas
reservadas = {
    'begin':'BEGIN',
    'end':'END',
    'if':'IF',
    'then':'THEN',
    'while':'WHILE',
    'do':'DO',
    'call':'CALL',
    'const':'CONST',
    'int':'INT',
    'procedure':'PROCEDURE',
    'out':'OUT',
    'in':'IN',
    'else':'ELSE'
}

#concatenando ambos
tokens = tokens + list(reservadas.values())

# 'r' indicador de expressão regular
# '\' indicador de caractere
t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if  t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    #qualquer caractere exceto \n
    r'\#.*'
    pass


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


#Quando não atender as condições
def t_error(t):
    print("Caractere não permitido %s") % t.value[0]
    t.lexer.skip(1)


def buscarFicheiros(diretorio):
    ficheiros = []
    numArquivo = ''
    resposta = False
    cont = 1


    for base, dirs, files in os.walk(diretorio):
        ficheiros.append(files)

    for file in files:
        print (str(cont)+". "+file)
        cont += 1

    while resposta == False:
        numArquivo = input('Numero do teste: ')
        for file in files:
            if file == files[int(numArquivo)-1]:
                resposta = True
                break

    print ("Você escolheu: %s" % files[int(numArquivo)-1])

    return files[int(numArquivo)-1]


# PS: mudar diretorio de testes ao testar em outra maquina
diretorio = '/home/andressa/Documentos/Compiladores/Analisador Lexico/teste/'

arquivo = buscarFicheiros(diretorio)
test = diretorio+arquivo
#codecs permite ler    
fp = codecs.open(test,'r','utf-8')
string = fp.read()
fp.close()


analisador = lex.lex()

analisador.input(string)

while True:
    tok = analisador.token()
    if not tok : break
    print (tok)