'''
> Ex 01:

Dada a lista nomes = ['ana', 'bruno', 'carla'], use uma
list comprehension para criar duas novas listas:

- Uma onde cada nome esteja em letras maiúsculas.
- Outra em CammelCase

== nomes = ['ana', 'bruno', 'carla']


> Ex 02:
Dada a lista numeros = , use uma list comprehension para 
criar uma nova lista contendo apenas os números que são maiores que 8.


== numeros = [5,12,67,6,4,9,8,21,7,3,45,2]
'''

#Exercicio 1
nomes = ['ana', 'bruno', 'carla']

nomes_maiusculos = [nome.upper() for nome in nomes]
nomes_camelcase = [nome.capitalize() for nome in nomes]

print(nomes_maiusculos)
print(nomes_camelcase)

# Exercicio 2
numeros = [5, 12, 67, 6, 4, 9, 8, 21, 7, 3, 45, 2]
numeros_maiores_que_8 = [n for n in numeros if n > 8]

print(numeros_maiores_que_8)
