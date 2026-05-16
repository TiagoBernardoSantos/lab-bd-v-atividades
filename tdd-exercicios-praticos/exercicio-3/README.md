# Exercício 3 — Calculadora de Salário

Calcula o salário líquido de funcionários com base no cargo e salário-base, seguindo TDD.

## Regras de cálculo

| Cargo | Salário ≥ limite | Desconto | Salário < limite | Desconto |
|-------|-----------------|----------|-----------------|----------|
| DESENVOLVEDOR | ≥ R$ 3.000 | 20% | < R$ 3.000 | 10% |
| DBA | ≥ R$ 2.000 | 25% | < R$ 2.000 | 15% |
| TESTADOR | ≥ R$ 2.000 | 25% | < R$ 2.000 | 15% |
| GERENTE | ≥ R$ 5.000 | 30% | < R$ 5.000 | 20% |

## Estrutura
```
exercicio-3/
├── src/
│   └── calculadora_salario.py  
├── tests/
│   └── test_calculadora_salario.py
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
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
src/__init__.py                    0      0   100%
src/calculadora_salario.py        26      1    96%   37
------------------------------------------------------------
TOTAL                             26      1    96%

16 passed in 0.04s
```

> Linha 37 corresponde ao branch de cargo inválido/desconhecido — situação impossível via Enum tipado.

## Casos de teste (16 CTs)

| CT | Cargo | Cenário |
|----|-------|---------|
| 01 | DESENVOLVEDOR | Salário < 3000 → desconto 10% |
| 02 | DESENVOLVEDOR | Salário == 3000 → desconto 20% |
| 03 | DESENVOLVEDOR | Salário > 3000 → desconto 20% |
| 04 | DESENVOLVEDOR | Salário limite inferior (2999.99) → desconto 10% |
| 05 | DBA | Salário < 2000 → desconto 15% |
| 06 | DBA | Salário == 2000 → desconto 25% |
| 07 | DBA | Salário > 2000 → desconto 25% |
| 08 | DBA | Salário limite inferior (1999.99) → desconto 15% |
| 09 | TESTADOR | Salário < 2000 → desconto 15% |
| 10 | TESTADOR | Salário == 2000 → desconto 25% |
| 11 | TESTADOR | Salário > 2000 → desconto 25% |
| 12 | GERENTE | Salário < 5000 → desconto 20% |
| 13 | GERENTE | Salário == 5000 → desconto 30% |
| 14 | GERENTE | Salário > 5000 → desconto 30% |
| 15 | GERENTE | Salário limite inferior (4999.99) → desconto 20% |
