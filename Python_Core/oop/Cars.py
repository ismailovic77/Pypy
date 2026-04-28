class Cars :
    def __init__(self, brand, model):
        self.brand = brand
        print(self.brand)
        self.model = model
        print(self.model)
        self.mileage = 0

    def start(self):
        print("Vrooooom")
    
    def run(self, miles):
        self.mileage += miles
        print(f"The car ran for {miles} miles")

    def get_mileage(self):
        return self.mileage
    
    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_brand(self):
        return self.brand
    
    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model

