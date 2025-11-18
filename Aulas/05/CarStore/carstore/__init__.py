class Main:

    def __init__(self):
        from .utils import  retorna_argumentos
        self.argumentos = retorna_argumentos()

    def call_info(self):
        from .api import connect, retrieve
        if not connect(): exit()
        
        try: self.veiculo = self.argumentos.vehicle
        except AttributeError: v_ano
        except AttributeError: v_veiculo = None
        
        try: self.modelo = self.argumentos.model
        except AttributeError: v_modelo = None

        try: self.marca = self.argumentos.brand
        except AttributeError: v_marca = None

        try: self.ano = self.argumentos.year
        except AttributeError: v_ano = None
        self.call_info()

    def call_info(self):
        from .api import connect, retrieve
        if not connect(): exit()
        info = retrieve(veiculo=self.veiculo, marca = self.marca, modelo = self.modelo, ano = self.ano)
        print(info.content)


class Carro:

    def __init__(self):
        pass

class Marca:
    ...