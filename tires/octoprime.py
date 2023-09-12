from tires.tires import Tires


class OctoprimeTires(Tires):

    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        count = 0
        for i in self.sensors:
            count += i
        if count >= 3:
            return True
        else:
            return False
