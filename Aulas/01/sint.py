import os

# Númericos
inteiroo:int = 42
flutuante:float = 42.42

# Texto
texto_simples:str = 'Qualquer coidsa'
texto_bytes:bytes = b'Qualquer coisa'

# Nulo
nada:None = None

# Booleano
verdadeiro:bool = True
falso:bool = False

# Coleções
lista:list = ['Meu nome', 24, False, None, b'ByteString']
tupla:tuple = ('abc', 12)
lista_set:set = {'abc', 2, 3}
dicionario:dict = {'abc', 2,3}

lista[0] = 'Meu nombre'

variavel:any = None
variavel = lista

inteirinho =  3
print(type(inteirinho))
inteirinho = inteirinho /  2
print(type(inteirinho))

 

# Limpando o terminal
os.system('clear')

print(f'O valor da variável é: {variavel}')
print(f'O valor da variável {type(variavel)}')
