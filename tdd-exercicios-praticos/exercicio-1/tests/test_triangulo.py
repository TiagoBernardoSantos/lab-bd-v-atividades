import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from triangulo import classificar_triangulo, TipoTriangulo


class TestTriangulo:

    # CT01 - Triângulo escaleno válido
    def test_ct01_escaleno_valido(self):
        resultado = classificar_triangulo(3, 4, 5)
        assert resultado == TipoTriangulo.ESCALENO

    # CT02 - Triângulo isósceles válido
    def test_ct02_isosceles_valido(self):
        resultado = classificar_triangulo(5, 5, 3)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT03 - Triângulo equilátero válido
    def test_ct03_equilatero_valido(self):
        resultado = classificar_triangulo(4, 4, 4)
        assert resultado == TipoTriangulo.EQUILATERO

    # CT04 - Isósceles permutação 1: (a == b)
    def test_ct04_isosceles_permutacao_ab(self):
        resultado = classificar_triangulo(5, 5, 3)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT05 - Isósceles permutação 2: (b == c)
    def test_ct05_isosceles_permutacao_bc(self):
        resultado = classificar_triangulo(3, 5, 5)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT06 - Isósceles permutação 3: (a == c)
    def test_ct06_isosceles_permutacao_ac(self):
        resultado = classificar_triangulo(5, 3, 5)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT07 - Um valor zero
    def test_ct07_valor_zero(self):
        with pytest.raises(ValueError, match="maiores que zero"):
            classificar_triangulo(0, 4, 5)

    # CT08 - Um valor negativo
    def test_ct08_valor_negativo(self):
        with pytest.raises(ValueError, match="maiores que zero"):
            classificar_triangulo(-1, 4, 5)

    # CT09 - Soma de 2 lados igual ao terceiro (a + b == c)
    def test_ct09_soma_igual_terceiro_ab_c(self):
        with pytest.raises(ValueError, match="não formam um triângulo válido"):
            classificar_triangulo(3, 4, 7)

    # CT10 - Soma de 2 lados igual ao terceiro, permutação (a + c == b)
    def test_ct10_soma_igual_terceiro_ac_b(self):
        with pytest.raises(ValueError, match="não formam um triângulo válido"):
            classificar_triangulo(3, 7, 4)

    # CT11 - Soma de 2 lados igual ao terceiro, permutação (b + c == a)
    def test_ct11_soma_igual_terceiro_bc_a(self):
        with pytest.raises(ValueError, match="não formam um triângulo válido"):
            classificar_triangulo(7, 3, 4)

    # CT12 - Soma de 2 lados menor que o terceiro (a + b < c)
    def test_ct12_soma_menor_terceiro_ab_c(self):
        with pytest.raises(ValueError, match="não formam um triângulo válido"):
            classificar_triangulo(1, 2, 10)

    # CT13 - Soma de 2 lados menor que o terceiro, permutação (a + c < b)
    def test_ct13_soma_menor_terceiro_ac_b(self):
        with pytest.raises(ValueError, match="não formam um triângulo válido"):
            classificar_triangulo(1, 10, 2)

    # CT14 - Soma de 2 lados menor que o terceiro, permutação (b + c < a)
    def test_ct14_soma_menor_terceiro_bc_a(self):
        with pytest.raises(ValueError, match="não formam um triângulo válido"):
            classificar_triangulo(10, 1, 2)

    # CT15 - Três valores iguais a zero
    def test_ct15_todos_zero(self):
        with pytest.raises(ValueError, match="maiores que zero"):
            classificar_triangulo(0, 0, 0)
