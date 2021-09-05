import random #Importamos a função random.
listaSorteio = ['Ruth', 'Ruth', 'Maria', 'Maria', 'Maria', 'Fernando', 'Fernando',
'Fernando', 'Fernando', 'Fernando'] # Criamos uma lista com os sorteados.

adcionarPessoa = input('Quem gostaria de adcionar? ')  #Insere o nome da pessoa.
quantidade = int(input('Quanto foi doado? ')) #Insere a quantia doada.

i = quantidade
while i > 0:
    listaSorteio.append(adcionarPessoa)
    i -= 10

#Faz um loop e adciona a quantidade de doação na lista.

print('Lista de sorteio: {}'.format(listaSorteio))
verify = int(input('Gostaria de sortear agora?   0 - Não   1 - Sim   '))
if verify == 1:
    random.shuffle(listaSorteio)
    sorteado = random.choice(listaSorteio)
    print('O sorteado foi: {}'.format(sorteado))
else:
    print('Encerrando programa...')

#Verifica se a pessoa gostaria de realizar o sorteio agora, caso a pessoa queira, realiza o sorteio, caso contrário, encerra o programa.