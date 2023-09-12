from tires.tires import Tires


class CarriganTires(Tires):

    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        for i in self.sensors:
            if i >= 0.9:
                return True
        return False
