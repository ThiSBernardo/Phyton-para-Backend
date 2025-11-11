# HTTP
# REST == Representational State Transfer
#
# GET - Ler/Buscar algo em um servidor
#
# POST - Criar um novo recurso
#
# PUT - SubstituirAtualizar um recurso
#
# PATCH - Atualizar parcialmente um recurso
#
# DELETE - Remover um recurso

# STATUS CODES
#
# 200 - Sucesso
# 300 - Redirecionamento
# 400 - Erro
# 500 - Serer Error
#
# 404 - Não encontrado
# 403 - Proibido
# 200 - ok
# 201 - Criado com sucesso
# 401 - Não autorizado
# 500 - Internal Server Error
# 204 - Sem conteúdo
import requests

URL = 'https://preview.keenthemes.com/metronic/demo1/features/bootstrap/buttons.html'

# GET
print('Método: GET')
resposta_fiap = requests.get(URL)
print(f'Objeto: {resposta_fiap}')
print(f'Status Code: {resposta_fiap.status_code}')
conteudo = str(resposta_fiap.content).replace('\t', '  ').replace('\\n', '\n')
print(f'Conteúdo: {conteudo}')


# POST
print('Método: POST')
URL_POST = ''
payload = {'x':0}
post_fiap = requests.post(URL_POST, payload)
print(f'Objeto: {post_fiap}')
print(f'Status Code: {post_fiap.status_code}') 