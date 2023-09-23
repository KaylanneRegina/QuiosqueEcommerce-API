from django.test import TestCase
from produtos.models import Categoria

@pytest.mark.django_db

def test_categoria_create():
    Categoria.objects.create(nome='Categoria A')
    assert Categoria.objects.count() == 1
    