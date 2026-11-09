import pytest
from app.reservation import Stock, Reservation


# Fixture : créer un nouveau stock pour chaque test
@pytest.fixture
def stock():
    return Stock(5)


# 1. Réservation réussie de 2 unités
def test_reservation_2_unites(stock):
    reservation = Reservation(stock)

    resultat = reservation.reserver(2)

    assert resultat == "confirmee"
    assert stock.quantite == 3


# 2. Réservation refusée de 6 unités
def test_reservation_6_unites(stock):
    reservation = Reservation(stock)

    resultat = reservation.reserver(6)

    assert resultat == "refusee"
    assert stock.quantite == 5


# 3. Réservation de toutes les unités disponibles
def test_reservation_5_unites(stock):
    reservation = Reservation(stock)

    resultat = reservation.reserver(5)

    assert resultat == "confirmee"
    assert stock.quantite == 0


# 4. Réservation d'une quantité nulle
def test_reservation_quantite_zero(stock):
    reservation = Reservation(stock)

    with pytest.raises(ValueError):
        reservation.reserver(0)

    assert stock.quantite == 5