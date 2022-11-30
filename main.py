class TransportInterface:

    def deliver(self):
        return True


class Truck(TransportInterface):

    def __init__(self, model):
        self.model = model


class Ship:

    def __init__(self, model):
        self.model = model
