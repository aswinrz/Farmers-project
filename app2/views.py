from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, request
from django.shortcuts import render

#Create your views here.

from app2.models import login_table,user_table,farmer_table,complaint_table,product_table,product_rating_and_feedback,notification_table,feedback_and_rating



def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')


def login(request):
    return render(request,"login index.html")


def login_code(request):
    un=request.POST['textfield']
    ps=request.POST['textfield2']

    ob = login_table.objects.filter(username=un, password=ps)
    if ob.exists():
        obb = login_table.objects.get(username=un, password=ps)

        if obb.type == "admin":
            request.session['lid'] = obb.id

            return HttpResponse('''<script>alert('welcome admin');window.location='/admin_home'</script>''')
        elif obb.type == "user":
            request.session['lid'] = obb.id
            return HttpResponse('''<script>alert('Welcome User');window.location='/user_home'</script>''')
        elif obb.type == "farmer":
            request.session['lid'] = obb.id
            return HttpResponse('''<script>alert('Welcome Farmer');window.location='/farmer_home'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/'</script>''')

    # except:
    #     return HttpResponse('''<script>alert('invalid');window.location='/'</script>''')
    #
def  user_registration(request):
    return render(request, "reg index.html")


def user_registration_post(request):
    first_name = request.POST['textfield']
    last_name= request.POST['textfield2']
    gender= request.POST['gender']
    phone_number= request.POST['textfield3']
    email= request.POST['textfield4']
    place= request.POST['textfield5']
    pin= request.POST['textfield6']
    username= request.POST['textfield8']
    password= request.POST['textfield7']



    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type="user"
    ob.save()



    ob1=user_table()
    ob1.first_name=first_name
    ob1.last_name=last_name
    ob1.gender=gender
    ob1.phone_number=phone_number
    ob1.e_mail=email
    ob1.place=place
    ob1.pin=pin
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('<script>("Registration Complete");window.location="/"</script>')

def farmer_Registration(request):
    return render(request,"farmer registration.html")

def Farmer_registration_post(request):
    first_name=request.POST['textfield']
    Gender=request.POST['gender']
    Place=request.POST['textfield3']
    Pin=request.POST['textfield4']
    Phone_number=request.POST['textfield5']
    Email=request.POST['textfield6']
    Username=request.POST['textfield7']
    Password=request.POST['textfield8']

    ob=login_table()
    ob.username=Username
    ob.password=Password
    ob.type="pending"
    ob.save()

    ob1=farmer_table()
    ob1.first_name=first_name
    ob1.gender=Gender
    ob1.place=Place
    ob1.pin=Pin
    ob1.phone_number=Phone_number
    ob1.e_mail=Email
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('''<script>("registration complete");window.location="/"</script>''')



#_________________________________ADMIN____________________________

def admin_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    return render(request,"sp-admin/adminindex.html")

def view_user(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=user_table.objects.all()
    return render(request,"sp-admin/admin-view user.html",{"d1":data})

def view_complaint(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=complaint_table.objects.all()
    return render(request,"sp-admin/admin view complaint of user.html",{"d1":data})

def search_date_view_complaint(request):
    f = request.POST['f']
    name = request.POST['t']
    ob = complaint_table.objects.filter(date__range=[f,name])
    return render(request, "sp-admin/admin view complaint of user.html", {'d1': ob})


def send_reply(request,id):
    request.session['cid'] = id
    return render(request,"sp-admin/admin send reply.html")
    # return HttpResponse('''<script> alert("Reply send");window.location="/view_complaint"</script>''')

def admin_send_reply(request):
    reply=request.POST['textfield']
    ob=complaint_table.objects.get(id=request.session['cid'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script> alert("Reply send");window.location="/view_complaint"</script>''')


def view_accept_farmer(request,id):
    data=login_table.objects.get(id=id)
    data.type="pending"
    data.save()
    return HttpResponse('''<script> alert("verification complited");window.location="/view_farmer_and_verify"</script>''')

def view_farmer_and_verify(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=farmer_table.objects.all()
    return render(request,"sp-admin/admin view farmer and verify.html",{"d1":data})

def acceptfarm(request,id):
    ob=login_table.objects.get(id=id)
    ob.type="farmer"
    ob.save()
    return HttpResponse('''<script> alert("Accepted");window.location="/view_farmer_and_verify"</script>''')


def rejectfarm(request,id):
    ob=login_table.objects.get(id=id)
    ob.type="REJECTED"
    ob.save()
    return HttpResponse('''<script> alert("REJECTED");window.location="/view_farmer_and_verify"</script>''')




#_________________________farmer_____________________________________

def farmer_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    return render(request,"sp-farmer/farmerindex.html")

def farmer_edit_product(request,id):
    request.session['pname_id']=id
    ob=product_table.objects.get(id=id)
    return  render(request,"sp-farmer/f_edit_n.html",{'val':ob})

def edit_product(request):
   try:
       pname = request.POST['textfield']
       Image = request.FILES['file']
       fs = FileSystemStorage()
       fp = fs.save(Image.name, Image)
       Discription = request.POST['textfield2']
       Rate = request.POST['textfield3']
       quality = request.POST['textfield4']

       ob = product_table.objects.get(id=request.session['pname_id'])
       ob.product = pname
       ob.image = fp
       ob.description = Discription
       ob.rate = Rate
       ob.quality = quality
       ob.save()
       return HttpResponse(
           '''<script> alert("product details Edited");window.location="/farmer_manage_product"</script>''')
   except:
       pname = request.POST['textfield']
       Discription = request.POST['textfield2']
       Rate = request.POST['textfield3']
       quality = request.POST['textfield4']

       ob = product_table.objects.get(id=request.session['pname_id'])
       ob.product = pname
       ob.description = Discription
       ob.rate = Rate
       ob.quality = quality
       ob.save()
       return HttpResponse(
           '''<script> alert("product details Edited");window.location="/farmer_manage_product"</script>''')

def search_product(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    name=request.POST['textfield']
    ob=product_table.objects.filter(PRODUCT__istartswith=name)
    return render(request,"sp-farmer/farmer manage product.html",{"val":ob})


def delete_product(request,id):
    ob=product_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("product deleted");window.location="/farmer_manage_product"</script>''')

def farmer_manage_product(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=product_table.objects.filter(FARMER__id=request.session['lid'])
    return render(request,"sp-farmer/farmer manage product.html",{"val":data})

def add_new_product(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    return render(request,"sp-farmer/farmer add new product.html")


def add_new_product_post(request):
    product_name = request.POST['textfield']
    image = request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(image.name,image)
    discription = request.POST['textfield2']
    rate = request.POST['textfield3']
    stock = request.POST['textfield4']

    ob =product_table()
    ob.PRODUCT=product_name
    ob.image=fn
    ob.description=discription
    ob.rate=rate
    ob.quality=stock
    ob.FARMER=login_table.objects.get(id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>("new product is add");window.location="/farmer_manage_product"</script>''')


def farmer_view_feedback_and_rating(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=product_rating_and_feedback.objects.all()
    return render(request,"sp-farmer/farmer view feedback and rating.html",{"d1":data})

def search_feedback_and_rating(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    name=request.POST['textfield']
    ob=product_rating_and_feedback.objects.filter(PRODUCT__PRODUCT__istartswith=name)
    return render(request, "sp-farmer/farmer view feedback and rating.html", {"d1": ob})


def farmer_view_complaint_and_view_reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=complaint_table.objects.all()
    return render(request,"sp-farmer/farmer view complaint and view reply.html",{"d1":data})

def farmer_reply(request,id):
    request.session['cid'] = id
    return render(request, "sp-farmer/farmer reply.html")
    #return HttpResponse('''<script> alert("Reply send");window.location="/farmer view complaint and view reply.htm"</script>''')

def farmer_send_reply(request,):
    reply=request.POST['textfield']
    ob = complaint_table.objects.get(id=request.session['cid'])
    ob.reply = reply
    ob.save()
    return HttpResponse('''<script> alert("Reply send");window.location="/farmer_view_complaint_and_view_reply"</script>''')


def search_date_complaint_reply(request):
    name=request.POST['textfield']
    ob=complaint_table.objects.filter(date=name)
    return render(request,"sp-farmer/farmer view complaint and view reply.html",{'d1':ob})

def send_notification(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')


    name=notification_table.objects.all()
    return render(request,"sp-farmer/farmer send notification.html")


def farmer_send_noti(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    send=request.POST['textfield']
    ob=notification_table()
    ob.notification=send
    ob.date = datetime.now()
    ob.save()
    return HttpResponse('''<script> alert("Reply send");window.location="/farmer_home"</script>''')


def farmer_view_profile(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data = farmer_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request, "sp-farmer/farmer view profile.html", {"val": data})


#__________________________user______________________________

def user_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    return render(request,"sp-user/userindex.html")

def view_product_rating_and_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=product_rating_and_feedback.objects.all()
    return render(request,"sp-user/user view product rating and feedback.html",{"d1":data})

def search_product_rating_fb(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    name=request.POST['textfield']
    ob=product_rating_and_feedback.objects.filter(PRODUCT__PRODUCT__istartswith=name)
    return render(request, "sp-user/user view product rating and feedback.html", {"d1": ob, "name": name})




def view_product(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=product_table.objects.all()
    return render(request,"sp-user/user view product.html",{"d1":data})

def search_user_view_product(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    name = request.POST['textfield']
    ob = product_table.objects.filter(PRODUCT__istartswith=name)
    return render(request, "sp-user/user view product.html", {"d1": ob})


def view_notification(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data=notification_table.objects.all()
    return render(request,"sp-user/user view notification.html",{"d1":data})



def send_rating_and_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    ob=farmer_table.objects.all()
    ob1 = product_table.objects.all()
    return render(request,'sp-user/user send rating and feedback.html',{"val":ob, "val1":ob1 })


def user_send_rating_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    rating = request.POST['select']
    feedback = request.POST['textfield2']
    product=request.POST['select2']
    ob = product_rating_and_feedback()
    ob.feedback = feedback
    ob.rating = rating
    ob.PRODUCT=product_table.objects.get(id=product)
    ob.date = datetime.today().date()
    ob.USER = user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script> alert(" send");window.location="/user_home"</script>''')



def user_complaint_to_farmer(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    data = complaint_table.objects.all()
    return render(request, "sp-user/user complaint to farmer.html", {'d1': data})

def send_complaint(request):
    ob = product_table.objects.all()
    return render(request, 'sp-user/send_complaint_user.html',{"val":ob,})

def search_complaint_product(request):
    name = request.POST['textfield']
    ob = complaint_table.objects.filter(PRODUCT__PRODUCT__icontains=name)
    return render(request, "sp-user/user complaint to farmer.html", {"d1": ob})





def send_complaint_user(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('logout successful');window.location='/'</script>''')

    product_id = request.POST['select2']
    complaint=request.POST['complaint']
    ob = complaint_table()
    ob.complaint = complaint
    ob.PRODUCT=product_table.objects.get(id=product_id)
    ob.USER=user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.date =datetime.now()
    ob.reply='pending'
    ob.save()
    return HttpResponse('''<script> alert("Add");window.location="user_complaint_to_farmer"</script>''')


























































