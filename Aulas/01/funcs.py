# import meu_modulo

# global CONTADOR

# # def increment(num:int) -> None:
# #     CONTADOR = 0
# #     cont = CONTADOR
# #     for i in range(num+1):
# #         cont += 1
# #     print(cont)

# # if __name__ == '__main__':
# #     increment(1000000)

# def argumentos(inteiro:int, texto:str):
#     ''' Essa função retorna um dicionario (inteiro, texto) com os valores Passados
#     return {'inteiro': inteiro, 'texto': texto} '''

# if __name__ == '__main__':
#     # args = argumentos()
#     # print(type(args))
#     # print(args)


#     # print(__name__)
#     # meu_modulo.chamar_name()

#     tipo_inteiro = meu_modulo.validar_tipo(42)
#     print(tipo_inteiro)
#     print(type(tipo_inteiro))

from meu_modulo import Tarefas

if __name__ == '__main__':
    try: Tarefas()
    except KeyboardInterrupt: print('Finalizado pelo Usuario! (ctr +  c)')