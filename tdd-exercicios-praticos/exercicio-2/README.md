# Exercício 2 — PersonDAO / isValidToInclude()

Implementação TDD do método `isValidToInclude(p: Person) -> List[str]` que retorna uma lista de erros de validação.

## Regras de validação
- Nome composto por ao menos 2 partes, somente letras
- Idade no intervalo [1, 200]
- Ao menos um e-mail associado
- Formato de e-mail: `algo@dominio.extensao`

## Estrutura
```
exercicio-2/
├── src/
│   └── person.py       # Classes: Email, Person, PersonDAO
├── tests/
│   └── test_person_dao.py
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
Name                Stmts   Miss  Cover   Missing
--------------------------------------------------
src/__init__.py         0      0   100%
src/person.py          33      3    91%   21-23
--------------------------------------------------
TOTAL                  33      3    91%

20 passed in 0.05s
```

> Linhas 21-23 correspondem ao bloco `raise` dentro de `save()`, não coberto intencionalmente pois é lógica de persistência.

## Casos de teste (20 CTs)

| CT | Descrição |
|----|-----------|
| 01 | Nome válido (caso base) |
| 02 | Nome com apenas uma parte |
| 03 | Nome vazio |
| 04 | Nome com números |
| 05 | Nome com caracteres especiais |
| 06 | Nome com duas partes válidas |
| 07 | Nome com três partes válidas |
| 08 | Idade válida no limite inferior (1) |
| 09 | Idade válida no limite superior (200) |
| 10 | Idade zero |
| 11 | Idade negativa |
| 12 | Idade acima de 200 |
| 13 | Sem e-mails associados |
| 14 | E-mail com formato válido |
| 15 | E-mail sem @ |
| 16 | E-mail sem ponto |
| 17 | E-mail sem domínio |
| 18 | E-mail vazio |
| 19 | Múltiplos e-mails válidos |
| 20 | Um e-mail inválido entre válidos |
| 21 | Múltiplos erros simultâneos |
