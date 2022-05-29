from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
# Create your views here.
from django.shortcuts import render
from .models import UserModel
from mainapp.models import UserFeedback


from hotelapp.models import HoteldashboardModel
from hotelapp.models import HotelModel
from travelapp.models import TravelModel
from travelapp.models import CardashboardModel
from travelapp.models import FlightdashboardModel
from travelapp.models import CruisesdashboardModel
from .models import RoomBooking
from .models import CarBooking
from .models import FlightBooking
from .models import CruisesBooking
import re

from django.core.mail import EmailMessage





def customer_registration(request):
    if request.method == "POST" and request.FILES["user_photo"]:
        user_name = request.POST['user_name']
        user_lastname = request.POST['user_lastname']
        user_phone = request.POST['user_phone']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_photo = request.FILES ["user_photo"]
        
        if len(user_name) > 20:
            
            messages.error (request, "user name must be 10 characters")
        elif not user_name.isalpha():
            messages.error (request, "username should only contain letters")

        elif len(user_password) < 8:
            messages.error (request, "Make sure your password is atleast 8 letters")
        elif re.search('[0-9]', user_password) is None:
            messages.error  (request, "Make sure your password has a number in it")
        elif re.search('[A-Z]', user_password) is None:
            messages.error(request, "Make sure your password has a capital letter in it")
        

        elif UserModel.objects.filter(user_email=user_email).exists():
            messages.error (request, "Email alredy exist")
        
            return redirect("customer_registration")
        
        else:
    
            customer_registration = UserModel.objects.create(user_name=user_name,user_lastname=user_lastname,user_phone=user_phone,user_email=user_email,user_pwd=user_password,user_photo=user_photo )
            customer_registration.save()
            messages.success(request, "your account has been successfully created")
            return redirect("customer")
    return render(request, "user/custmor-register.html")





def customer(request):
    if request.method == "POST":

        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        try:
            login_user = UserModel.objects.get(user_email=user_email,user_pwd=user_password)
            request.session["user_email"]=login_user.user_email
            return redirect("room")
        except:
            messages.error(request, "bad credential Please Register")
            return redirect("customer_registration")
    return render(request, "user/customer.html")



def user_profile(request):
    user_email = request.session["user_email"]
    data = UserModel.objects.get(user_email=user_email)
    context = {'obj': data }        
    return render (request, "./user/profile.html", context=context)

def my_booking(request):
    email =  request.session["user_email"]
    
    data = RoomBooking.objects.filter(email=email)
    
    car_data = CarBooking.objects.filter(email=email)

    
    flight_data = FlightBooking.objects.filter(email=email)
    
    cruises_data = CruisesBooking.objects.filter(email=email)
    
    
        
    print(data.query)
    context = {
        'obj' :  data,
        'car' : car_data,
        'flight' : flight_data,
        'cruises' : cruises_data

    }
    
    return render (request, "./user/my-booking.html", context=context)





def password_reset(request):
    if request.method == "POST":
        gmail = request.POST['gmail']
        dict = gmail
        email = EmailMessage('Subject', 'http://127.0.0.1:8000/userapp/password_reset_confirm', to=[ dict ])
        email.send()
        return redirect ('password_reset/done/')
    return render (request, "./resetpws/password-reset.html") 












def password_reset_confirm(request):
    
    if request.method == "POST":
        user_email = request.POST.get('user_email')
        user_pwd = request.POST.get('user_pwd')

        user = get_object_or_404(UserModel, user_email = user_email)
        user.user_pwd = user_pwd
        user.save(update_fields=["user_pwd","user_email"])
        user.save()
        messages.success(request, "your password has been successfully changed")
        return redirect("customer")
        
    
    return render (request, "./resetpws/password-reset-confirm.html")


def base (request):
    return render (request, "./resetpws/base.html")








def room(request):
    
    hotel = HotelModel.objects.all()    
    rooms = HoteldashboardModel.objects.all() 
    mylist = zip(rooms, hotel)
   
    return render (request, "./hotel/rooms.html", {'view' : mylist})

def user_car_rental(request):
    travel = TravelModel.objects.all() 
    cars = CardashboardModel.objects.all()
    mylist = zip(travel, cars) 
    return render (request, "./dashboard/travel-agency/user-car-rental.html", {'view' : mylist})


def user_flight(request):
    travel = TravelModel.objects.all()
    flights = FlightdashboardModel.objects.all() 
    mylist = zip(travel, flights) 
    return render (request, "./dashboard/travel-agency/user-flight.html", {'view' : mylist})

def user_cruises(request):
    crui = CruisesdashboardModel.objects.all() 
    return render (request, "./dashboard/travel-agency/user-cruises.html", {'view' : crui})

def booking (request, id):
    room_id=request.session["hotel_id"]
    print(room_id)
    if request.method == "POST":
        room_addres = request.POST['room_addres']
        room_check_in = request.POST['room_check_in']
        room_check_out = request.POST['room_check_out']
        
        no_room = request.POST['no_room']
        no_adults = request.POST['no_adults']
        no_children = request.POST['no_children']
        email = request.POST['email']
        phone = request.POST['phone']
        roombooking = RoomBooking.objects.create(room_id=room_id,room_addres=room_addres,room_check_in=room_check_in,room_check_out=room_check_out,no_room=no_room,no_adults=no_adults, no_children=no_children,email=email,phone=phone)
        request.session["booking_id"] = roombooking.booking_id
        roombooking.save()
        messages.success(request, "successfully Booked Thankyou")
        booking = email
        demo = phone
        email = EmailMessage('Subject',f'Hello {booking}, your booking is confirmed\nBooking Details:\nRoom no:{no_room}\nCheck-in:{room_check_in}\nCheck-out:{room_check_out}', to=[ booking ])
        email.send()
        return redirect("room")

    return render(request, "./user/booking.html")

def car_booking (request, id):
    demo=request.session["agency_id"]
    print(demo)
    if request.method == "POST":
        car_from = request.POST['car_from']
        to = request.POST['to']
        journey_date = request.POST['journey_date']
        return_date = request.POST['return_date']
        pick_up = request.POST['pick_up']
        drop_off = request.POST['drop_off']
        email = request.POST['email']
        phone = request.POST['phone']

        carbooking = CarBooking.objects.create(agency_id=demo,car_from=car_from,to=to,journey_date=journey_date,return_date=return_date,pick_up=pick_up, drop_off=drop_off,email=email,phone=phone)
        carbooking.save()
        messages.success(request, "successfully Booked Thankyou")
        carbooking = email
        demo = phone
        email = EmailMessage('Subject',f'Hello {carbooking}, your booking is confirmed\nBooking Details:\nJourney Date:{journey_date}\nReturn Date:{return_date}\nPick_up:{pick_up}\ndrop -off : {drop_off} ', to=[ carbooking ])
        email.send()
        return redirect("user_car_rental")
    return render(request, "./user/car-booking.html")

def flight_booking(request, id):
    demo=request.session["agency_id"]
    if request.method == "POST":
        addres = request.POST['addres']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        passport = request.POST['passport']
        select_class = request.POST['select_class']
        no_adults = request.POST['no_adults']
        no_children = request.POST['no_children']
        email = request.POST['email']
        phone = request.POST['phone']

        flightbooking = FlightBooking.objects.create(agency_id=demo,addres=addres,check_in=check_in,check_out=check_out,passport=passport,select_class=select_class, no_adults=no_adults,no_children=no_children,email=email,phone=phone)
        flightbooking.save()
        messages.success(request, "successfully Booked Thankyou")
        flightbooking = email
        demo = phone
        email = EmailMessage('Subject',f'Hello {flightbooking}, your booking is confirmed\nBooking Details:\nPassport:{passport}\n No adults : {no_adults}\n Class : {select_class}\n No children:{no_children}\n check-in:{check_in}\n dcheck - out: {check_out} ', to=[ flightbooking ])
        email.send()
        return redirect("user_flight")
    return render(request, "./user/flight-booking.html")

def cruises_booking(request, id):
    demo=request.session["agency_id"]
    if request.method == "POST":
        addres = request.POST['addres']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        passport = request.POST['passport']
        select_class = request.POST['select_class']
        no_adults = request.POST['no_adults']
        no_children = request.POST['no_children']
        email = request.POST['email']
        phone = request.POST['phone']

        cruisesbooking = CruisesBooking.objects.create(agency_id=demo,addres=addres,check_in=check_in,check_out=check_out,passport=passport,select_class=select_class, no_adults=no_adults,no_children=no_children,email=email,phone=phone)
        cruisesbooking.save()
        messages.success(request, "successfully Booked Thankyou")
        cruisesbooking = email
        demo = phone
        
        email = EmailMessage('Subject',f'Hello {cruisesbooking}, your booking is confirmed\nBooking Details:\nPassport:{passport}\n No adults : {no_adults}\n Class : {select_class}\n No children:{no_children}\n check-in:{check_in}\n dcheck - out: {check_out} ', to=[ cruisesbooking ])
        
        email.send()
        return redirect("user_cruises")
    return render(request, "./user/cruises-booking.html")

def user_hotel_feedback(request,id, email):
    hotel = id
    email = email
    if request.method == 'POST':
        rating = request.POST.get('rating')
        
        comments = request.POST.get('comments')
        

        feedback = UserFeedback.objects.create(hotel_id = hotel,email=email, rating=rating, comments=comments)
        request.session['user_hotel_id']=feedback.hotel_id
        request.session['user_email']=feedback.email
        feedback.save()
        return redirect ('my_feedback')

    # hotel_id = HoteldashboardModel.objects.filter(hotel_id=id).first()
    # hotel = HotelModel.objects.all()
    # travel = TravelModel.objects.all()
    # booking_id = RoomBooking.objects.filter(room_id=id).first()
    return render(request,'./user/hotel-feedback.html')

def user_agency_feedback(request, id, email):
    travel = id
    email = email
    
   
    if request.method == 'POST':
        rating = request.POST.get('rating')
        
        comments = request.POST.get('comments')
    
        feedback = UserFeedback.objects.create(agency_id = travel, email=email,  rating=rating, comments=comments)
        request.session['user_agency_id']=feedback.agency_id
        request.session['agency_email']=feedback.email
        feedback.save()
        return redirect ('my_feedback')

    return render(request,'./user/feedback.html')






# def user_feedback(request):
#     if request.method == 'POST':
#         rating = request.POST.get('rating')
#         servies = request.POST.get('servies')
#         comments = request.POST.get('comments')
#         email = request.POST.get('email')
#         user_name = request.POST.get('user_name')
#         print(servies)
#         feedback = Feedback.objects.create(servies=servies, rating=rating, comments=comments, email=email, user_name=user_name)
#         request.session["servies"]=feedback.servies
#         feedback.save()
        
#         messages.success(request, "your feedback saved Thankyou")
#         return redirect('user_feedback')
#     return render (request, "./user/feedback.html")


def my_feedback (request):
    email =  request.session["user_email"]
    email1 =  request.session["agency_email"]
    user_email = request.session["user_email"]
    demo = UserFeedback.objects.filter(email=email)
    data = UserFeedback.objects.filter(email=email1)
    data1 = UserModel.objects.get(user_email=user_email)
    
    
    context = {
        'obj' : demo,
        'obj1' : data,
        'obj2': data1
       
    }
    return render (request, './user/my-feedback.html', context=context)



def updateprofile (request, id):    
    rooms = UserModel.objects.get(user_id=id)
    print('hello')
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_lastname = request.POST.get('user_lastname')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_phone')
        
        rooms = get_object_or_404(UserModel, user_id=id)
        rooms.user_name = user_name
        rooms.user_lastname = user_lastname
        rooms.user_email = user_email
        rooms.user_phone = user_phone
       
        if request.FILES["user_photo"] != None:
            user_photo = request.FILES.get("user_photo")
            rooms.user_photo = user_photo
        
        rooms.save(update_fields=["user_name","user_lastname","user_email","user_phone","user_photo"])
        rooms.save()
        return redirect("user_profile")

    return render(request, 'user/updateprofile.html', {'obj' : rooms})
