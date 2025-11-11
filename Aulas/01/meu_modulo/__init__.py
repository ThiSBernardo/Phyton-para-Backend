# print('importado!')

# # def chamar_name() -> None:
#     # print(__name__)

#     # if __name__ == 'meu_modulo':
#     #     print('Esse cara foi importado')
#     # else:
#     #     print('Esse cara está sendo executado como __main__')

# def validar_tipo(variavel:any) -> type:
#     return type(variavel)

class Tarefas:

    def __init__(self):
        try:
            inteiro:int = int(input('digite um numero:\n> '))
            raise ErroPersonalizado('Esse erro é um erro personalizado')
        except ErroPersonalizado as e:
            print('Ocorreu um erro personalizado:', e)
        except ValueError: 
            print('O programa requer um numero inteiro!')
        finally:
            print('ok')

class ErroPersonalizado(Exception):

    def __init__(self, *args):
        super().__init__(*args)