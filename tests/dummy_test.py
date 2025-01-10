from src.ultimate_tic_tac_toe.dummy import Dummy


def test_dummy() -> None:
    d = Dummy()
    assert d.x == 4