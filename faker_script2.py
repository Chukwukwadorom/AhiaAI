from faker import Faker
import random
from backend.models import Demographics, Retailer, Product, Sale

class AhiaFaker:
    def __init__(self):
        self.fake = Faker()

    def dem_faker(self):
        demographics = Demographics.objects.create(
            location_name=self.fake.city(),
            latitude=random.uniform(-90, 90),
            longitude=random.uniform(-180, 180),
            median_income=random.uniform(15000, 100000),
            population_density=random.uniform(100, 1000),
            education_level=random.choice(['NO_EDUCATION', 'PRIMARY', 'SECONDARY', 'COLLEGE', 'POSTGRAD']),
            employment_rate=random.uniform(50, 100),
            urban_rural=random.choice(['Urban', 'Rural']),
        )
        return demographics

    def retail_faker(self):
        demographics = random.choice(Demographics.objects.all())  # Link to an existing demographic
        retailer = Retailer.objects.create(
            name=self.fake.company(),
            demographics=demographics,
        )
        return retailer

    def product_faker(self):
        product = Product.objects.create(
            name=self.fake.word().capitalize(),
            description=self.fake.sentence(),
            price=random.uniform(10, 1000),
        )
        return product

    def sale_faker(self):
        retailers = Retailer.objects.all()
        products = Product.objects.all()
        if not retailers.exists() or not products.exists():
            print("Populate Retailer and Product tables first!")
            return None
        
        sale = Sale.objects.create(
            retailer=random.choice(retailers),
            product=random.choice(products),
            quantity=random.randint(1, 50),
            sale_date=self.fake.date_time_this_year(),
        )
        return sale

# Usage
ahia = AhiaFaker()

# Generate data
for _ in range(10):  # Generate 10 demographics
    ahia.dem_faker()

for _ in range(50):  # Generate 50 retailers
    ahia.retail_faker()

for _ in range(100):  # Generate 100 products
    ahia.product_faker()

for _ in range(200):  # Generate 200 sales
    ahia.sale_faker()
