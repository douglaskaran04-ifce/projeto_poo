from modelos.academia import (
    Exercicio,
    Aerobico,
    Corrida,
    Natacao,
    Musculacao,
    Alongamento,
)

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
    print(exercicio)  # Chama polimorficamente o método __str__()
    print(exercicio.descrever())  # 1º método polimórfico
    print(f"Gasto estimado: {exercicio.calcular_calorias(peso_aluno):.2f} kcal")  # 2º método polimórfico
    print("-" * 55)

# Verificação de herança com isinstance()
print("Verificações com isinstance():")
print(f"Corrida é instância de Exercicio? {isinstance(treino_do_dia[0], Exercicio)}")
print(f"Corrida é instância de Aerobico? {isinstance(treino_do_dia[0], Aerobico)}")
print(f"Musculacao é instância de Exercicio? {isinstance(treino_do_dia[2], Exercicio)}")