import pytest 
from app.texte import nettoyer_texte


def test_text():
    assert nettoyer_texte("  BONJOUR   monde  ") == "bonjour monde"  



@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("Bonjour", "bonjour"),
    ("HELLO", "hello"),
])

def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

@pytest.mark.parametrize("entree", [123, None])
def test_nettoyer_texte_entree_non_textuelle(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


def test_nettoyer_texte_deja_nettoye():
    texte = "bonjour monde"
    resultat = nettoyer_texte(texte)
    assert nettoyer_texte(resultat) == resultat

# Vérifier les entrées non textuelles
@pytest.mark.parametrize("entree", [123, None])
def test_nettoyer_texte_entree_non_textuelle(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


# Vérifier que le nettoyage est idempotent
def test_nettoyer_texte_deja_nettoye():
    texte = "bonjour monde"

    resultat = nettoyer_texte(texte)

    assert nettoyer_texte(resultat) == resultat