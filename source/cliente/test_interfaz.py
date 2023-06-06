import interfaz
import pytest

r = interfaz.Round("AHAS")
g = interfaz.Game("Javier")
m = interfaz.Map(r, g)


def test_build_round():
    assert r.hand == "AHAS"
    assert r.outcome == "unknown"


def test_build_game():
    assert g.name == "Javier"
    assert g.rounds == []
    assert g.next_available_round_id == 0


def test_add_round():
    id = g.next_available_round_id
    g.add_round(r)
    assert g.rounds[-1] == r
    assert r.number == id
    assert g.next_available_round_id == id + 1


def test_build_map():
    m.odds == g.hands_odds[r.hand]
    str(m) == str(g.hands_odds[r.hand])


def test_calc_duration():
    start_time = g.start_datetime
    g.calc_duration()
    end_time = g.end_datetime
    assert g.duration == end_time - start_time


def test_update_outcome():
    r.update_outcome("win")
    assert r.outcome == "win"
    r.update_outcome("lose")
    assert r.outcome == "lose"
    with pytest.raises(interfaz.UnexpectedOutcomeError) as err:
        r.update_outcome("parchita")
    assert str(err.value) == "Unexpected outcome, failed to update round data."
