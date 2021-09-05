def geradorDeEmail(nome, sobrenome): # A função capta seu nome e sobrenome, guardando os itens em um variável
    primeiraLetra = nome[0] # Isola a primeira letra da STR em outra váriavel
    print('{}{}@algoritmos.com.br'.format(primeiraLetra,sobrenome)) # Gera o email

geradorDeEmail('joao', 'pedro42') # Teste executado