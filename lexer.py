#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ply import lex

reserved = {
'int':'INT',
'float':'FLOAT',
'char':'CHAR',
'string':'STRING',
'double':'DOUBLE',
'long':'LONG',
'short':'SHORT',

'+':'SOMA', 
'-':'SUBTRACAO', 
'*':'MULTIPLICACAO',
'/':'DIVISAO',
'==':'IGUALDADE',
'=':'ATRIBUICAO',
'!':'NEGACAO',
'(':'(',
')':')',
'{':'{',
'}':'}',
';':'FIM DA LINHA',

'begin':'BEGIN',
'end':'END',
'if':'IF',
'else':'ELSE',
'while':'WHILE',
'do':'DO',
'for':'FOR',
'include':'INCLUDE',
'break':'BREAK',
'case':'CASE',
'swirch':'SWITCH',
'const':'CONST',
'default':'DEFAULT',
'return':'RETURN',
'static':'STATIC',
'void':'VOID',
}

tokens = [
    'FIM_COMANDO', #End of statement
    'ID',
    'NUM_INTEIRO',
    'NUM_REAL',
    'LETRA',
    'ABRE_PAR',
    'FECHA_PAR',
    'VIRGULA',
    'DIVIDIDO',
    'ELEVADO',
    'DIFERENTE',
    'MENOR_QUE',
    'MAIOR_QUE',
    'MENOR_IGUAL',
    'MAIOR_IGUAL',
    'IGUAL',
] + list(reserved.values())

t_ABRE_PAR = r'\('
t_FECHA_PAR = r'\)'
t_VIRGULA = r'\,'


def t_DIVIDIDO(t):
    r'dividido\s+por'
    t.value = str(t.value)
    return t

def t_ELEVADO(t):
    r'na'
    t.value = str(t.value)
    return t

def t_DIFERENTE(t):
    r'é\s+diferente\s+de'
    t.value = str(t.value)
    return t

def t_MAIOR_IGUAL(t):
    r'é\s+maior\s+ou\s+igual\s+a'
    t.value = str(t.value)
    return t

def t_MENOR_IGUAL(t):
    r'é\s+menor\s+ou\s+igual\s+a'
    t.value = str(t.value)
    return t

def t_IGUAL(t):
    r'é\s+igual\s+a'
    t.value = str(t.value)
    return t

def t_MAIOR_QUE(t):
    r'é\s+maior\s+que'
    t.value = str(t.value)
    return t

def t_MENOR_QUE(t):
    r'é\s+menor\s+que'
    t.value = str(t.value)
    return t

def t_NUM_REAL(t):
    r'\d+,\d+ | \,\d+'
    t.value = t.value.replace(',', '.')
    t.value = float(t.value)
    return t

def t_NUM_INTEIRO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_LETRA(t):
    r'\"[A-Za-z !#,$%&*+-~|:@¨¬\w]*"'
    return t

def t_ID(t):
    r'[a-zA-Z_\w*][a-zA-Z_0-9\w*]*'
    t.type = reserved.get(t.value,'ID')  #checando as palavras reservadas
    return t

def t_FIM_COMANDO(t):
    r'\.'
    return t

def t_newline(t): #regra para rastrear o numero de linhas
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print('Caractere ilegal na linha {}: {}'.format(lexer.lineno, t.value[0])) #algo fora do que permitido
    t.lexer.skip(1)

t_ignore = ' \r\t'

t_ignore_COMMENT='\#.*'

lexer = lex.lex()

if __name__ == '__main__':
    import sys

    dados = open(sys.argv[1]).read() #le o arquivo de entrada
    lexer.input(dados)
    token = lexer.token()
    while token:
        print(token)
        token = lexer.token()
