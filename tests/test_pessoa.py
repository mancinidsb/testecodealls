# from ..classes.Pessoa import Pessoa
from classes.Pessoa import Pessoa

def test_pessoa_construction():
    p1 = Pessoa("ana", 15, 55, 1.67)

    assert p1.altura ==1.67
    assert p1.nome == "ana"
    assert p1.peso == 55
    assert p1.idade == 15

def test_pessoa_imc():
    p1 = Pessoa("pedro", 22, 65, 1.74)

    assert p1.calcula_imc() == 21.47

def test_pessoa_str():
    p1 = Pessoa("marcia", 34, 71, 1.70)

    assert f"{p1}" == f"nome: {p1.nome} | idade: {p1.idade} | peso: {p1.peso} | altura: {p1.altura} -> IMC: {p1.calcula_imc()}"