class Cliente:

    def __init__(self, nome:str, email:str):
        self.nome = nome
        self.email = email
        self.carrinho = []

    
    def __str__(self):
        return f'Cliente: \'{self.nome}\'({self.email})'

    def __repr__(self):
        return f'Cleinte(nome={self.nome}, email={self.email})'
    
    def __len__(self):
        return len(self.carrinho)
    
    def __getitem__(self, index):
        return self.carrinho[index]
    
    def buscar_produto_por_id_lista(id_busca:int):
        global produtos_lista
        for i, item in enumerate(produtos_lista):
            if i == id_busca:
                return item
            
    def transformar_lista_para_dict(produtos_lista:list) -> dict:
        return {i: item for i, item in enumerate(produtos_lista)}

    def buscar_produto_por_id_dict(produtos_dict:dict, id_busca:int) -> dict:
        return produtos_dict.get(id_busca)


    def criar_dicts():
        ids = ['0-5','5-10','10-20','20-100']
        dict_final = {}
        for id in ids:
            valor_min, valor_max = [int(x) for x in id.split('-')]
            dict_final[id] = [x for x in produtos_lista if x.values()[0] < valor_max and x.values()[0] >= valor_min]

        return dict_final
    
dicio = Cliente.criar_dict()
print(dicio)