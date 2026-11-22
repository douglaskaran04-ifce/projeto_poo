from abc import ABC, abstractmethod


class Cronometravel(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def parar(self):
        pass

    @abstractmethod
    def tempo_decorrido(self):
        pass


class Progressivo(ABC):
    @abstractmethod
    def evoluir(self):
        pass