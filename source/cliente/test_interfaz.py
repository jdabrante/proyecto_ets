import interfaz
import pytest

r = interfaz.Round('AHAS')
g = interfaz.Game('Javier')

def test_build_round():
    assert r.hand == 'AHAS'
    assert r.outcome == "unknown"


def test_build_game():
    assert g.name == "Javier"
    assert g.rounds == []
    assert g.next_available_round_id == 0
