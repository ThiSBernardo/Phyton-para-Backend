
'''
|> EX02 <|
Crie uma função:

>>> classificar_imc(peso: float, altura: float) -> str. 

A função deve primeiro calcular o IMC (Índice de Massa Corporal) usando a fórmula:

>>> $peso / (altura * altura)$

Em seguida, deve retornar uma string classificando o resultado:

- Menor que 18.5: "Abaixo do peso"
- 18.5 a 24.9: "Peso normal"
- 25.0 a 29.9: "Sobrepeso"
- 30.0 ou mais: "Obesidade"
'''

def classificar_imc(peso: float, altura: float) -> str:
    num_imc = peso / (altura * altura)

    if num_imc < 18.5:
        return "Abaixo do peso"
    elif num_imc < 25.0:
        return "Peso normal"
    elif num_imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"
