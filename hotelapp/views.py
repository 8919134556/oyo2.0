from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
# Create your views here.
from django.shortcuts import render
from .models import HotelModel
from .models import HoteldashboardModel
from userapp.models import RoomBooking
from mainapp.models import UserFeedback
from userapp.models import UserModel
import re



def hotel_registration(request):
    if request.method == "POST" and request.FILES["hotel_photo"] and request.FILES["hotel_certificate"]:
        hotel_name = request.POST['hotel_name']
        pannumber = request.POST['pannumber']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        hotel_photo = request.FILES ["hotel_photo"]
        hotel_certificate = request.FILES ["hotel_certificate"]
        if len(hotel_name) > 20:
            
            messages.error (request, "user name must be 10 characters")
       
        
        elif re.search('[A-Z]{4}[0-9]{4}[A-Z]{1}', pannumber) is None :
            messages.error(request, "plase enter vailed pannumber")
            
        

        elif HotelModel.objects.filter(hotel_email=email).exists():
            messages.error (request, "Email alredy exist")
        
            return redirect("hotel_registration")
        else: 
            hotel_registation = HotelModel.objects.create(hotel_name=hotel_name,hotel_pan_number=pannumber,hotel_addres=address,hotel_phone=phone,hotel_email=email,hotel_pwd=password,hotel_photo=hotel_photo,hotel_certificate=hotel_certificate)
            hotel_registation.save()
            messages.success(request, "your account has been successfully created")
            return redirect('hotel_owners')
    return render(request, "hotel/hotel-register.html")

def hotel_owners(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            login = HotelModel.objects.get(hotel_email=email,hotel_pwd=password)
            request.session["hotel_id"]=login.hotel_id
            status = login.status
            print("hallo")
            if status == "Accepted":
                print('ok')
                request.session['email'] = login.hotel_email
                return redirect ("hotel_index")
                print("hallo")
            else : 
                messages.success(request, "your account not at activated")
            
        except:
            messages.error(request, "bad credential Please Register")
            return redirect("hotel_registration")
    return render(request, "hotel/hotel-owners.html")


def add_room(request):
    hotel_id=request.session["hotel_id"]
    if request.method == "POST" and request.FILES["room_photo"] :
        room_type = request.POST['room_type']
        room_size = request.POST['room_size']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        price = request.POST['price']
        description = request.POST['description']
        hotel_policies = request.POST['hotel_policies']
        room_photo = request.FILES ["room_photo"]

        add_room = HoteldashboardModel.objects.create(hotel_id=hotel_id,room_type=room_type,room_size=room_size,check_in=check_in,check_out=check_out,price=price,description=description,hotel_policies=hotel_policies, room_photo=room_photo)
        request.session["room_id"] = add_room.room_id
        messages.success(request, "successfully added")
        return redirect('view_room')
        
    return render(request, "dashboard/hotel-corporate-admin/add-room.html")




def hotel_index(request):
    hotel_id=request.session["hotel_id"]
    rooms = HoteldashboardModel.objects.filter(hotel_id=hotel_id)

    
    
    rooms_count = rooms.count()
    context = {
        'rooms_count' : rooms_count

    }
   
    return render (request, "dashboard/hotel-corporate-admin/index.html", context)



def edit_room(request):
    demo = request.session["hotel_id"]
    rooms = HoteldashboardModel.objects.filter(hotel_id=demo)
    return render(request, "dashboard/hotel-corporate-admin/edit-rooms.html", {'view' : rooms})

# this function is delete 
def deleroom(request, id):
    rooms = HoteldashboardModel.objects.get(room_id=id)
    rooms.delete()
    return redirect('edit_room')

# thsi function update
def updateroom(request, id):    
    rooms = HoteldashboardModel.objects.get(room_id=id)
    print('hello')
    if request.method == "POST":
        room_type = request.POST.get('room_type')
        room_size = request.POST.get('room_size')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        price = request.POST.get('price')
        description = request.POST.get('description')
        hotel_policies = request.POST.get('hotel_policies')
       
        
        rooms = get_object_or_404(HoteldashboardModel, room_id= id)
        rooms.room_type = room_type
        rooms.room_size = room_size
        rooms.check_in = check_in
        rooms.check_out = check_out
        rooms.price = price
        rooms.description = description
        rooms.hotel_policies = hotel_policies
        if request.FILES["room_photo"] != None:
            room_photo = request.FILES.get("room_photo")
            rooms.room_photo = room_photo
        
        rooms.save(update_fields=["room_type","room_size","check_in","check_out","price", "description","hotel_policies", "room_photo"])
        rooms.save()
        return redirect("view_room")

    return render(request, 'dashboard/hotel-corporate-admin/edit_room_form.html', {'ro' : rooms})




def edit_room_form(request, id):
    rooms = HoteldashboardModel.objects.get(room_id=id)
    if request.method == "POST" and request.FILES.get("room_photo") :
        room_type = request.POST.get('room_type')
        room_size = request.POST.get('room_size')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        price = request.POST.get('price')
        description = request.POST.get('description')
        hotel_policies = request.POST.get('hotel_policies')
        room_photo = request.FILES .get("room_photo")

        rooms = get_object_or_404(HoteldashboardModel, room_id= id)
       
        rooms.room_type = room_type
        rooms.room_size = room_size
        rooms.check_in = check_in
        rooms.check_out = check_out
        rooms.price = price
        rooms.description = description
        rooms.hotel_policies = hotel_policies
        rooms.room_photo = room_type
        
        rooms.save(update_fields=["room_type","room_size","check_in","check_out","price", "description","hotel_policies", "room_photo" ])
        messages.success(request,'Updated Successfully')
        return redirect("view_room")
    return render(request, "dashboard/hotel-corporate-admin/edit_room_form.html" )








def hotel_feedback(request):
    
    hotel_id = request.session['hotel_id']
    
    
    demo = UserFeedback.objects.filter(hotel_id=hotel_id)



    return render (request, "dashboard/hotel-corporate-admin/hotel-feedback.html", {'view' : demo} )



def hotel_profile(request):
    email = request.session["hotel_id"]
    

    data = HotelModel.objects.get(hotel_id=email)
    context = {'obj': data }
    return render (request, "dashboard/hotel-corporate-admin/hotel-profile.html", context=context)
 
def view_room(request):
    demo = request.session["hotel_id"]

    rooms = HoteldashboardModel.objects.filter(hotel_id=demo)

    return render (request, "dashboard/hotel-corporate-admin/view-room.html", {'view' : rooms})

def view_booking(request):
    data = request.session["hotel_id"]
    obj = RoomBooking.objects.filter(room_id = data)
    return render (request, "dashboard/hotel-corporate-admin/view-booking-details.html", {'view' : obj})