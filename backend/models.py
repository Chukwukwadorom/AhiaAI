from django.db import models
import json

# Demographics Table
class Demographics(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ('NO_EDUCATION', 'No Formal Education'),
        ('PRIMARY', 'Primary Education'),
        ('SECONDARY', 'Secondary Education'),
        ('COLLEGE', 'College'),
        ('POSTGRAD', 'Postgraduate'),
    ]

    location_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    median_income = models.FloatField()
    population_density = models.FloatField()
    education_level =  models.CharField(
        max_length=15,
        choices=EDUCATION_LEVEL_CHOICES,
        default='SECONDARY',
        help_text="Dominant education level in the demographic."
    )
    employment_rate = models.FloatField()
    urban_rural = models.CharField(max_length=50, choices=[('Urban', 'Urban'), ('Rural', 'Rural')])
    # ethnicity_distribution = models.JSONField()  # Store ethnicities as a JSON object

    def __str__(self):
        return f"{self.location_name} Demographics"

# Retailers Table
class Retailer(models.Model):
    name = models.CharField(max_length=255)
    demographics = models.ForeignKey(Demographics, on_delete=models.CASCADE, related_name="retailers")
    
    def __str__(self):
        return f"{self.name} - {self.demographics.location_name}"

# Products Table
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

# Sales Table
class Sale(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name="sales")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.retailer.name} - {self.product.name} ({self.quantity})"

# Cluster Table (Feature Store)
# class RetailerCluster(models.Model):
#     retailer = models.OneToOneField(Retailer, on_delete=models.CASCADE, related_name="cluster")
#     cluster_label = models.IntegerField()

#     def __str__(self):
#         return f"Retailer: {self.retailer.name} - Cluster: {self.cluster_label}"
