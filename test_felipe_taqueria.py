import pytest
from felipe_taqueria import FelipeTaqueria

@pytest.mark.parametrize("item, price", [
    ("bowl", 8.50),
    ("baja taco", 4.25),
    ("Burrito, 7.50"),
    ("Quesadilla", 8.50)
])
class TestGetPrice:
    felipe_taqueria = FelipeTaqueria()
    def test_get_price(self, item , price):
        assert self.felipe_taqueria.get_price(item) == price