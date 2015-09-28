from config.env import ENV
import pandas as pd


class Postgres:

    def __init__(self):
        self.connection = None
        uri = ENV.ENV1
        self.connection = self.connection or 'configure the here ' + uri

    def getConnection(self):
        return self.connection

    # Look for a good ORM - sqlalchemy? Depending if heavy data processing or not
    # We can use pandas to get the query results
    # Care with SQL injection here and in the models!!
    def executeQuery(self, queryString):
        query = 'execute the query %s' % queryString
        return 'QUERY: ' + query + ', CONNECTION: ' + self.connection
