# Exercicio 1

answr = int(input('Inserir dados?   0 - Não   1 - Sim   ')) #Pergunta se a pessoa gostaria de inserir os dados
if answr == 1: # Verifica se o resultado for = True, e continua coma  operação
    nome = input('Nome do aluno(a): ') #Capta o nome e isola em uma variável.
    nota = input('Nota final: ') #Capta a nota no data tipo de STR e isola em uma variável.
    notaFloated = float(nota) #Transforma a variável de DataType STR para "Number" seja "INT" ou "FLOAT".
    if notaFloated >= 0 and notaFloated < 3:
        conceito = 'E'                              #A partir desse processo é realizado uma verificação que de acordo com o tamanho da nota retorna uma variável com o conceito.
    elif notaFloated >= 3 and notaFloated < 5:   
        conceito = 'D'
    elif notaFloated >= 5 and notaFloated < 7:
        conceito = 'C'
    elif notaFloated >= 7 and notaFloated < 9:
        conceito = 'B'
    else:
        conceito = 'A'
    print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome, nota, conceito)) #Retorn o Output com as variáveis inseridas no programa.
else: #Caso a operação seja negada finaliza o processo.
    print('Encerrando...')