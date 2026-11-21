```mermaid
classDiagram
    class Exercicio {
        <<abstract>>
        +String nome
        +String grupo_muscular
        +calcular_calorias(peso)*
        +descrever()*
        +__str__()
    }

    class Cronometravel {
        <<interface>>
        +iniciar()
        +parar()
        +tempo_decorrido()
    }

    class Progressivo {
        <<interface>>
        +evoluir()
    }

    class Aerobico {
        +int duracao
        +calcular_calorias(peso)
        +descrever()
        +iniciar()
        +parar()
        +tempo_decorrido()
        +evoluir()
        +__str__()
    }

    class Corrida {
        +float distancia
        +calcular_calorias(peso)
        +descrever()
        +evoluir()
        +__str__()
    }

    class Natacao {
        +int piscinas
        +calcular_calorias(peso)
        +descrever()
        +evoluir()
    }

    class Musculacao {
        +int series
        +int repeticoes
        +float carga
        +calcular_calorias(peso)
        +descrever()
        +evoluir()
        +__str__()
    }

    class Alongamento {
        +int duracao_segundos
        +calcular_calorias(peso)
        +descrever()
        +__str__()
    }

    Exercicio <|-- Aerobico
    Exercicio <|-- Musculacao
    Exercicio <|-- Alongamento
    Aerobico <|-- Corrida
    Aerobico <|-- Natacao

    Cronometravel <|.. Aerobico
    Progressivo <|.. Aerobico
    Progressivo <|.. Musculacao
```