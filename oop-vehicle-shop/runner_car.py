from car_management import CarManager


def get_car_details():
    # Collect car details from the user
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    year = int(input("Enter the car year: "))
    mileage = int(input("Enter the car mileage: "))
    
    return make, model, year, mileage

if __name__ == "__main__":
    make, model, year, mileage = get_car_details()
    
    car = CarManager(make, model, year, mileage)

print(CarManager.all_cars)
