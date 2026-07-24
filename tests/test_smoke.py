from scripts.verify_hyperbola import hyperbola, line_occupancies


def test_single_hyperbola_line_cap():
    p = 11
    pts = hyperbola(3, p)
    assert max(len(v) for v in line_occupancies(pts).values()) <= 2
