class car:
    name = None
    model = None
    make = None

    def __init__(self, o_name, o_model, o_make):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


petty = car("Maruti", "800", "2024")
petty.start_engine()

orry = car("XUV", "152", "2024")
orry.start_engine()
