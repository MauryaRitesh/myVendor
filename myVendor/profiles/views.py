from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import csv
from .forms import contactForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Orders
from PayTm import Checksum
from django.http import HttpResponse

MERCHANT_KEY = 'PAsM#uXIW9nnW_Zm'


# Create your views here.
def home(request):
	context = locals()
	template = 'home.html'
	return render(request, template, context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request, template, context)

def contact(request):
	title = "Contact"
	form = contactForm(request.POST or None)
	confirm_message = None


	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = "Message from MyVendor."
		message = "{} {}".format(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		#send_mail(subject, message, emailFrom,emailTo ,fail_silently = True,)
		dict1 = {'name':name, 'email':emailFrom, 'contact_message':comment,}
		with open("data.csv", 'a') as csvfile:
			wrt = csv.writer(csvfile)
			for key, value in dict1.items():
				wrt.writerow([key, value])
			csvfile.write('\n')

		title = "Thanks!"
		confirm_message = "Thanks for Contacting Us. We'll get right back to you."
		context = { "title":title, "confirm_message":confirm_message, }
		form = None




	context = {"title":title, "form":form, "confirm_message":confirm_message, }
	template = 'contact.html'
	return render(request, template, context)

def services(request):
	context = locals()
	template = 'services.html'
	return render(request, template, context)


#Products
#Note: In future keep only one function along with product's id &
#then call the desired product using that id.
def potatoes(request):
	context = locals()
	template = 'products/potatoes.html'
	return render(request, template, context)
def cl(request):
	context = locals()
	template = 'products/cauliflower.html'
	return render(request, template, context)

def tomato(request):
	context = locals()
	template = 'products/tomato.html'
	return render(request, template, context)

def spinach(request):
	context = locals()
	template = 'products/spinach.html'
	return render(request, template, context)

def capcicum(request):
	context = locals()
	template = 'products/capcicum.html'
	return render(request, template, context)

def brinjal(request):
	context = locals()
	template = 'products/brinjal.html'
	return render(request, template, context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = "profile.html"
	return render(request,template,context)
@login_required
def checkout(request):
	if request.method=="POST":
		items_json = request.POST.get('items_json', '')
		name = request.POST.get('name', '')
		#amount = request.POST.get('amount', '')
		amount = str(1000)
		email = request.POST.get('email', '')
		address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
		city = request.POST.get('city', '')
		state = request.POST.get('state', '')
		zip_code = request.POST.get('zip_code', '')
		phone = request.POST.get('phone', '')

		order = Orders(items_json = items_json, name = name, email=email, address=address, city = city, state=state, zip_code=zip_code, phone=phone, amount=amount,)
		order.save()

		thank = True
		id = order.order_id
		#return render(request, 'checkout.html',{'thank':thank, 'id':id})
		param_dict = {"MID":"pLrzNJ16841966718931", "ORDER_ID":str(order.order_id), "TXN_AMOUNT":str(amount), "CUST_ID":email, "INDUSTRY_TYPE_ID":"Retail", "WEBSITE":"WEBSTAGING", "CHANNEL_ID":"WEB", "CALLBACK_URL":"http://myvendor.pythonanywhere.com/handlerequest/"}
		param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
		return render(request, 'paytm.html', {'param_dict':param_dict})


	return render(request, 'checkout.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Order Placed!')
            print (response_dict)
        else:
            print('Order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


#