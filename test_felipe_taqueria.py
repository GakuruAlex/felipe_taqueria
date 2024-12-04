import pytest
from felipe_taqueria import FelipeTaqueria

@pytest.mark.parametrize("item, price", [
    ("bowl", 8.50),
    ("baja taco", 4.25),
    ("Burrito", 7.50),
    ("Quesadilla", 8.50)
])
class TestGetPrice:
    felipe_taqueria = FelipeTaqueria()
    def test_get_price(self, item , price):
        assert self.felipe_taqueria.get_price(item) == price

@pytest.mark.parametrize("price, total",[
    (8.50, 8.50),
    (4.25, 12.75),
    (7.50, 20.25),
    (8.50, 28.75)
])
class TestCalculatePrice:
    felipe_taqueria = FelipeTaqueria()
    def test_calculate_price(self, price, total):
        assert self.felipe_taqueria.calculate_total(price) == total


class TestMain:
    def test_main_with_several_items(self,monkeypatch, capsys):
        felipe_taqueria = FelipeTaqueria()
        mock_inputs = iter(["bowl", "Baja Taco", "Burrito", "Quesadilla", ""])
        monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))
        
        felipe_taqueria.main()
        
        captured = capsys.readouterr()
        
        assert captured.out == "Total: $8.50\nTotal: $12.75\nTotal: $20.25\nTotal: $28.75\n"