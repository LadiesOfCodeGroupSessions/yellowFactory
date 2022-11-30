from main import Truck, Ship

def test_create_a_new_truck():
    truck1 = Truck("Small")
    assert truck1.model == "Small"

def test_create_a_new_ship():
    ship1 = Ship("Big")
    assert ship1.model == "Big"

def test_can_truck_deliver():
    truck1 = Truck("Medium")
    assert truck1.deliver()
