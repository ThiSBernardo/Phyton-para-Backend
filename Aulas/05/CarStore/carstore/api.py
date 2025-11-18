from requests import get
URL = ''
def connect():
    response = get(f'{URL}/carros/marcas')
    return True if response.status_code == 200 else False

def retrieve(**argumentos):
    veiculo = argumentos.get('veiculo')
    marca = argumentos.get('marca')
    modelo = argumentos.get('modelo')
    ano = argumentos.get('ano')

    if not veiculo: return '{\'erro\':\'NOT_FOUND\'}'
    if not marca: connection = f'{URL}/carros/marca'
    elif not 
    
    response = get(connection)
    print(response.content)


print(retrieve(veiculo='carro'))