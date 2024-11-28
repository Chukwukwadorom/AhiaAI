from faker import Faker
from backend.models import Demographics, Retailer, Product, Sale

class ahia_faker():
    def __init__ (self):
        pass    
       
    def dem_faker (self,
                location_name:str,
                latitude:float,
                longitude:float,
                median_income:float,
                population_density:float,
                education_level:str,
                employment_rate:float,
                urban_rural:str):
        
        self.location_name = location_name
        self.latitude = latitude
        self.longitude = longitude
        self.median_income: median_income
        self.population_density = population_density,
        self.education_level = education_level
        self.employment_rate = employment_rate
        self.urban_rural = urban_rural       



    
    def retail_faker (self):
        pass

    def product_faker (self):
        pass

    def sale_faker (self):
        pass






# location_name = models.CharField(max_length=255)
# latitude = models.FloatField()
# longitude = models.FloatField()
# median_income = models.FloatField()
# population_density = models.FloatField()
# education_level = models.FloatField()
# employment_rate = models.FloatField()