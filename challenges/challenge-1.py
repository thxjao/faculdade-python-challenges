# Exercicio 1

answr = int(input('Inserir dados?   0 - Não   1 - Sim   '))
print(answr)
if answr == 1:
    nome = input('Nome do aluno(a): ')
    nota = input('Nota final: ')
    notaFloated = float(nota)
    if notaFloated >= 0 and notaFloated < 3:
        conceito = 'E'
    elif notaFloated >= 3 and notaFloated < 5:
        conceito = 'D'
    elif notaFloated >= 5 and notaFloated < 7:
        conceito = 'C'
    elif notaFloated >= 7 and notaFloated < 9:
        conceito = 'B'
    else:
        conceito = 'A'
    print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(nome, nota, conceito))