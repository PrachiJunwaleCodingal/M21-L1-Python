#class vehicles

class Vehicle:
    def __init__(self, speed, model):
        self.speed = speed  #self will bind the arguments
        self.model = model

obj= Vehicle(200,"x3 model")
print("Vehicle model:",obj.model)
print("Vehicle speed:",obj.speed)