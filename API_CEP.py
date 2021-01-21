import requests
import time
import json
import os

def menuprincipal():
    print(" [ 1 ] CONSULTAR CEP.")
    print(" [ 2 ] SAIR.")


def consultarcep():
    try:
        CITY = str(input('CEP: '))
        print('')
        req = requests.get('https://viacep.com.br/ws/' + CITY + '/json/')

        cep = json.loads(req.text)
        print(cep)
        print('CEP:', cep['cep'])
        print('logradouro: ', cep['logradouro'])
        print('complemento: ', cep['bairro'])
        print('cidade: ', cep['localidade'])
        print('uf: ', cep['uf'])
        print('')
    except Exception as Error:
        print("Tente novamente...")
        print('')


print('Iniciando...')
print('')
time.sleep(2)

op = 0
while op != 2:
    menuprincipal()
    op = int(input("Deseja escolher qual opção? "))
    if op == 1:
        consultarcep()
    elif op == 2:
        print('Encerrando...')
        time.sleep(2)
    else:
        print('Opção Inválida...')


os.system("pause")
