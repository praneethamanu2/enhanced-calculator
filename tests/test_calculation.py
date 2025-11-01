from app.calculation import Calculation

def test_to_dict_and_back():
    c = Calculation("add", 2, 3, 5)
    d = c.to_dict()
    c2 = Calculation.from_dict(d)
    assert c2.operation == "add"
    assert c2.result == 5
