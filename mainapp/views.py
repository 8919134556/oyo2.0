from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
# Create your views here.
from django.shortcuts import render
from hotelapp.models import HotelModel
from userapp.models import UserModel
from travelapp.models import TravelModel
from travelapp.models import CardashboardModel
from travelapp.models import CruisesdashboardModel
from travelapp.models import FlightdashboardModel
from userapp.models import RoomBooking
from userapp.models import CarBooking
from userapp.models import FlightBooking
# from userapp.models import Feedback
from userapp.models import CruisesBooking
from django.core.mail import EmailMessage
from django.db.models import Q







# Create your views here.

def index (request):
    hotel=HotelModel.objects.all()
    
    print('get')
    if request.method=="POST":
        search = request.POST.get("home_search")
        print(search)
        hotel = HotelModel.objects.filter(Q(hotel_name__icontains=search))
    return render(request, "./main/index.html", {'view' : hotel})




def admin(request):
    if request.method == "POST":
        admin_email = request.POST.get('admin_email')
        admin_pws = request.POST.get ('admin_pws')
        if admin_email =='admin' and admin_pws =='admin':
            messages.success(request, "Welcome")
            return redirect('admin_dashboard')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('admin')
    return render(request, "./admin/admin.html")


def hotel(request):
    hotel=HotelModel.objects.all()
    print('get')
    if request.method=="POST":
        search = request.POST.get("hotel_search")
        print(search)
        hotel = HotelModel.objects.filter(Q(hotel_name__icontains=search))
    
    return render(request, "./hotel/hotel.html", {'view' : hotel})
def hotel_owners(request):
    return render(request, "./hotel/hotel-owners.html")



def car(request):
    agency=TravelModel.objects.all()
    print('get')
    if request.method=="POST":
        search = request.POST.get("agency_search")
        print(search)
        agency = TravelModel.objects.filter(Q(agency_name__icontains=search))
    return render(request, "./travel/cars.html", {'view' : agency})

def flight(request):
    return render(request, "./travel/flights.html")
def main_cruises (request):
    return render(request, "./travel/cruises.html")
def travel_agencies(request):
    return render(request, "./travel/travel-agency.html")

    
    




def admin_dashboard(request):
    hotel=HotelModel.objects.all()
    feedback=Feedback.objects.all()
    user=UserModel.objects.all()
    agency=TravelModel.objects.all()
    cars=CardashboardModel.objects.all()
    flights = FlightdashboardModel.objects.all()
    crui = CruisesdashboardModel.objects.all()
    booking = RoomBooking.objects.all()
    car_booking = CarBooking.objects.all()
    flight_booking = FlightBooking.objects.all()
    cruises_booking = CruisesBooking.objects.all()

    user_count = user.count()
    feedback_count = feedback.count()
    cars_count = cars.count()
    agency_count = agency.count()
    hotel_count = hotel.count()
    flights_count = flights.count()
    crui_count = crui.count()
    booking_count = booking.count()
    car_booking_count = car_booking.count()
    flight_booking_count = flight_booking.count()
    cruises_booking_count = cruises_booking.count()

    context = {
        'hotel_count' : hotel_count,
        'agency_count' : agency_count,
        'cars_count' : cars_count,
        'flights_count' : flights_count,
        'crui_count' : crui_count,
        'user_count' : user_count,
        'booking_count' : booking_count,
        'car_booking_count' : car_booking_count,
        'flight_booking_count' : flight_booking_count,
        'cruises_booking_count' : cruises_booking_count,
        'feedback_count' : feedback_count
    }
    return render(request, "./dashboard/admin/index.html", context)


def hotel_corporate(request):
    hotel=HotelModel.objects.all()
    return render(request, "./dashboard/admin/hotel-corporate.html", {'view': hotel})

def car_rental(request):
    cars=CardashboardModel.objects.all()
    return render(request, "./dashboard/admin/car-rental.html", {'view' : cars})

def admin_feedback(request):
    feedback = Feedback.objects.all()
    user = UserModel.objects.all()
    mylist = zip(feedback, user)
    return render(request, "./dashboard/admin/feedback.html", {'view' : mylist})

def flight_dashboard(request):
    flights = FlightdashboardModel.objects.all()
    return render(request, "./dashboard/admin/flight.html", {'view' : flights})

def cruises_dashboard(request):
    crui = CruisesdashboardModel.objects.all()
    return render(request, "./dashboard/admin/cruises.html", {'view' : crui})

def admin_profile(request):
    return render(request, "./dashboard/admin/profile.html")




def travel_agency(request):
    agency=TravelModel.objects.all()
    
    
    return render(request, "./dashboard/admin/travel-agency.html", {'view' : agency})



def accept_agency(request, id) : 
    accept = get_object_or_404(TravelModel, agency_id=id)
    accept.status = 'Accepted'
    accept.save(update_fields = ['status'])
    accept.save()
    ac = accept.agency_email
    acc = accept.agency_pwd
    email = EmailMessage('Subject',f'Hello {ac}, your account is activated\nhere your details\n username : {ac} \n Password : {acc}', to=[ ac ])
    email.send()
    return redirect("travel_agency")

def reject_agency(request, id) : 
    reject = get_object_or_404(TravelModel, agency_id=id)
    reject.status = 'Rejected'
    reject.save(update_fields = ['status'])
    reject.save()
    re = reject.agency_email
    
    email = EmailMessage('Subject',f'Hello {re}, your account is rejected pls rejecter again', to=[ re ])
    email.send()
    return redirect("travel_agency")

def accept_corporate(request, id) : 
    accept = get_object_or_404(HotelModel, hotel_id=id)
    accept.status = 'Accepted'
    accept.save(update_fields = ['status'])
    accept.save()
    ac = accept.hotel_email
    acc = accept.hotel_pwd
    email = EmailMessage('Subject',f'Hello {ac}, your account is activated\nhere your details\n username : {ac} \n Password : {acc}', to=[ ac ])
    email.send()
    return redirect("hotel_corporate")

def reject_corporate(request, id) : 
    reject = get_object_or_404(HotelModel, hotel_id=id)
    reject.status = 'Rejected'
    reject.save(update_fields = ['status'])
    reject.save()
    re = reject.hotel_email
    
    email = EmailMessage('Subject',f'Hello {re}, your account is rejected pls rejecter again', to=[ re ])
    email.send()
    return redirect("hotel_corporate")