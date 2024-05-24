from django.shortcuts import render , HttpResponse , redirect
# from .models import register , author , feedback , ticket , state
from .models import *


# Demo code 

# Create your views here.
#to show messages  
def first(request):
    return HttpResponse('<h1>this is first page using html and css</h1')

# to show html pages
def second(request): 
    return render(request , 'demo.html')

def table(request):
    a = register.objects.all()
    b = author.objects.all()

    # all the row
    # for i in a:
        #  (i.number)
    return render(request,'table.html' , {'dataFetch':a , 'dataFetch2':b})

def nav(request):
    if 'email' in request.session:
        b = register.objects.get(email = request.session['email'])
        return render(request,'navbar.html' , {'session':b})
    return render(request,'navbar.html' , {'session':False})

def auth(request):
    if (request.method == 'POST'):
        # table
        a = author()
                    # name attribute value
        a.name = request.POST['name']
                    # for image
        a.post  = request.FILES['img']
        a.save()
        return render(request,'auth.html')
    else :
        return render(request,'auth.html')


def reg(request):
    if request.method == 'POST':
        # table
        b = register()
        # store the data
        b.name = request.POST['name']
        b.number = request.POST['number']
        b.confirm = request.POST['cpass']
        b.password = request.POST['pass']
        b.email = request.POST['email']
        b.address = request.POST['address']

        # print(request.method)
        c = register.objects.filter(name=b.name)
        error_msg = None
        if b.email:
            if c : 
                return render(request,'reg.html' , {'save':'Username already exists ... '})
            else:
                if (len(b.number) == 10):
                    if (b.password == b.confirm):
                        b.save()
                        return render(request,'reg.html' , {'save':'Data stored successfully ... '})
                    else:
                        return render(request, 'reg.html',{'save':'Password is not matching'})
                else:
                    error_msg = 'Contact length should be 10 digits'
                    return render(request, 'reg.html',{'error':error_msg})        
        else:
            error_msg = 'Please insert email '
            return render(request,'reg.html',{'error':error_msg})
    else:
        return render(request,'reg.html')
    
from django.core.mail import send_mail

def feed(request):
    if 'email' in request.session:
        a = register.objects.get(email =request.session['email'])
        if request.method == 'POST':
            c = feedback()
            c.name = request.POST['name']
            c.email = request.POST['email']
            c.message = request.POST['mes']

            send_mail(
                'authentication email',
                'This is mail to check if you received an email or not',
                'kalmatheroshan@gmail.com',
                [c.email],
                fail_silently = False 
            )


            c.save()
            
            return render(request,'feed.html',{'feed':a ,'session':a})
        else:
            return render(request,'feed.html',{"feed":a , 'session':a})


def login(request):
    if request.method == 'POST':
        if 'agen_email' in request.session:
            del request.session['agen_email']
        try:
            a =  register.objects.get(email = request.POST['email'])
            
            if a.password == request.POST['pass'] :
                        # session['name of session'] 
                request.session['email'] = a.email

                # return render(request, 'nav.html')
                        # see the change in url 
                        # redirect('name of path in url.py')
                return redirect('Home')
            else:
                return render(request ,'login.html', {'mes' : "password is incorrect"})
        except:
                return render(request ,'login.html', {'mes' : "User not found "})

    else:
        return render(request, 'login.html')


def logout(request):
    if 'email' in request.session:
        del request.session['email']

        # other things
        # del request.session['pincode']
        # del request.session['city']
        # del request.session['state']
        # del request.session['orderid']
        # del request.session['total']

        return redirect('Home')
    elif 'agen_email' in request.session:
        del request.session['agen_email']
        return redirect('Home')
    else:
        return redirect('Home')

def profile(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        return render(request , 'profile.html',{'data' :a, 'session':a})
    else:
        return redirect('Home')
    

def EditProfile(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        if request.method == 'POST':
            a.name = request.POST['name']
            a.number = request.POST['number']
            a.address = request.POST['address']
            a.save()
            return render(request , 'Edit_pro.html',{'data' :a , 'update':"data succesfully updated .. " , "session":a})
        else:
            return render(request , 'Edit_pro.html',{'data' :a, 'session':a})
    else:
        return redirect('Home')

def changePass(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        if request.method == 'POST':
           oldPassword = request.POST['oldPassword']
           password = request.POST['password']
           Cpassword = request.POST['Cpassword']
           if((oldPassword == a.password) & (password == Cpassword)):
                a.password = password
                a.save()
                return render(request , 'ch_pass.html',{'data' :a , 'update':"password succesfully updated .. " , "session":a})
           else:
                if(oldPassword != a.password ):
                    mes = "Please enter valid Password !!"
                else:
                    mes = "Enter both password same"
                return render(request , 'ch_pass.html',{'data' :a , 'error':mes , "session":a})
        return render(request,'ch_pass.html',{'session':a})
    else:
        return redirect('Home')

def Home(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        if request.method == 'POST':
             b = ticket()

             b.email =  a.email
             b.source = request.POST['source']
             b.destination = request.POST['destination']
             b.price = 0
             b.numTickets = 0
             c = state.objects.get(state = b.source) 
             b.stateid = c.pk 
             b.save()
             request.session['b.pk'] = b.pk


             return redirect('categ')
        else: 
             return render(request , 'Home.html' , {'session':a})
    elif 'agen_email' in request.session:
        b = agen_reg.objects.get(email = request.session['agen_email'])
        return render(request , 'Home.html' , {'agent':b})
    else:
        return render(request , 'Home.html')

    
def categ(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        temp = ticket.objects.get(id = request.session['b.pk'])
        des = state.objects.get(state = temp.source)
        obj_bus = bus.objects.filter(stateid = des.pk)
        return render(request,'Agency.html',{'session' :a,'data':obj_bus})
    else:
        return redirect('Home')

def seat(request , id):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        if request.method == 'POST':
            aid = request.session['b.pk']
            b = ticket.objects.get(id = aid)

            try:
                b.price = int(request.POST['price'])
                b.numTickets= int(request.POST['ticketC'])
            except:
                print('except ====================')
            b.agencyid = id

            b.save()
            
            bs = bus.objects.get(id = id)
            bs.seats = bs.seats -  b.numTickets
            bs.save()         

            return redirect('cart')
        else:
            bs = bus.objects.get(id = id)
            return render(request , 'seats.html' , {'session' :a,"price":bs.price})
    else:
        return redirect('Home')


def cart(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        c = ticket.objects.filter(email = a.email , orderid = "0")
        total= 0
        for i in c:
            total = i.price+ total
        for i in c:
            if i.numTickets == 0:
                i.delete()
        if len(c) == 0:
            return render(request,'card.html',{'session' :a ,'data':c,'total' :total})
        else:
            try:
                li =[]
                tid = []
                for i in c:
                    bs = bus.objects.get(id = i.agencyid)
                    bus_details = {"source":i.source,"destination":i.destination,"Total_Price":i.price,"price":bs.price, "numTickets":i.numTickets ,'agent':bs.agency, "agency":i.agencyid , "busid":bs.busid , "id":i.id}
                    li.append(bus_details)
                    tid.append(i.id)
            except :
                print(len(c), ' ================')
            finally:
                return render(request,'card.html',{'session' :a ,'data':li,'total' :total,"show" : True})
    else:
        return redirect('login')


def remove(request , agency , id):
    if 'email' in request.session:
        b = ticket.objects.get(id = id)
        # print(id)
        bs = bus.objects.get(id = agency)
        bs.seats = bs.seats +int(b.numTickets)
        bs.save()
        b.delete()
        return redirect('cart')
    else:
        return redirect('login')

def removeall(request ):
    if 'email' in request.session:
        b = ticket.objects.filter(email=request.session['email'])
        for i in b : 
            c = bus.objects.get(id = i.agencyid)
            c.seats = c.seats + i.numTickets
            c.save()
            i.delete()
        return redirect('cart')
    else:
        return redirect('login')


#               vender side 

def agen_register(request):
    if request.method == 'POST':
        # table
        b = agen_reg()
        # store the data
        b.name = request.POST['name']
        b.number = request.POST['number']
        b.confirm = request.POST['cpass']
        b.password = request.POST['pass']
        b.email = request.POST['email']
        b.address = request.POST['address']
        b.agen_name = request.POST['agency']

        # print(request.method)
        c = bus.objects.filter(agency = b.agen_name)
        error_msg = None
        if b.email:
            if c : 
                return render(request, 'Agency_reg.html' , {'save':'Agency already Reservied ... '})
            else:
                if (len(b.number) == 10):
                    if (b.password == b.confirm):
                        b.save()
                        return redirect('Home')
                    else:
                        return render(request, 'Agency_reg.html',{'save':'Password is not matching'})
                else:
                    error_msg = 'Contact length should be 10 digits'
                    return render(request, 'Agency_reg.html',{'error':error_msg})        
        else:
            error_msg = 'Please insert email '
            return render(request,'Agency_reg.html',{'error':error_msg})
    else:
        return render(request,'Agency_reg.html')

def agen_login(request):
    if 'email' in request.session:
       del request.session['email']
   
    if request.method == 'POST':
        a =  agen_reg.objects.get(email = request.POST['email'])
        try:
            if a.password == request.POST['pass'] :
                request.session['agen_email'] = a.email
                request.session['agencyid'] = a.id
                return redirect('Home')
            else:
                return render(request ,'login.html', {'mes' : "password is incorrect",'agent':a})
        except:
                return render(request ,'login.html', {'mes' : "User not found " , 'agent':a})
    else:
        return render(request, 'login.html')
    return render(request,'login.html')


def add_bus(request):
    if 'agen_email' in request.session:
        a = agen_reg.objects.get(email = request.session['agen_email'])
        if request.method == 'POST':
            bs = bus()
            bs.agency =request.POST['agency']
            bs.stateid = int(request.POST['stateid'])
            bs.busid = (request.POST['busid'])
            st = state.objects.get(pk = bs.stateid)
            # set foreign key
            bs.state  = st
            bs.price = int(request.POST['price'])
            bs.seats = 36
            bs.agencyid = request.session['agencyid']
            c = bus.objects.filter(agency = request.POST['agency'] , stateid = bs.stateid )
            if c:
                return render(request , 'bus_add.html' , {'mes':"Bus already exists",'agent':a})
            else:
                bs.save()
                return render(request , 'bus_add.html' , {'mes':"Bus added succesfully",'agent':a})
        else:
            return render(request , 'bus_add.html',{'agent':a})
    else:
        return redirect('agen_login')


def agen_added(request):
    a = agen_reg.objects.get(email = request.session['agen_email'])
    b = bus.objects.filter(agencyid = request.session['agencyid'])
    return render(request,'agen_added.html',{'agent':a, 'data':b})

def delete_agen(request , id):
    if 'agen_email' in request.session:
        bs = bus.objects.get(id = id)
        bs.delete()
        return redirect('agen_added')

def update_agen(request,id):
    a = agen_reg.objects.get(email = request.session['agen_email'])
    if 'agen_email' in request.session:
        if request.method == 'POST':
            bs = bus.objects.get(id = id)
            bs.agency =request.POST['agency']
            bs.stateid = int(request.POST['stateid'])
            bs.busid = (request.POST['busid'])
            st = (state.objects.get(pk = bs.stateid))
            # set foreign key
            bs.state  = st
            bs.price = int(request.POST['price'])
            bs.seats = 36
            bs.agencyid = request.session['agencyid']
            c = bus.objects.filter(agency = request.POST['agency'] , stateid = bs.stateid )
            bs.save()
            return render(request , 'bus_add.html' , {'mes':"Bus updated succesfully",'agent':a})
        else:
            bs = bus.objects.get(id = id)
            return render(request,'bus_update.html',{'agent':a,'data':bs})

def about_us(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email']) 
        return render(request,'about_us.html',{'session':a})
    else:
        return render(request,'about_us.html')

    
def checkout(request):
    if 'email' in request.session:
        a = register.objects.get(email = request.session['email'])
        c = ticket.objects.filter(email = a.email,orderid = '0')
        li = []
        for i in c:
            li.append(i.id)


        d = ticket.objects.filter(email = a.email,orderid = "0")
        total= 0
        for i in d:
            total = i.price+ total
        request.session['total'] = total
        if request.method == 'POST':
            request.session['orderid'] = li
            request.session['city']=request.POST['city']
            request.session['state'] = request.POST['state']
            request.session['pincode'] = request.POST['pincode']
            # Or.save()
      
            return redirect('razorpay')
        else:
             return render(request,'checkout.html',{'session':a,"total":total})
    else:
        return redirect('login')


from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


RAZOR_KEY_ID = 'rzp_test_FcbpcUy2hUtuPY'
RAZOR_KEY_SECRET = 'Srqt8Res8XNPK9FHJMdxK7e9'

# client authenticate
razorpay_client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request): 
    currency = 'INR'

    # paise
    amount = int(request.session['total'])*100

    # Create a Razorpay Order
    # razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/app/paymenthandler/'    
    #       #live
    # callback_url = 'paymenthandler/'    


    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpay.html',context=context)



@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            
            # amount = int(request.session['price'])*100  # Rs. 200
            amount = int(request.session['total'])*100  # Rs. 200
            # capture the payemt
            razorpay_client.payment.capture(payment_id, amount)
            # Order Save Code
            ar = order()
            ar.orderid = request.session['orderid']
            ar.city = request.session['city']
            ar.state = request.session['state'] 
            ar.pincode = request.session['pincode']
            ar.transactionid = payment_id
            ar.save()
            # update order id 
            a = register.objects.get(email = request.session['email'])
            c = ticket.objects.filter(email = a.email,orderid = '0')

            Latest_ord_id = order.objects.latest('id')
            for i in c:
                i.orderid = Latest_ord_id.pk
                i.save()

            return render(request,'succes.html', {"trans":payment_id} )
        except:
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()


def my_order(request):
    if 'email' in request.session:
        s = register.objects.get(email = request.session['email'])
        a = ticket.objects.filter(email = request.session['email'])
        li = []
        for i in a:
            c = bus.objects.get(id = i.agencyid,stateid = i.stateid)
            if i.orderid == '0':
                continue
            b = order.objects.get(id = i.orderid)
            data = {'src': i.source, 'des':i.destination,'price':i.price , "tickets":i.numTickets , 'transid':b.transactionid , 'datatime':b.datetime , 'agency':c.agency}
            li.append(data)
        return render(request, 'Myorder.html',{'session':s,'data':li})
    else:
        return redirect('login')
#         