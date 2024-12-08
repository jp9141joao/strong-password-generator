import random
import time
import os

def Iniciar():
    Tam = random.randint(10,30)
    Layout = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ)TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
    Senha = ''

    for i in range(Tam):
        Caracter = random.choice(Layout)
        Senha += f'{Caracter}'

    return Senha


while True:
    os.system('cls')

    Menu = int(input(f'\n* Menu *\n1- Gerar senha\n2- Sair\nR: '))
    while Menu != 1 and Menu != 2:
        Menu = int(input('\n* Menu *\nOpção invalida!\n1- Gerar senha\n2- Sair\nR: '))

    if Menu == 1:
        print(f'Sua senha é\n\n{Iniciar()}')
        Continuar = int(input('\nDigite "1" para voltar\nR: '))
        while Continuar != 1:
            Continuar = int(input('\nDigite "1" para voltar\nR: '))
    else:
        print('\nPrograma finaliado!')
        break