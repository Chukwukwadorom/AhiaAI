from faker import Faker
import requests
import random
# from backend.models import Demographics, Retailer, Product, Sale

host = "http://localhost:8000/"

class AhiaFaker:
    def __init__(self):
        self.fake = Faker()

    def dem_faker(self):

        self.demographic_data = {
            "location_name": self.fake.city(),
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180),
            "median_income": random.uniform(15000, 100000),
            "population_density": random.uniform(100, 1000),
            "education_level": random.choice(['NO_EDUCATION', 'PRIMARY', 'SECONDARY', 'COLLEGE', 'POSTGRAD']),
            "employment_rate": random.uniform(50, 100),
            "urban_rural": random.choice(['Urban', 'Rural']),
        }
        url = f"{host}/save-demographics/"
        response = requests.post(url, json=[self.demographic_data])

        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())

    
    def retail_faker(self):
        url_dem  = f"{host}/demographics/"
        url_ret = f"{host}/save-retailers/"
        
        response = requests.get(url_dem)
        
        if response.status_code != 200:
            raise ValueError("Failed to fetch demographics from the API.")

        print("Status Code:", response.status_code)
        demographs = response.json()
       
        chosen_demographic = random.choice(demographs)  
        self.retailer = {
            "name":self.fake.company(),
            "demographics":chosen_demographic["id"]
        }

        response = requests.post(url_ret, json=[self.retailer])

        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
        

    def product_faker(self):
        url_prod = f"{host}/save-products/"

        product = {
            "name" :self.fake.word().capitalize(),
            "description":self.fake.sentence(),
            "price":random.uniform(10, 1000),
        }
        response = requests.post(url=url_prod, json=[product])
        
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())

    def sale_faker(self):
        url_retailers  = f"{host}/retailers/"
        url_products  = f"{host}/products/"
        url_sales = f"{host}/sales/"

        response_retailer = requests.get(url_retailers)
        response_products = requests.get(url_products)
        
        response_products.raise_for_status()
        response_retailer.raise_for_status()

        retailers = response_retailer.json()
        products = response_products.json()

        if len(retailers) < 1 or len(products) < 1:
            print("Populate Retailer and Product tables first!")
            return None
        
        sale = {
            "retailer":random.choice(retailers),
            "product":random.choice(products),
            "quantity":random.randint(1, 50),
            "sale_date":self.fake.date_time_this_year(),
        }
       
        response = requests.post(url=url_sales, json= [sale])
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())




if __name__ == "__main__":
    ahia = AhiaFaker()
    
    # for _ in range(10):  # Generate 10 demographics
    #     ahia.dem_faker()

    # for _ in range(50):  # Generate 50 retailers
    #     ahia.retail_faker()

    # for _ in range(100):  # Generate 100 products
    #     ahia.product_faker()

    # for _ in range(200):  # Generate 200 sales
    #     ahia.sale_faker()
