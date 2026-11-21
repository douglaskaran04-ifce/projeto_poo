# Sistema de Gestão de Treinos — Tema: Academia

**Objetivo do sistema:** Gerenciar rotinas de treinos e calcular de forma polimórfica o gasto calórico e o detalhamento de exercícios aeróbicos, de musculação e de alongamento.

## Integrantes da Equipe
- Douglas Karan
- Carlos Jefferson
- Fernando Carvalho

## Documentação e Modelagem
- [Diagrama de Classes (Mermaid)](docs/diagrama.md)

## Parte 2 — Classes Abstratas e Interfaces

Nesta etapa, aplicamos os conceitos de abstração e contratos utilizando o módulo `abc` do Python:

- **Classe Abstrata (`Exercicio`):** Herda de `ABC` e impede que um exercício genérico seja instanciado diretamente. Possui os métodos abstratos `calcular_calorias(peso)` e `descrever()`, além do método concreto `__str__()`, que é reaproveitado por toda a hierarquia.
- **Interfaces (`modelos/interfaces.py`):**
  - **`Cronometravel`:** Define os métodos `iniciar()`, `parar()` e `tempo_decorrido()`. É implementada pela classe `Aerobico` (e herdada por `Corrida` e `Natacao`).
  - **`Progressivo`:** Define o método `evoluir()` para progressão de treino (tempo, distância, piscinas ou carga). É implementada por `Aerobico` (`Corrida` e `Natacao`) e `Musculacao`.
- **Classe sem interfaces (`Alongamento`):** Herda apenas de `Exercicio`, demonstrando que interfaces representam capacidades específicas e não pertencem obrigatoriamente a toda a família de classes.
