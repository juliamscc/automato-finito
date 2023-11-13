class AutomatoFinito:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def reconhecer_palavra(self, palavra):
        estado_atual = self.estado_inicial

        for simbolo in palavra:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                # Se não houver transição, a palavra não é reconhecida
                return False

        # Verificar se o estado atual é um estado final
        return estado_atual in self.estados_finais