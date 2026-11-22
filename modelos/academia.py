from abc import ABC, abstractmethod
from modelos.interfaces import Cronometravel, Progressivo


class Exercicio(ABC):
    def __init__(self, nome, grupo_muscular):
        self.nome = nome
        self.grupo_muscular = grupo_muscular

    @abstractmethod
    def calcular_calorias(self, peso):
        pass

    @abstractmethod
    def descrever(self):
        pass

    def __str__(self):
        return f"{self.nome} ({self.grupo_muscular})"


class Aerobico(Exercicio, Cronometravel, Progressivo):
    def __init__(self, nome, grupo_muscular, duracao):
        super().__init__(nome, grupo_muscular)
        self.duracao = duracao  # duração em minutos

    def calcular_calorias(self, peso):
        # Gasto basal (peso * 0.5) + gasto por minuto de exercício aeróbico
        return (peso * 0.5) + (self.duracao * peso * 0.08)

    def descrever(self):
        return (
            f"Exercício: {self.nome} | Grupo muscular: {self.grupo_muscular}"
            f" | Duração: {self.duracao} min"
        )

    def iniciar(self):
        return f"Cronômetro iniciado para {self.nome}."

    def parar(self):
        return f"Cronômetro pausado em {self.nome}."

    def tempo_decorrido(self):
        return f"Tempo registrado: {self.duracao} minutos."

    def evoluir(self):
        self.duracao += 5
        return f"Evolução em {self.nome}: duração aumentada para {self.duracao} min."

    def __str__(self):
        return super().__str__() + f" - {self.duracao} min"


class Corrida(Aerobico):
    def __init__(self, nome, grupo_muscular, duracao, distancia):
        super().__init__(nome, grupo_muscular, duracao)
        self.distancia = distancia  # distância em km

    def calcular_calorias(self, peso):
        # Aproveita o cálculo aeróbico e adiciona o gasto por distância
        return super().calcular_calorias(peso) + (self.distancia * peso * 0.5)

    def descrever(self):
        return super().descrever() + f" | Distância: {self.distancia:.1f} km"

    def evoluir(self):
        self.distancia += 0.5
        return f"Evolução em {self.nome}: distância aumentada para {self.distancia:.1f} km."

    def __str__(self):
        return super().__str__() + f" ({self.distancia:.1f} km)"


class Natacao(Aerobico):
    def __init__(self, nome, grupo_muscular, duracao, piscinas):
        super().__init__(nome, grupo_muscular, duracao)
        self.piscinas = piscinas

    def calcular_calorias(self, peso):
        # Aproveita o cálculo aeróbico e adiciona o gasto por piscina
        return super().calcular_calorias(peso) + (self.piscinas * 6.5)

    def descrever(self):
        return super().descrever() + f" | Piscinas: {self.piscinas}"

    def evoluir(self):
        self.piscinas += 2
        return f"Evolução em {self.nome}: meta aumentada para {self.piscinas} piscinas."


class Musculacao(Exercicio, Progressivo):
    def __init__(self, nome, grupo_muscular, series, repeticoes, carga):
        super().__init__(nome, grupo_muscular)
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga  # carga em kg

    def calcular_calorias(self, peso):
        volume_treino = self.series * self.repeticoes * (self.carga * 0.1)
        return (peso * 0.5) + volume_treino

    def descrever(self):
        return (
            f"Exercício: {self.nome} | Grupo muscular: {self.grupo_muscular}"
            f" | Treino: {self.series}x{self.repeticoes} com {self.carga:.1f} kg"
        )

    def evoluir(self):
        self.carga += 2.0
        return f"Evolução em {self.nome}: carga aumentada para {self.carga:.1f} kg."

    def __str__(self):
        return super().__str__() + f" [{self.series}x{self.repeticoes} - {self.carga:.1f}kg]"


class Alongamento(Exercicio):
    def __init__(self, nome, grupo_muscular, duracao_segundos):
        super().__init__(nome, grupo_muscular)
        self.duracao_segundos = duracao_segundos

    def calcular_calorias(self, peso):
        return (peso * 0.5) + (self.duracao_segundos * 0.05)

    def descrever(self):
        return (
            f"Exercício: {self.nome} | Grupo muscular: {self.grupo_muscular}"
            f" | Tempo: {self.duracao_segundos}s"
        )

    def __str__(self):
        return super().__str__() + f" - {self.duracao_segundos}s"