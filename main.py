from config.env import ENV
from src.db.Postgres import Postgres
from src.models.Car import Car

print ENV.ENV1

car = Car('MyModel', 'MyManufacturer')
print car.getSimilarTypes()
