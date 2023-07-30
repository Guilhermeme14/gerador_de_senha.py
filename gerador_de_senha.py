import random
import os


def pergunta(texto):
    while True:
        resposta = input(texto).strip().lower()
        if resposta in ['s', 'n']:
            return resposta
        os.system('cls')
        print('Resposta inválida. Por favor, responda com "s" ou "n"')


i = 0

while True:
    quantas_senhas = int(input('Quantas senhas serão utilizadas? '))
    os.system('cls')
    tamanho_senha = int(input('Digite quantos carecteres terá sua senha: '))
    os.system('cls')
    caracteres_permitidos = ''
    todos_carac = pergunta(
        'Deseja por todos os caracteres?\n [s]sim ou [n]não\n')
    os.system('cls')

    if todos_carac == 'n':
        carac_esp = pergunta(
            'A senha possui caractere especial? \n [s]sim ou [n]não\n ')
        os.system('cls')
        if carac_esp == 's':
            caracteres_permitidos += '!@#$%^&*?'
        carac_letra = pergunta('A senha possui letra? \n [s]sim ou [n]não\n ')
        os.system('cls')
        if carac_letra == 's':
            caracteres_permitidos += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        carac_num = pergunta('A senha possui número? \n [s]sim ou [n]não\n ')
        os.system('cls')
        if carac_num == 's':
            caracteres_permitidos += '0123456789'
    elif todos_carac == 's':
        caracteres_permitidos += '!@#$%^&*()_+-=[]{}|;:,.<>?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while i < quantas_senhas:
        senha = ''.join(random.choice(caracteres_permitidos)for _ in range(tamanho_senha))
        i += 1
        print(f'Sua senha número {i}: {senha}')