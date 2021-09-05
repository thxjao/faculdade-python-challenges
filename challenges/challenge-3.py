import random
listaSorteio = ['Ruth', 'Ruth', 'Maria', 'Maria', 'Maria', 'Fernando', 'Fernando',
'Fernando', 'Fernando', 'Fernando']

adcionarPessoa = input('Quem gostaria de adcionar? ')
quantidade = int(input('Quanto foi doado? '))

i = quantidade
while i > 0:
    listaSorteio.append(adcionarPessoa)
    i -= 10

print('Lista de sorteio: {}'.format(listaSorteio))
verify = int(input('Gostaria de sortear agora?   0 - Não   1 - Sim   '))
if verify == 1:
    random.shuffle(listaSorteio)
    sorteado = random.choice(listaSorteio)
    print('O sorteado foi: {}'.format(sorteado))
else:
    print('Encerrando programa...')