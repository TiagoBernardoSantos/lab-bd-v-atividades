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

8 passed in 0.05s
```

> Linhas 21-23 correspondem ao bloco `raise` dentro de `save()`, não coberto intencionalmente pois é lógica de persistência.

## Casos de teste (8 CTs)

| CT | Descrição |
|----|-----------|
| CT01 | Pessoa completamente válida |
| CT02 | Nome com apenas uma parte |
| CT03 | Nome com números |
| CT04 | Idade fora do intervalo (zero) |
| CT05 | Idade fora do intervalo (acima de 200) |
| CT06 | Sem e-mails associados |
| CT07 | E-mail com formato inválido |
| CT08 | Múltiplos erros simultâneos |
