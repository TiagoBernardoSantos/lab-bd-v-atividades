import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora_salario import CalculadoraSalario, Funcionario, Cargo


class TestCalculadoraSalario:

    def setup_method(self):
        self.calc = CalculadoraSalario()

    # CT01 - DESENVOLVEDOR salário < 3000 → desconto 10%
    def test_ct01_desenvolvedor_desconto_10(self):
        f = Funcionario("Ana", "ana@email.com", 2000.00, Cargo.DESENVOLVEDOR)
        assert self.calc.calcular_salario_liquido(f) == 1800.00

    # CT02 - DESENVOLVEDOR salário >= 3000 → desconto 20%
    def test_ct02_desenvolvedor_desconto_20(self):
        f = Funcionario("Ana", "ana@email.com", 3000.00, Cargo.DESENVOLVEDOR)
        assert self.calc.calcular_salario_liquido(f) == 2400.00

    # CT03 - DBA salário < 2000 → desconto 15%
    def test_ct03_dba_desconto_15(self):
        f = Funcionario("Bob", "bob@email.com", 1500.00, Cargo.DBA)
        assert self.calc.calcular_salario_liquido(f) == 1275.00

    # CT04 - DBA salário >= 2000 → desconto 25%
    def test_ct04_dba_desconto_25(self):
        f = Funcionario("Bob", "bob@email.com", 2000.00, Cargo.DBA)
        assert self.calc.calcular_salario_liquido(f) == 1500.00

    # CT05 - TESTADOR salário < 2000 → desconto 15%
    def test_ct05_testador_desconto_15(self):
        f = Funcionario("Carlos", "carlos@email.com", 1800.00, Cargo.TESTADOR)
        assert self.calc.calcular_salario_liquido(f) == 1530.00

    # CT06 - TESTADOR salário >= 2000 → desconto 25%
    def test_ct06_testador_desconto_25(self):
        f = Funcionario("Carlos", "carlos@email.com", 2000.00, Cargo.TESTADOR)
        assert self.calc.calcular_salario_liquido(f) == 1500.00

    # CT07 - GERENTE salário < 5000 → desconto 20%
    def test_ct07_gerente_desconto_20(self):
        f = Funcionario("Diana", "diana@email.com", 4000.00, Cargo.GERENTE)
        assert self.calc.calcular_salario_liquido(f) == 3200.00

    # CT08 - GERENTE salário >= 5000 → desconto 30%
    def test_ct08_gerente_desconto_30(self):
        f = Funcionario("Diana", "diana@email.com", 5000.00, Cargo.GERENTE)
        assert self.calc.calcular_salario_liquido(f) == 3500.00
