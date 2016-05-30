from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from app.models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
#email
from django.views.generic.base import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings 
# create your views here:

#cart
from cart.forms import CartAddProductForm

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id,
										 slug=slug, 
										 available=True)
	cart_product_form = CartAddProductForm()
	return render(request,
				  'app/detail.html',
				  {'product': product,
				   'cart_product_form': cart_product_form})


def sendmail(request):
	print "sendmail"
	form = EmailForm(request.POST or None)
	print form 
	if form.is_valid():
		print "form is valid"
		firstname = form.cleaned_data.get('firstname')
		lastname = form.cleaned_data.get('lastname')
		email = form.cleaned_data.get('email')
		subject = form.cleaned_data.get('subject')
		message = form.cleaned_data.get('message')
		
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'haljeri@icloud.com']
		contact_message = "%s: %s via %s"%(
				firstname,  
				message, 
				email,)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
		return HttpResponseRedirect('/thankyou/')
	context = {
		"form": form,
	}

	return render(request, 'contact.html', context)


@staff_member_required
def delete_fabric(request, pk):

	fabric = Fabric.objects.get(pk=pk)

	fabric.delete()

	return redirect('/fabric_list/')



@staff_member_required
def create_fabric(request):
	context = {}

	form = CreateFabricForm()

	context['form'] = form

	if request.method == 'POST':
		form = CreateFabricForm(request.POST)

		if form.is_valid():
			form.save()

		context['form'] = form 
	return render(request,'create_fabric.html', context)


@staff_member_required
def edit_fabric(request, pk):
	context = {}
	fabric = Fabric.objects.get(pk=pk)
	context['fabric'] = fabric
	form = EditFabricForm(request.POST or None, instance=fabric)
	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/edit_fabric/%s' % fabric.id)
	return render_to_response('/creat_fabric.html', context, context_instance=RequestContext(request))




@staff_member_required
def delete_model(request, pk):

	model = ProductDesign.objects.get(pk=pk)

	model.delete()

	return redirect('/model_list/')



@staff_member_required
def create_model(request):
	context = {}

	form = CreateModelForm()

	context['form'] = form

	if request.method == 'POST':
		form = CreateModelForm(request.POST)

		if form.is_valid():
			form.save()

		context['form'] = form 
	return render(request,'create_model.html', context)


@staff_member_required
def edit_model(request, pk):
	context = {}
	model = ProductDesign.objects.get(pk=pk)
	context['model'] = model
	form = EditModelForm(request.POST or None, instance=model)
	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/edit_model/%s' % model.id)
	return render_to_response('/creat_model.html', context, context_instance=RequestContext(request))





def tailor_detail(request, pk):
	context = {}
	tailor = Tailor.objects.get(pk=pk)
	context['tailor'] = tailor

	return render(request, 'tailor_detail.html', context)



def tailor_list(request):
	context = {}
	tailors = Tailor.objects.all()
	context['tailors'] = tailors

	return render(request, 'fabric_list.html', context)




def fabric_detail(request, pk):
	context = {}
	fabric = Fabric.objects.get(pk=pk)
	context['fabric'] = fabric

	return render(request, 'fabric_detail.html', context)



def fabric_list(request):
	context = {}
	fabrics = Fabric.objects.all()
	context['fabrics'] = fabrics

	return render(request, 'fabric_list.html', context)



def product_design_detail(request, pk):
	context = {}
	product = ProductDesign.objects.get(pk=pk)
	context['product'] = product

	return render(request, 'DesignDetail.html', context)



def product_design_list(request):
	context = {}
	products = ProductDesign.objects.all()
	context['products'] = products
	print products
	return render(request, 'design.html', context)

def Ready_to_wear(request):
	context = {}
	products = ReadyToWear.objects.all()
	context['products'] = products
	return render(request, 'readytowear.html', context)

def ready_detail(request, pk):
	context = {}
	product = ReadyToWear.objects.get(pk=pk)
	context['product'] = product

	return render(request, 'ReadyToWearDetail.html', context)


def measurments(request):
	context = {}
	context['form'] = MeasurmentsForm()
	if request.method == 'POST':
		form = MeasurmentsForm(request.POST)
		context['form'] = form
		if form.is_valid():
			form.save()
	
	return render(request, 'measurments.html', context)


def sign_up(request):
	context = {}
	context['form'] = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		context['form'] = form
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password1', None)
			auth_user = authenticate(username=email, password=password)
			try:
				login(request, auth_user)
			except Exception, e:
				print e 
				return HttpResponse('invalid user, try again <a href="/login/">here</a>')
	return render(request, 'signup.html', context)



def login_view(request):
	context = {}
	context['form'] = CustomUserLoginForm()
	if request.method == 'POST':
		form = CustomUserLoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password', None)
			auth_user = authenticate(username=email, password=password)
			
			try:
				login(request, auth_user)
			except Exception, e:
				message = """
				username or password incorrect, try again
				<a href='/login/'>login</a>
				""" 
				return HttpResponse(message)
	return render(request, 'login.html', context)



def logout_view(request):
	logout(request)
	return redirect('/login/')


# def json_response(request):
# 	search_string = request.GET.get('search', '')
# 	if search_string == "":
# 		area_list = []
# 		for gov in Gov.objects.filter(name__icontains=search_string):
# 		#	x = {'name':gov.name, 'id':gov.pk,'type': 'gov'}
# 			x = {'name':gov.name, 'id':gov.pk}
# 			area_list.append(x)
# 		for area in Area.objects.filter(name__icontains=search_string):
# 	#		area_list.append(['name' ,area.name, area.pk, 'area'])
# 			area_list.append({'name':area.name, 'id':area.pk})
# 		return JsonResponse(area_list, safe=False)
# 	else:
# 		return JsonResponse("", safe=False)

# def ajax_search(request):
# 	context = {}
# 	return render_to_response('ajax_search.html', context, context_instance=RequestContext(request))

# def search_view(request):
# 	context = {}
# 	context['form'] = Searchbox()
# 	if request.method == 'POST':
# 		form = Searchbox(request.POST or None)
# 		context['form'] = form
# 		if form.is_valid():
# 			x = {}
# 			if form.cleaned_data.get('parking', None) != None:
# 				x['parking__gte']=form.cleaned_data.get('parking', '0')
# 				print x['parking__gte']
# 			if form.cleaned_data.get('internet', None) is True:
# 				x['internet']=form.cleaned_data.get('internet', None)
# 			if form.cleaned_data.get('pets', None) is True:
# 				x['pets']=form.cleaned_data.get('pets', None)
# 			if form.cleaned_data.get('maidroom', None) is True:
# 				x['maidroom']=form.cleaned_data.get('maidroom', None)
# 			if form.cleaned_data.get('lift', None) is True:
# 				x['lift']=form.cleaned_data.get('lift', None)
# 			if form.cleaned_data.get('balcony', None) is True:
# 				x['balcony']=form.cleaned_data.get('balcony', None)
# 			if form.cleaned_data.get('bills', None) is True:
# 				x['bills']=form.cleaned_data.get('bills', None)
# 			if form.cleaned_data.get('area', None) != None:
# 				area=form.cleaned_data.get('area', None)
# 				search_result = area.apartment_set.filter(**x)
# 				print x
# 				print area
# 			else:
# 				areas=Area.objects.all()
# 				search_result = []
# 				for area in areas:
# 					if not area.apartment_set.filter(**x):
# 						empty = 'empty'
# 					else:
# 						search_result.append(area.apartment_set.filter(**x))
# 				print search_result
# 				context['apartments'] = search_result
# 			return render(request, 'apartment_list.html', context)
# 	print 'first'
# 	return render(request, 'apartment_list.html', context)



def profile_page(request):
	context = {}
	print request.user
	print request.user.pk
	try:
		context['user'] = CustomUser.objects.get(pk=request.user.pk)
	except Exception, e:
		raise Http404('404')
	return render(request, 'profile_page.html', context)

def edit_profile(request):
	context = {}
	try:
		user = CustomUser.objects.get(pk=request.user.pk)
	except Exception, e:
		raise Http404('404')
	form = EditProfileForm(request.POST or None, instance=user)
	context['form'] = form
	if form.is_valid():
		form.save()
		return redirect('/profile/')
	else:
		print form.errors
	return render(request, 'edit_profile.html', context)
