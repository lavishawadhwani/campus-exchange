# Create your views here.
from django.shortcuts import render, redirect
from .forms import ListingForm, ContactForm
from .models import Listing

# 🏠 Home View (with Search)
def home(request):
    query = request.GET.get('q')  # get search term
    listings = Listing.objects.all()  # show all by default

    if query:
        listings = listings.filter(title__icontains=query) | listings.filter(description__icontains=query)

    context = {'listings': listings}
    return render(request, 'market/home.html', context)


# 📂 Categories Page
def categories(request):
    return render(request, 'market/categories.html')


# ➕ Add Listing
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListingForm()
    return render(request, 'market/add_listing.html', {'form': form})


# 📞 Contact Page (simple version)
def contact(request):
    return render(request, 'market/contact.html')


# 📧 Contact Form (with success page)
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'market/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'market/contact.html', {'form': form})
