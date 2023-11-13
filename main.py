from automato import *

#Ler Arquivo
with open('teste.txt', 'r') as arquivo:

    linhas = arquivo.readlines()

linha_desejada = linhas[3]
minha_variavel = linha_desejada.strip()
print(minha_variavel)

# # Exemplo antigo
# estados = {'A', 'B', 'C'}
# estado_inicial = 'A'
# estados_finais = {'C'}
# transicoes = {('A', 'a'): 'B', ('B', 'b'): 'C'}

# automato = AutomatoFinito(estados, estado_inicial, estados_finais, transicoes)

# palavra_teste = 'ab'
# print(automato.reconhecer_palavra(palavra_teste))
