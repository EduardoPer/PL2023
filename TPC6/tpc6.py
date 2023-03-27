import ply.lex as lex
import re

tokens = (
    'NUMBER', #r'-?[\d]+'
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'TYPE', 
    'LOOP', #r'for|while'
    'GREATER',
    'LESSER',
    'EQUALS',
    'END_LINE', #r'\;'
    'LBRACKET',
    'RBRACKET',
    'LSBRACKET',
    'RSBRACKET',
    'PROGRAM',
    'COMMENT',
    'MCOMMENT',#r'\/\*(.*)*[\n]*\*\/'
    'FUNCTION',
    'COMMA',
    'IF',
    'VARIABLE',
    'LIST',
    'FNAME'
)

t_NUMBER = r'-?[\d]+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_TYPE = r'int|float|double|bool|char|string|long'
t_LOOP = r'for|while'
t_GREATER = r'\>'
t_LESSER = r'\<'
t_EQUALS = r'\='
t_END_LINE = r'\;'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'
t_PROGRAM = r'program'
t_COMMENT = r'\/\/.*'
t_MCOMMENT = r'/\*[\s\S]*?\*/'#r'\/\*((\-\-)?(.*)[\n]?)*\*\/'
t_FUNCTION = r'function'
t_COMMA = r'\,'
t_IF = r'if'
t_VARIABLE = r'[a-z]+[\[|\)|(\=)|(in)|\,]'
t_LIST = r'\[((.*),*)*\] | \[(-?[\d]+)..(-?[\d]+)\]'
t_FNAME = r'[\w]+{'

t_ignore  = ' \t'

def t_error(t):
    if re.match(r'[ \t\n]', t.value[0]) == None:
        print(f"Unspecified token {t.value[0]}")
    t.lexer.skip(1)

def main():  
    example1 = '''
    /* max.p: calcula o maior inteiro duma lista desordenada
    -- 2023-03-20 
    -- by jcr
    */
    int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
    // Programa principal
    program myMax{
    int max = a[0];
    for i in [1..9]{
        if max < a[i] {
        max = a[i];
        }
    }
    print(max);
    }
    '''

    lexer = lex.lex()
    lexer.input(example1)

    print("\n\n\n")
    print("EXAMPLE 1")
    print("\n\n")


    while tok := lexer.token():
        print(tok)

if __name__ == '__main__':
    main()