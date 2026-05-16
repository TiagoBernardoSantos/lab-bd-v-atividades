import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from person import Person, Email, PersonDAO


class TestPersonDAO:

    def setup_method(self):
        self.dao = PersonDAO()

    def _pessoa_valida(self):
        return Person(1, "João Silva", 30, [Email("joao@email.com")])

    # CT01 - Pessoa completamente válida
    def test_ct01_pessoa_valida(self):
        p = self._pessoa_valida()
        assert self.dao.isValidToInclude(p) == []

    # CT02 - Nome com apenas uma parte
    def test_ct02_nome_uma_parte(self):
        p = self._pessoa_valida()
        p.name = "João"
        erros = self.dao.isValidToInclude(p)
        assert any("2 partes" in e for e in erros)

    # CT03 - Nome com números
    def test_ct03_nome_com_numeros(self):
        p = self._pessoa_valida()
        p.name = "João 123"
        erros = self.dao.isValidToInclude(p)
        assert any("apenas de letras" in e for e in erros)

    # CT04 - Idade fora do intervalo (zero)
    def test_ct04_idade_zero(self):
        p = self._pessoa_valida()
        p.age = 0
        erros = self.dao.isValidToInclude(p)
        assert any("idade" in e.lower() for e in erros)

    # CT05 - Idade fora do intervalo (acima de 200)
    def test_ct05_idade_acima_200(self):
        p = self._pessoa_valida()
        p.age = 201
        erros = self.dao.isValidToInclude(p)
        assert any("idade" in e.lower() for e in erros)

    # CT06 - Sem e-mails associados
    def test_ct06_sem_emails(self):
        p = self._pessoa_valida()
        p.emails = []
        erros = self.dao.isValidToInclude(p)
        assert any("e-mail" in e.lower() for e in erros)

    # CT07 - E-mail com formato inválido
    def test_ct07_email_invalido(self):
        p = self._pessoa_valida()
        p.emails = [Email("emailinvalido")]
        erros = self.dao.isValidToInclude(p)
        assert any("inválido" in e for e in erros)

    # CT08 - Múltiplos erros simultâneos
    def test_ct08_multiplos_erros(self):
        p = Person(99, "X", 0, [])
        erros = self.dao.isValidToInclude(p)
        assert len(erros) >= 3
