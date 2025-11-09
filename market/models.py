from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    seller_name = models.CharField(max_length=100, null=True, blank=True)
    contact_info = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='listing_images/', null=True, blank=True)

    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
 
 


 