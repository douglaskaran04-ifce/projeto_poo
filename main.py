from modelos.academia import (
    Exercicio,
    Aerobico,
    Corrida,
    Natacao,
    Musculacao,
    Alongamento,
)

def obter_peso():
    """Pede o peso ao usuário com validação simples."""
    while True:
        try:
            peso = float(input("Digite o peso do aluno (kg): "))
            if peso > 0:
                return peso
            print("O peso deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def executar_treino(peso_aluno):
    """Cria a lista de exercícios e executa o laço polimórfico."""
    # Lista heterogênea
    treino_do_dia = [
        Corrida("Corrida na Esteira", "Pernas / Cardio", 30, 5.0),
        Natacao("Nado Crawl", "Corpo Inteiro", 45, 20),
        Musculacao("Supino Reto", "Peitoral", 4, 12, 40.0),
        Alongamento("Alongamento Posterior", "Isquiotibiais e Lombar", 120),
    ]

    print(f"\n=== FICHA DE TREINO (Aluno: {peso_aluno} kg) ===\n")
    
    total_calorias = 0.0

    for exercicio in treino_do_dia:
        print(exercicio)
        print(exercicio.descrever())
        
        calorias = exercicio.calcular_calorias(peso_aluno)
        print(f"Gasto estimado: {calorias:.2f} kcal")
        print("-" * 55)
        
        total_calorias += calorias

    print(f"\n🔥 GASTO CALÓRICO TOTAL DO TREINO: {total_calorias:.2f} kcal\n")

    # Testes de isinstance usando os próprios objetos
    # Encontrando os objetos na lista para não depender da posição fixa
    obj_corrida = next(x for x in treino_do_dia if isinstance(x, Corrida))
    obj_musculacao = next(x for x in treino_do_dia if isinstance(x, Musculacao))
    
    print("--- VERIFICAÇÕES DE HERANÇA (isinstance) ---")
    print(f"Corrida é instância de Exercicio? {isinstance(obj_corrida, Exercicio)}")
    print(f"Corrida é instância de Aerobico?  {isinstance(obj_corrida, Aerobico)}")
    print(f"Musculacao é instância de Exercicio? {isinstance(obj_musculacao, Exercicio)}")
    # Exemplo extra para provar que funciona:
    print(f"Corrida é instância de Musculacao? {isinstance(obj_corrida, Musculacao)}")

if __name__ == "__main__":
    # O programa começa aqui
    print("Bem-vindo ao Sistema de Academia!")
    peso = obter_peso()
    executar_treino(peso)