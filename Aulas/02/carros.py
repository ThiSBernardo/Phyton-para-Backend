class Carro:

    def __init__(self, 
                marca:str,
                modelo:str,
                ano:int,
                preco:float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def __repr__(self):
        return f'Carro(marca=\'{self.marca}\', modelo=\'{self.modelo}\', ano={self.ano}, preco={self.preco})'
    
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano}) → R${self.preco}'
    
    def __gt__(self, other):
        if not isinstance(other, Carro):
            return None
        preco_1 = self.preco
        preco_2 = other.preco
        if preco_1 > preco_2: return True
        return False
    
    def __lt__(self, other):
        if not isinstance(other, Carro):
            return None
        preco_1 = self.preco
        preco_2 = other.preco
        if preco_1 < preco_2: return True
        return False

if __name__ == '__main__': 
    # list_carros = []

    ka = Carro('Ford', 'Ka', 2020, 35000.00)
    ka_2 = Carro('Ford', 'Ka', 2016, 8000.00)

    f1_gtr = Carro('Mclaren', 'F1-GTR', 1995, 1200000.0)
    charger = Carro('Dodge', 'Charger', 1970, 23000.0) 

class Concessionaria:

    def __init__(self, nome:str, positions:int, arquivo_carros:str = None, dicio_carros:dict = {}):
        self.nome:str = nome
        self.arquivo:str = arquivo_carros
        self.dicio_carros:dict[Carro] = dicio_carros

        self.empty_positions:list[int] = list(range(1, positions+1))
        self.complete_positions:list[int] = []

        if self.arquivo:
            self.add_cars()
        else:
            print('Sem Arquivo!')

    def __repr__(self):
        return f'Concessionaria(nome=\'{self.nome}\', positions={self.positions}, arquivo_carros=\'{self.arquivo}\', dicio_carros={self.dicio_carros})'

    def __str__(self):
        return f'{self.nome} ({self.positions} Posições)'

    def __add__(self, other):
        if not isinstance(other, Carro):
            raise Exception('Você tentou adionar algo que não é um carro!')
        
        if other in self.dicio_carros.values():
            return None
        try:
            self.dicio_carros[self.empty_positions[0]] = other
            self.complete_positions.append(self.empty_positions[0])
            self.empty_positions.pop(0)
            print(f'{other.modelo} {other.ano} adicionado!')
        except (KeyError, IndexError):
            print(f'A concessionária \'{self.nome}\' está cheia!\n\tNão foi possível adicionar o {other.modelo}')
            return None 
        
    def __sub__(self, other):
        if not isinstance(other, Carro):
            raise Exception('Você tentou remover algo que não é um carro!')
        
        deletar = None
        for vaga, carro in self.dicio_carros.items():
            if other == carro:
                deletar = vaga
        
        if deletar:
            self.complete_positions.remove(deletar)
            self.empty_positions.append(deletar)
            del self.dicio_carros[deletar]
            print(f'{other.modelo} removido!')

    def add_cars(self):
        ''' 
        Aqui dentro eu coloco meu comentário

        Comentário - Extra
        ------------------
        Aqui vem um comentário mais longo, tipo lorem ipsum dolor sit

        O que Fazer?
        ----------------
        Fazer isso, isso e aquele outro

        Exemplo de código
        ------------------

        '''
        from json import loads as json_loads
        with open(self.arquivo) as f:
            dicio_carros:dict = json_loads(f.read())
        for carro in dicio_carros.values():
            marca, modelo, ano, preco = carro
            car = Carro(marca, modelo, ano, preco)
            self + car

if __name__ == '__main__':
    # super_car = Concessionaria(nome='Super Car', arquivo_carros='carros.json', positions=30)

    test_car = Concessionaria(nome='Teste Car', positions=2, arquivo_carros='carros.json')  