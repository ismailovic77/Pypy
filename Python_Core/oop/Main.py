#import Cars as CR
from Cars import Cars

if __name__ == '__main__' :
    print("Hello this is the start of the main project")
    car = Cars('Mercedes', 'GLE')
    car.start()
    car.run(200)
    print(f"the mileage of the car in this moment {car.get_mileage()}")
    car.run(300)
    print(f"the mileage of the car in this moment {car.get_mileage()}")
    print("*****************")
    dct = dict(brand = car.get_brand(), model = car.get_model())
    print(dct)
    car.set_brand("Audi")
    car.set_model("V8")
    dct = {'brand': car.get_brand(), 'model': car.get_model()}
    print(dct)