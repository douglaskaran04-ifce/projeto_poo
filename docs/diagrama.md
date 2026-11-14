classDiagram
    class Exercicio {
        <<abstract>>
        +String nome
        +String grupo_muscular
        +calcular_calorias(peso: float) float*
        +descrever() String*
    }

    class Aerobico {
        +int duracao
    }

    class Corrida {
        +float distancia
        +calcular_calorias(peso: float) float
        +descrever() String
    }

    class Natacao {
        +int piscinas
        +calcular_calorias(peso: float) float
        +descrever() String
    }

    class Musculacao {
        +int series
        +int repeticoes
        +float carga
        +calcular_calorias(peso: float) float
        +descrever() String
    }

    class Alongamento {
        +calcular_calorias(peso: float) float
        +descrever() String
    }

    %% Relacionamentos de Herança
    Exercicio <|-- Aerobico
    Exercicio <|-- Musculacao
    Exercicio <|-- Alongamento
    
    Aerobico <|-- Corrida
    Aerobico <|-- Natacao