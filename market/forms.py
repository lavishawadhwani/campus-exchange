 
from django import forms
from .models import Listing
from .models import ContactMessage
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'seller_name', 'contact_info', 'image']
 

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
