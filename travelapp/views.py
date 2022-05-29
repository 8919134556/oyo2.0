from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
# Create your views here.
from django.shortcuts import render
from .models import TravelModel
from .models import CardashboardModel
from .models import FlightdashboardModel
from .models import CruisesdashboardModel
from userapp.models import CarBooking
from mainapp.models import UserFeedback
from userapp.models import UserModel
from userapp.models import FlightBooking
from userapp.models import CruisesBooking
import re


def travel_registration(request):
    if request.method == "POST" and request.FILES["agency_photo"] and request.FILES["iata_certificate"]:
        agency_name = request.POST['agency_name']
        pannumber = request.POST['pannumber']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        agency_photo = request.FILES ["agency_photo"]
        iata_certificate = request.FILES ["iata_certificate"]
        
        if len(agency_name) > 20:
            
            messages.error (request, "user name must be 10 characters")
        elif not agency_name.isalpha():
            messages.error (request, "username should only contain letters")

        

        elif re.search('[A-Z]{4}[0-9]{4}[A-Z]{1}', pannumber) is None :
            messages.error(request, "plase enter vailed pannumber")
        
        


        elif TravelModel.objects.filter(agency_email=email).exists():
            messages.error (request, "Email alredy exist")
            return redirect("travel_registration")
        else:
            travel_registration = TravelModel.objects.create(agency_name=agency_name,agency_pan_number=pannumber,agency_addres=address,agency_phone=phone,agency_email=email,agency_pwd=password,agency_photo=agency_photo,iata_certificate=iata_certificate)
            travel_registration.save()
            messages.success(request, "your account has been successfully created")
            return redirect("travel_agencies")
    return render(request, "travel/agency-registration.html")

def travel_agencies(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            login = TravelModel.objects.get(agency_email=email,agency_pwd=password)
            request.session["agency_id"]=login.agency_id
            status = login.status
            # print("agency_id", login.agency_id)
            if status == "Accepted":
                print('ok')
                request.session['email'] = login.agency_email
                return redirect ("travel_index")
                print("hallo")
            else : 
                messages.success(request, "your account not at activated")
        except:
            messages.error(request, "bad credential Please Register")
            return redirect("travel_registration")
    return render(request, "travel/travel-agency.html")






def travel_index(request):
    cars = CardashboardModel.objects.all()
    flights = FlightdashboardModel.objects.all()
    cruises = CruisesdashboardModel.objects.all()
    car_booking = CarBooking.objects.all()
    flight_booking = FlightBooking.objects.all()
    cruises_booking = CruisesBooking.objects.all()

    cars_count = cars.count()
    flights_count = flights.count()
    cruises_count= cruises.count()
    car_booking_count = car_booking.count()
    flight_booking_count = flight_booking.count()
    cruises_booking_count = cruises_booking.count()
    context = {
        'cars_count' : cars_count,
        'flights_count' : flights_count, 
        'cruises_count' : cruises_count,
        'car_booking_count' : car_booking_count,
        'flight_booking_count' : flight_booking_count,
        'cruises_booking_count' : cruises_booking_count
        
 
    }
   
    return render(request, "dashboard/travel-agency/travel-index.html", context)


def cars(request):
    agency_id=request.session["agency_id"]
    if request.method == "POST" and request.FILES["car_photo"] :
        car_type = request.POST['car_type']
        car_model = request.POST['car_model']
        car_no = request.POST['car_no']
        select_car = request.POST['select_car']
        price = request.POST['price']
        car_photo = request.FILES ["car_photo"]

        cars = CardashboardModel.objects.create(agency_id=agency_id,car_type=car_type,car_model=car_model,car_no=car_no,select_car=select_car,price=price,car_photo=car_photo)
        messages.success(request, "successfully added")
        return redirect('view_cars')
    return render(request, "dashboard/travel-agency/cars.html")

def travel_flight(request):
    agency_id=request.session["agency_id"]
    if request.method == "POST" and request.FILES["flight_photo"] :
        flight_name = request.POST['flight_name']
        flight_no = request.POST['flight_no']
        select_class = request.POST['select_class']
        flight_from = request.POST['flight_from']
        to = request.POST['to']
        via = request.POST['via']
        date = request.POST['date']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        price = request.POST['price']
        flight_photo = request.FILES ["flight_photo"]

        flights = FlightdashboardModel.objects.create(agency_id=agency_id,flight_name=flight_name,flight_no=flight_no,select_class=select_class,flight_from=flight_from,to=to,via=via,date=date, check_in=check_in,check_out=check_out,price=price,flight_photo=flight_photo )
        messages.success(request, "successfully added")
        return redirect('view_flights')


    return render (request, "dashboard/travel-agency/flights.html")

def cruises(request):
    agency_id=request.session["agency_id"]
    if request.method == "POST" and request.FILES["cruises_photo"] :
        cruises_name = request.POST['cruises_name']
        cruises_no = request.POST['cruises_no']
        select_class = request.POST['select_class']
        cruises_from = request.POST['cruises_from']
        to = request.POST['to']
        via = request.POST['via']
        date = request.POST['date']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        price = request.POST['price']
        cruises_photo = request.FILES ["cruises_photo"]

        crui = CruisesdashboardModel.objects.create(agency_id=agency_id,cruises_name=cruises_name,cruises_no=cruises_no,select_class=select_class,cruises_from=cruises_from,to=to,via=via,date=date, check_in=check_in,check_out=check_out,price=price,cruises_photo=cruises_photo )
        messages.success(request, "successfully added")
        return redirect('view_cruises')
    return render(request, "dashboard/travel-agency/cruises.html")


def view_cruises(request):
    demo = request.session["agency_id"]
    crui = CruisesdashboardModel.objects.filter(agency_id=demo)
    return render (request, "dashboard/travel-agency/view-cruises.html", {'view': crui})

def edit_cruises(request):
    demo = request.session["agency_id"]
    crui = CruisesdashboardModel.objects.filter(agency_id = demo)
    return render (request, "dashboard/travel-agency/edit-cruises.html", {'view': crui})



def view_flights(request):
    demo = request.session["agency_id"]
    flights = FlightdashboardModel.objects.filter(agency_id=demo)
    return render (request, "dashboard/travel-agency/view-flights.html", {'view' : flights})

def edit_flight(request):
    demo = request.session["agency_id"]
    flights = FlightdashboardModel.objects.filter(agency_id=demo)
    return render (request, "dashboard/travel-agency/edit-flight.html", {'view' : flights})

def deleflight(request, id):
    flights = FlightdashboardModel.objects.get(flight_id=id)
    flights.delete()
    return redirect('edit_flight')




def updatecar(request, id):    
    cars = CardashboardModel.objects.get(car_id=id)
    print('hello')
    if request.method == "POST":
        car_type = request.POST.get('car_type')
        car_model = request.POST.get('car_model')
        car_no = request.POST.get('car_no')
        select_car = request.POST.get('select_car')
        price = request.POST.get('price')
   
        cars = get_object_or_404(CardashboardModel, car_id= id)
        cars.car_type = car_type
        cars.car_model = car_model
        cars.car_no = car_no
        cars.select_car = select_car
        cars.price = price
        
        
        if request.FILES["car_photo"] != None:
            car_photo = request.FILES.get("car_photo")
            cars.car_photo = car_photo
        
        cars.save(update_fields=["car_type","car_model","car_no","select_car","price","car_photo" ])
        cars.save()
        return redirect("view_cars")

    return render(request, 'dashboard/travel-agency/edit-car-form.html', {'ca' : cars})


def updatecruises(request, id):    
    crui = CruisesdashboardModel.objects.get(cruises_id=id)
    
    if request.method == "POST":
        cruises_name = request.POST.get('cruises_name')
        cruises_no = request.POST.get('cruises_no')
        select_class = request.POST.get('select_class')
        cruises_from = request.POST.get('cruises_from')
        to = request.POST.get('to')
        via = request.POST.get('via')
        date = request.POST.get('date')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        price = request.POST.get('price')
        

   
        crui = get_object_or_404(CruisesdashboardModel, cruises_id= id)
        crui.cruises_name = cruises_name
        crui.cruises_no = cruises_no
        crui.select_class = select_class
        crui.cruises_from = cruises_from
        crui.to = to
        crui.via = via
        crui.date = date
        crui.check_in = check_in
        crui.check_out = check_out
        crui.price = price
        
        
        if request.FILES["cruises_photo"] != None:
            cruises_photo = request.FILES.get("cruises_photo")
            crui.cruises_photo = cruises_photo
        
        crui.save(update_fields=["cruises_name","cruises_no","select_class","cruises_from","to","via","date","check_in","check_out","price", "cruises_photo"])
        crui.save()
        return redirect("view_cruises")

    return render(request, 'dashboard/travel-agency/edit-cruises-form.html', {'cr' : crui})

def delecruises(request, id):
    crui = CruisesdashboardModel.objects.get(cruises_id=id)
    crui.delete()
    return redirect('edit_cruises')




def updateflight(request, id):    
    flights = FlightdashboardModel.objects.get(flight_id=id)
    print('hello')
    if request.method == "POST":
        flight_name = request.POST.get('flight_name')
        flight_no = request.POST.get('flight_no')
        select_class = request.POST.get('select_class')
        flight_from = request.POST.get('flight_from')
        to = request.POST.get('to')
        via = request.POST.get('via')
        date = request.POST.get('date')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        price = request.POST.get('price')
        

   
        flights = get_object_or_404(FlightdashboardModel, flights_id= id)
        flights.flight_name = flight_name
        flights.flight_no = flight_no
        flights.select_class = select_class
        flights.flight_from = flight_from
        flights.to = to
        flights.via = via
        flights.date = date
        flights.check_in = check_in
        flights.check_out = check_out
        flights.price = price
        
        
        if request.FILES["flight_photo"] != None:
            flight_photo = request.FILES.get("flight_photo")
            flights.flight_photo = flight_photo
        
        flights.save(update_fields=["flight_name","flight_no","select_class","flight_from","to","via","date","check_in","check_out","price"])
        flights.save()
        return redirect("view_flight")

    return render(request, 'dashboard/travel-agency/edit-flight-form.html', {'fi' : flights})



def edit_cruises_form(request):
    crui = CruisesdashboardModel.objects.get(cruises_id=id)
    if request.method == "POST" and request.FILES.get("cruises_photo") :
        cruises_name = request.POST.get('cruises_name')
        cruises_no = request.POST.get('cruises_no')
        select_class = request.POST.get('select_class')
        cruises_from = request.POST.get('cruises_from')
        to = request.POST.get('to')
        via = request.POST.get('via')
        date = request.POST.get('date')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        price = request.POST.get('price')
        cruises_photo = request.FILES .get("cruises_photo")

        crui = get_object_or_404(CruisesdashboardModel, cruises_id= id)
        crui.cruises_name = cruises_name
        curi.cruises_no = cruises_no
        crui.select_class
        crui.cruises_from
        crui.to = to
        crui.via = via
        crui.date = date
        crui.check_in = check_in
        crui.check_out = check_out
        crui.price = price
        crui.cruises_photo = cruises_photo
        crui.save(update_fields=["cruises_name","cruises_no","select_class","cruises_from",
        "to","via","date","check_in","check_out","price","cruises_photo" ])
        messages.success(request,'Updated Successfully')
        return redirect("view_cruises")
    return render (request, "dashboard/travel-agency/edit-cruises-form.html")


def edit_flight_form(request):
    flights = FlightdashboardModel.objects.get(flight_id=id)
    if request.method == "POST" and request.FILES.get("flight_photo") :
        flight_name = request.POST.get('flight_name')
        flight_no = request.POST.get('flight_no')
        select_class = request.POST.get('select_class')
        flight_from = request.POST.get('flight_from')
        to = request.POST.get('to')
        via = request.POST.get('via')
        date = request.POST.get('date')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        price = request.POST.get('price')
        flight_photo = request.FILES .get("flight_photo")

        flights = get_object_or_404(FlightdashboardModel, flight_id= id)
        flights.flight_name = flight_name
        flights.flight_no = flight_no
        flights.select_class
        flights.flight_from
        flights.to = to
        flights.via = via
        flights.date = date
        flights.check_in = check_in
        flights.check_out = check_out
        flights.price = price
        flights.flight_photo = flight_photo
        flights.save(update_fields=["flight_name","flight_no","select_class","flight_from",
        "to","via","date","check_in","check_out","price","flight_photo" ])
        messages.success(request,'Updated Successfully')
        return redirect("view_flight")
    
    return render (request, "dashboard/travel-agency/edit-flight-form.html")









def edit_car_form(request, id):
    cars = CardashboardModel.objects.get(car_id=id)
    if request.method == "POST" and request.FILES.get("car_photo") :
        car_type = request.POST.get('car_type')
        car_model = request.POST.get('car_model')
        car_no = request.POST.get('car_no')
        select_car = request.POST.get('select_car')
        price = request.POST.get('price')
        
        car_photo = request.FILES .get("car_photo")

        cars = get_object_or_404(CardashboardModel, car_id= id)
       
        cars.car_type = car_type
        cars.car_model = car_model
        cars.car_no = car_no
        cars.select_car = select_car
        cars.price = price
        
        cars.car_photo = car_type
        
        cars.save(update_fields=["car_type","car_model","car_no","select_car","price","car_photo" ])
        messages.success(request,'Updated Successfully')
        return redirect("view_cars")
    return render(request, "dashboard/travel-agency/edit-car-form.html")





def delecar(request, id):
    cars = CardashboardModel.objects.get(car_id=id)
    cars.delete()
    return redirect('edit_cars')








def edit_cars(request):
    demo = request.session["agency_id"]
    cars = CardashboardModel.objects.filter(agency_id=demo) 
    return render (request, "dashboard/travel-agency/edit-car.html", {'view' : cars})



def edit_details(request):
    return render (request, "dashboard/travel-agency/edit-details.html")

def view_details(request):
    return render (request, "dashboard/travel-agency/view-details.html")

def view_booking_details(request):
    return render (request, "dashboard/travel-agency/view-booking-details.html")

def view_cars(request):
    demo = request.session["agency_id"]
    cars = CardashboardModel.objects.filter(agency_id=demo) 
    return render (request, "dashboard/travel-agency/view-cars.html", {'view' : cars})

def car_booking_details(request):
    data = request.session["agency_id"]
    obj = CarBooking.objects.filter(agency_id = data)
    return render (request, "dashboard/travel-agency/car-booking-details.html", {'view' : obj})

def flight_booking_details(request):
    data = request.session["agency_id"]
    obj = FlightBooking.objects.filter(agency_id = data)
    return render (request, "dashboard/travel-agency/flight-booking-details.html", {'view' : obj})

def cruises_booking_details(request):
    data = request.session["agency_id"]
    obj = CruisesBooking.objects.filter(agency_id = data)
    return render (request, "dashboard/travel-agency/cruises-booking-details.html", {'view' : obj})



def feedback(request):
    travel = request.session["agency_id"]
    demo = UserFeedback.objects.filter(agency_id=travel)
    

    return render (request, "dashboard/travel-agency/feedback.html", {'view' : demo})
    
def profile(request):
    email = request.session["agency_id"]
    data = TravelModel.objects.get(agency_id=email)
    context = {'obj': data }
    return render (request, "dashboard/travel-agency/profile.html", context=context)