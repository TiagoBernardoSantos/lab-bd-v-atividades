# Exercício 1 — Triângulo

Classifica um triângulo como **Escaleno**, **Isósceles** ou **Equilátero** com base em três lados inteiros.

## Regras
- Os lados devem ser maiores que zero
- A soma de dois lados deve ser maior que o terceiro lado

## Estrutura
```
exercicio-1/
├── src/
│   └── triangulo.py
├── tests/
│   └── test_triangulo.py
└── requirements.txt
```

## Instalação
```bash
pip install -r requirements.txt
```

## Executar testes
```bash
pytest tests/ -v
```

## Cobertura
```bash
pytest tests/ --cov=src --cov-report=term-missing
```

## Evidência de cobertura

```
Name                  Stmts   Miss  Cover
-----------------------------------------
src/__init__.py           0      0   100%
src/triangulo.py         15      0   100%
-----------------------------------------
TOTAL                    15      0   100%

15 passed in 0.05s
```

## Casos de teste (15 CTs)

| CT | Descrição |
|----|-----------|
| CT01 | Triângulo escaleno válido |
| CT02 | Triângulo isósceles válido |
| CT03 | Triângulo equilátero válido |
| CT04 | Isósceles — permutação a == b |
| CT05 | Isósceles — permutação b == c |
| CT06 | Isósceles — permutação a == c |
| CT07 | Um valor zero |
| CT08 | Um valor negativo |
| CT09 | Soma de 2 lados igual ao terceiro (a+b == c) |
| CT10 | Soma de 2 lados igual ao terceiro (a+c == b) |
| CT11 | Soma de 2 lados igual ao terceiro (b+c == a) |
| CT12 | Soma de 2 lados menor que o terceiro (a+b < c) |
| CT13 | Soma de 2 lados menor que o terceiro (a+c < b) |
| CT14 | Soma de 2 lados menor que o terceiro (b+c < a) |
| CT15 | Todos os três valores iguais a zero |
