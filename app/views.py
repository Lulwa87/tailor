from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from app.models import CustomUser, Measurment, Model, Fabric, Tailor
from django.http import HttpResponse, Http404, HttpResponseRedirect
from app.forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserChangeForm, EditProfileForm, MeasurmentsForm, EditModelForm, CreateModelForm, EditFabricForm, CreateFabricForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


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

	model = Model.objects.get(pk=pk)

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
	model = Model.objects.get(pk=pk)
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



def model_detail(request, pk):
	context = {}
	model = Model.objects.get(pk=pk)
	context['model'] = model

	return render(request, 'model_detail.html', context)



def model_list(request):
	context = {}
	models = Model.objects.all()
	context['models'] = models

	return render(request, 'model_list.html', context)


def measurments(request):
	context = {}
	context['form'] = MeasurmentsForm()
	if request.method == 'POST':
		form = MeasurmentsForm(request.POST)
		context['form'] = form
		if form.is_valid():
			form.save()
	
	return render(request, 'measurments.html', context)



def profile_page(request):

	context = {}

	print request.user 
	print request.user.pk 

	try:

		context['user'] = CustomUser.objects.get(pk=request.user.pk)
	except Exception, e:
		raise HTTP404('404')

	return render(request, 'profile_page.html', context)



def edit_profile(request):

	context = {}

	try:
		user = CustomUser.objects.get(pk=request.user.pk)

	except Exception, e:
		raise HTTP404('404')

	form = EditProfileForm(request.POST or None, instance=user)

	context['form'] = form

	if form.is_valid():
		form.save()
		return redirect('/profile/')

	else:
		print form.errors

	return render(request, 'edit_profile.html', context)



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
				return HttpResponse('invalid user, try again <a href="/signup/">here</a>')
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
	return render(request, 'signin.html', context)



def logout_view(request):
	logout(request)
	return redirect('/signup/')
