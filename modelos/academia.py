class Exercicio:
    def __init__(self, nome, grupo_muscular):
        self.nome = nome
        self.grupo_muscular = grupo_muscular

    def calcular_calorias(self, peso):
        # Gasto basal padrão de referência para qualquer exercício
        return peso * 0.5

    def descrever(self):
        return f"Exercício: {self.nome} | Grupo muscular: {self.grupo_muscular}"

    def __str__(self):
        return f"{self.nome} ({self.grupo_muscular})"


class Aerobico(Exercicio):
    def __init__(self, nome, grupo_muscular, duracao):
        super().__init__(nome, grupo_muscular)
        self.duracao = duracao  # duração em minutos

    def calcular_calorias(self, peso):
        # Aproveita o cálculo base com super() e adiciona o gasto por minuto
        return super().calcular_calorias(peso) + (self.duracao * peso * 0.08)

    def descrever(self):
        return super().descrever() + f" | Duração: {self.duracao} min"

    def __str__(self):
        return super().__str__() + f" - {self.duracao} min"


class Corrida(Aerobico):
    def __init__(self, nome, grupo_muscular, duracao, distancia):
        super().__init__(nome, grupo_muscular, duracao)
        self.distancia = distancia  # distância em km

    def calcular_calorias(self, peso):
        # Soma o gasto aeróbico por tempo com o gasto por quilômetro percorrido
        return super().calcular_calorias(peso) + (self.distancia * peso * 0.5)

    def descrever(self):
        return super().descrever() + f" | Distância: {self.distancia:.1f} km"

    def __str__(self):
        return super().__str__() + f" ({self.distancia:.1f} km)"


class Natacao(Aerobico):
    def __init__(self, nome, grupo_muscular, duracao, piscinas):
        super().__init__(nome, grupo_muscular, duracao)
        self.piscinas = piscinas

    def calcular_calorias(self, peso):
        # Soma o gasto aeróbico com o esforço adicional por piscina nadada
        return super().calcular_calorias(peso) + (self.piscinas * 6.5)

    def descrever(self):
        return super().descrever() + f" | Piscinas: {self.piscinas}"


class Musculacao(Exercicio):
    def __init__(self, nome, grupo_muscular, series, repeticoes, carga):
        super().__init__(nome, grupo_muscular)
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga  # carga em kg

    def calcular_calorias(self, peso):
        volume_treino = self.series * self.repeticoes * (self.carga * 0.1)
        return super().calcular_calorias(peso) + volume_treino

    def descrever(self):
        return (
            super().descrever()
            + f" | Treino: {self.series}x{self.repeticoes} com {self.carga:.1f} kg"
        )

    def __str__(self):
        return super().__str__() + f" [{self.series}x{self.repeticoes} - {self.carga:.1f}kg]"


class Alongamento(Exercicio):
    def __init__(self, nome, grupo_muscular, duracao_segundos):
        super().__init__(nome, grupo_muscular)
        self.duracao_segundos = duracao_segundos

    def calcular_calorias(self, peso):
        return super().calcular_calorias(peso) + (self.duracao_segundos * 0.05)

    def descrever(self):
        return super().descrever() + f" | Tempo: {self.duracao_segundos}s"

    def __str__(self):
        return super().__str__() + f" - {self.duracao_segundos}s"