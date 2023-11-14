from automato import *

# Função para formatar os dados das transições:
def formatar_transicoes(lista_de_transicoes):
    transicoes = {}
    for item in lista_de_transicoes:
        lista = item.split('-')
        tupla = tuple(lista[0].split())
        transicoes[tupla]=lista[1]
    return transicoes

#Ler Arquivo
with open('gramaticas/teste.txt', 'r') as arquivo:
    lista_dados = [linha.strip() for linha in arquivo]

estados = lista_dados[0].split()
estado_inicial = lista_dados[1]
estados_finais = lista_dados[2].split()
lista_de_transicoes = lista_dados[3:]
transicoes = formatar_transicoes(lista_de_transicoes)

# print(estados)
# print(estado_inicial)
# print(estados_finais)
# print(transicoes)

automato = AutomatoFinito(estados, estado_inicial, estados_finais, transicoes)
palavra_teste = input("Insira uma palavra para verificar:")

resultado = automato.reconhecer_palavra(palavra_teste)
if automato.reconhecer_palavra(palavra_teste) == True:
    print("A palavra é reconhecida")
else:
    print("A palavra não é reconhecida")    