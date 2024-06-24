from django.shortcuts import render, redirect
from .models import Chambre, Catalogue, Testimonial, ReservationForm, Reservation


def index(request):
    chambres = Chambre.objects.all()
    catalogues = Catalogue.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "chambres": chambres,
        "catalogues": catalogues,
        "testimonials": testimonials,
    }
    return render(request, "index.html", context)


# Ensure this import is correct based on your project structure


def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect("reservation_confirmation")
        else:
            print("Formulario inválido")
            print(form.errors)
    else:
        form = ReservationForm()
    return render(request, "reservation.html", {"form": form})

def reservation_confirmation(request):
    return render(request, "reservation_confirmation.html")

def check_availability(request):
    if request.method == "POST":
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')

        # Aquí se puede agregar lógica adicional para filtrar las habitaciones
        # según las fechas y la disponibilidad.

        available_rooms = Chambre.objects.filter(disponibilité=True)

        context = {
            'available_rooms': available_rooms,
            'checkin_date': checkin_date,
            'checkout_date': checkout_date,
            'adults': adults,
            'children': children,
        }
        
        return render(request, 'available_rooms.html', context)
    return render(request, 'index.html')

def contact(request):
    return render(request, "contact.html")


def blog(request):
    chambres = Chambre.objects.all()
    return render(request, "blog.html", {"chambres": chambres})


def about(request):
    return render(request, "about.html")

