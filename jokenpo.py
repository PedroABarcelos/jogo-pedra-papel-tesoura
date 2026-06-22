import random
largura = 50
titulo = 'Jokenpô'.center(largura)
sub_titulo = 'Será que você consegue ganhar do Computador?'.center(largura)
print('\033[31m' + '=' * largura + '\033[0m')
print(f'\033[1;31m{titulo}\033[0m')
print(f'\033[1;31m{sub_titulo}\033[0m')
print('\033[31m' + '=' * largura + '\033[0m')
print()
itens = ['✊', '✋', '✌️']
computador = random.choice(itens)
val = 0
op = int(input('\033[1;31mMENU:\n1-Pedra✊\n2-Papel✋\n3-Tesoura✌️\nFaça a sua Jogada: \033[0m'))
if op==1:
    usuario = '✊'
    val=1
elif op==2:
    usuario = '✋'
    val=1
elif op==3:
    usuario = '✌️'
    val=1
else:
    print('\033[1;31mEssa opção não existe, rode o programa novamente e selecione uma opção válida!\033[0m')

if val > 0:
    print() 
    print(f'\033[1;31mVocê jogou {usuario} e o Computador jogou {computador}\033[0m')
    if usuario == computador:
        print('\033[1;31mEMPATOU!🤝\033[0m')
    elif (usuario == '✊' and computador == '✌️') or \
        (usuario == '✋' and computador == '✊') or \
        (usuario == '✌️' and computador == '✋'):
        print('\033[1;31mVOCÊ GANHOU!🎉\033[0m')
    else:
        print('\033[1;31mCOMPUTADOR GANHOU!🤖\033[0m')
