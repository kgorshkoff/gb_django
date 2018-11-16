from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'index.html')

def catalog(request):
    return render(request, 'catalog.html')

def contacts(request):
    return render(request, 'contacts.html')