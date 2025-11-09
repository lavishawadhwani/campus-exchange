 

# Register your models here.
from django.contrib import admin
from .models import Listing
from .models import ContactMessage
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seller_name', 'contact_info')
 
 

admin.site.register(ContactMessage)
