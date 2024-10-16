class CarManager:
    all_cars = {}
    total_cars = 0
    
    
    def __init__(self, make, model, year, mileage):
        self._make = make.capitalize()
        self._model = model.capitalize()
        self._year = year
        self._mileage = mileage
        self._services = []
        
        
        @property
        def make(self):
            return self._make
        
        @property
        def model(self):
            return self._model
        
        @property
        def year(self):
            return self._year
        
        @property
        def mileage(self):
            return self._mileage
        
        @property
        def id(self):
            return self._id
        
        @property
        def services(self):
            return self._services
        
        # Incrementing total_cars by 1 every time
        CarManager.total_cars += 1
        
        # Setting ID equal to total_cars so that it increments along with total_cars
        self._id = CarManager.total_cars
        
        # Adding each instance of CarManager to all_cars every time CarManager is called
        CarManager.all_cars[f"Car {CarManager.total_cars}"] = self
        
        def add_service(self, service):
            self._services.append(service)
        
        def add_service(self):
            service = input("Enter the service performed: ")  # Prompt user for the service
            self._services.append(service)
        
        
        
    def __repr__(self):
        return f"Make: {self._make} | Model: {self._model} | Year: {self._year} | Mileage: {self._mileage} | ID: {self._id}"
        
    
    

        
   