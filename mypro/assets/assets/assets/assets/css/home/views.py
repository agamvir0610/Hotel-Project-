from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def booking_page(request):
    return render(request, 'booking.html')

def contact_page(request):
    return render(request, 'contact.html')

def room_page(request):
    return render(request, 'room.html')

def service_page(request):
    return render(request, 'service.html')

def team_page(request):
    return render(request, 'team.html')

def testimonial_page(request):
    return render(request, 'testimonial.html')
