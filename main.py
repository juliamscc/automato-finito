from automato import *

# Exemplo de uso:
estados = {'A', 'B', 'C'}
estado_inicial = 'A'
estados_finais = {'C'}
transicoes = {('A', 'a'): 'B', ('B', 'b'): 'C'}
automato = AutomatoFinito(estados, estado_inicial, estados_finais, transicoes)

palavra_teste = 'ab'
print(automato.reconhecer_palavra(palavra_teste))  # Saída: True
