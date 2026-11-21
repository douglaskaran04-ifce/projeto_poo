from modelos.academia import (
    Exercicio,
    Aerobico,
    Corrida,
    Natacao,
    Musculacao,
    Alongamento,
)
from modelos.interfaces import Cronometravel, Progressivo

# 1. Teste de erro ao tentar instanciar a classe abstrata Exercicio
print("=== TESTE DE CLASSE ABSTRATA ===")
try:
    exercicio_generico = Exercicio("Exercício Genérico", "Corpo Todo")
except TypeError as erro:
    print(f"Erro esperado: {erro}\n")

peso_aluno = 75.0  # Peso de referência em kg para o cálculo de calorias

# Lista contendo objetos de todas as classes folha
treino_do_dia = [
    Corrida("Corrida na Esteira", "Pernas / Cardio", 30, 5.0),
    Natacao("Nado Crawl", "Corpo Inteiro", 45, 20),
    Musculacao("Supino Reto", "Peitoral", 4, 12, 40.0),
    Alongamento("Alongamento Posterior", "Isquiotibiais e Lombar", 120),
]

print(f"=== FICHA DE TREINO (Aluno: {peso_aluno} kg) ===\n")

for exercicio in treino_do_dia:
    print(exercicio)  # Chama polimorficamente o método concreto __str__()
    print(exercicio.descrever())  # Método abstrato implementado nas subclasses
    print(f"Gasto estimado: {exercicio.calcular_calorias(peso_aluno):.2f} kcal")  # Método abstrato

    # Uso de isinstance() para verificar contratos (interfaces)
    if isinstance(exercicio, Cronometravel):
        print(f"  [Cronômetro] {exercicio.iniciar()} -> {exercicio.tempo_decorrido()}")

    if isinstance(exercicio, Progressivo):
        print(f"  [Progressão] {exercicio.evoluir()}")

    print("-" * 60)

# Verificações explícitas com isinstance()
print("Verificações de contrato com isinstance():")
print(f"Corrida é Cronometravel? {isinstance(treino_do_dia[0], Cronometravel)}")
print(f"Musculacao é Cronometravel? {isinstance(treino_do_dia[2], Cronometravel)}")
print(f"Musculacao é Progressivo? {isinstance(treino_do_dia[2], Progressivo)}")
print(f"Alongamento é Progressivo? {isinstance(treino_do_dia[3], Progressivo)}")