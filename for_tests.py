import pytest

class TestClass:
 def test_something(self):
    x = "hello"
    assert "h" in x

def f():
    raise SystemExit(1)
def test_mytest():
    with pytest.raises(SystemExit):
        f()
def test_sum():
    assert (0.1 + 0.3 ) == pytest.approx(0.4)
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)
    assert all(fruit.cubed for fruit in fruit_salad.fruit)

