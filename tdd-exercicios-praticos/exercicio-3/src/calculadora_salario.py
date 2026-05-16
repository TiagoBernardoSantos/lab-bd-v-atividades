from enum import Enum


class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


class Funcionario:
    def __init__(self, nome: str, email: str, salario_base: float, cargo: Cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo


class CalculadoraSalario:
    def calcular_salario_liquido(self, funcionario: Funcionario) -> float:
        salario = funcionario.salario_base
        cargo = funcionario.cargo

        if cargo == Cargo.DESENVOLVEDOR:
            desconto = 0.20 if salario >= 3000.00 else 0.10

        elif cargo == Cargo.DBA:
            desconto = 0.25 if salario >= 2000.00 else 0.15

        elif cargo == Cargo.TESTADOR:
            desconto = 0.25 if salario >= 2000.00 else 0.15

        elif cargo == Cargo.GERENTE:
            desconto = 0.30 if salario >= 5000.00 else 0.20

        else:
            raise ValueError(f"Cargo desconhecido: {cargo}")

        return round(salario * (1 - desconto), 2)
