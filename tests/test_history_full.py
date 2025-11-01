from app.history import History
from app.calculation import Calculation

def test_add_and_to_list_and_iter_and_clear():
    # Create history with small max size
    h = History(max_size=3)
    c1 = Calculation("add", 1, 2, 3)
    c2 = Calculation("subtract", 5, 2, 3)
    c3 = Calculation("multiply", 2, 3, 6)

    # Add calculations
    h.add(c1)
    h.add(c2)
    h.add(c3)

    # Check to_list covers that method
    lst = h.to_list()
    assert len(lst) == 3
    assert all(isinstance(x, Calculation) for x in lst)

    # __iter__ coverage
    items = list(iter(h))
    assert len(items) == 3
    assert items[0].operation == "add"

    # clear() coverage
    h.clear()
    assert len(h.to_list()) == 0

    # Ensure adding after clear still works
    h.add(c1)
    assert len(h.to_list()) == 1
