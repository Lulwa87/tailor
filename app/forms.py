from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import CustomUser, Measurment, Model, Fabric

class CreateFabricForm(forms.ModelForm):
	class Meta:
		model = Fabric
		fields = '__all__'



class EditFabricForm(forms.ModelForm):
	class Meta:
		model = Fabric
		fields = '__all__'



class CreateModelForm(forms.ModelForm):
	class Meta:
		model = Model
		fields = '__all__'



class EditModelForm(forms.ModelForm):
	class Meta:
		model = Model
		fields = '__all__'




class MeasurmentsForm(forms.ModelForm):
	class Meta:
		model = Measurment
		fields = '__all__'




class EditProfileForm(forms.ModelForm):

	class Meta:
		model = CustomUser
		fields = ['email', 'first_name', 'last_name']




class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		# del self.fields['username']
	class Meta:
		model = CustomUser
		fields = ("email",)




class CustomUserChangeForm(UserChangeForm):
		def __init__(self, *args, **kwargs):
			super(CustomUserChangeForm, self).__init__(*args, **kwargs)
			del self.fields['username']
		class Meta:
			model = CustomUser
			fields = '__all__'




class CustomUserLoginForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())


