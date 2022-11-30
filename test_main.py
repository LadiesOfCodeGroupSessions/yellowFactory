from main import Truck

def test_create_a_new_truck():
    truck1 = Truck("Small")
    assert truck1.model == "Small"