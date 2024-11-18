from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    our_services = ["Bush camps", "Ballon Tours", "firecamps", "color festivals"]
    price = 10000
    date = '15-11-2024'
    return render(request, 'services.html', {"services": our_services, "price":price, "date":date})    


#dislpay data in our pages
#loops
#if statements
#Templating engine language
