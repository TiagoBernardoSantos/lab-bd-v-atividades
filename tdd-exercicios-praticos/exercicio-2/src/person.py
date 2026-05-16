from __future__ import annotations
import re
from typing import List


class Email:
    def __init__(self, nome: str):
        self.nome = nome


class Person:
    def __init__(self, id: int, name: str, age: int, emails: List[Email] = None):
        self.id = id
        self.name = name
        self.age = age
        self.emails: List[Email] = emails if emails is not None else []


class PersonDAO:
    def save(self, p: Person) -> None:
        errors = self.isValidToInclude(p)
        if errors:
            raise ValueError(f"Pessoa inválida: {errors}")

    def isValidToInclude(self, p: Person) -> List[str]:
        errors: List[str] = []

        partes = p.name.strip().split()
        if len(partes) < 2:
            errors.append("O nome deve ser composto por ao menos 2 partes.")
        if not all(parte.isalpha() for parte in partes):
            errors.append("O nome deve ser composto apenas de letras.")

        if not (1 <= p.age <= 200):
            errors.append("A idade deve estar no intervalo [1, 200].")

        if not p.emails:
            errors.append("A pessoa deve ter pelo menos um e-mail associado.")
        else:
            padrao = re.compile(r'^.+@.+\..+$')
            for email in p.emails:
                if not padrao.match(email.nome):
                    errors.append(f"O e-mail '{email.nome}' está em formato inválido.")

        return errors
