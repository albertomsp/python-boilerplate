from src.db.Postgres import Postgres


class Car(object):

    """docstring for Car"""

    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer
        self.postgresConnection = Postgres()

    def getSimilarTypes(self):
        similar_types = self.postgresConnection.executeQuery(
            'SELECT * FROM cars WHERE manufacturer = %s' % self.manufacturer)
        res = similar_types  # processing
        return res
