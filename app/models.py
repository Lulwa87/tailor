from django.db import models
from django.utils import timezone
from django.core.mail import send_mail 
from django.utils.http import urlquote  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from app.widget import ColorPickerWidget
from django import forms


# class ColorField(models.CharField):
# 	def __init(self, *args, **kwargs):
# 		kwargs['max_length'] = 10
# 		super(ColorField, self).__init__(*args, **kwargs)

# 	def formField(self, **kwargs, *args):
# 		kwargs['widget'] = ColorPickerWidget
# 		return super(ColorField, self).__init__(*args, **kwargs)

class ShippingAddress(models.Model):
	customer = models.ForeignKey('app.CustomUser')
	city = models.CharField(max_length=50, blank=False)
	block = models.IntegerField(blank=False)
	street = models.CharField(max_length=255, blank=False)
	avenue = models.CharField(max_length=255, blank=True)
	house_number = models.CharField(max_length=50, blank=False)
	mobile = models.CharField(max_length=50, blank=False)
	extra_instructions = models.CharField(max_length=50, blank=True)



# class ShoppingCart(models.Model):
# 	customer = models.ForeignKey('app.CustomUser')
# 	order_number = models.CharField(max_length=255, blank=False)
# 	readyproduct = models.ForeignKey('app.ReadyToWear')
# 	designproduct = models.ForeignKey('app.ProductDesign')



class ModelTag(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return '%s' % self.name

		
class ReadyToWear(models.Model):
	product_id = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	color = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	category = models.CharField(max_length=255, null=True, blank=True)
	description = models.CharField(max_length=225, null=True, blank=True)
	size = models.CharField(max_length=225, null=True, blank=True)
	fabric_tag = models.ManyToManyField('app.FabricTag', null=True, blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	brand = models.CharField(max_length=255, null=True, blank=True)
	def __unicode__(self):
		return '%s' % self.name

class ProductDesign(models.Model):
	product_id = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	color = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	# category = 
	description = models.CharField(max_length=225, null=True, blank=True)
	size = models.CharField(max_length=225, null=True, blank=True)
	model_tag = models.ManyToManyField('app.ModelTag', null=True, blank=True)
	material_tag = models.ManyToManyField('app.MaterialTag', null=True, blank=True)
	fabric_tag = models.ManyToManyField('app.FabricTag', null=True, blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	brand = models.CharField(max_length=255, null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.name


class MaterialTag(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return '%s' % self.name


class Material(models.Model):
	material_id = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	color = models.CharField(max_length=200, null=True, blank=True)
	material_tag = models.ManyToManyField('app.MaterialTag', null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.name


class Tailor(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	experience = models.CharField(max_length=200, null=True, blank=True)
	specialest = models.CharField(max_length=200, null=True, blank=True)
	model = models.ForeignKey('app.ProductDesign', null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.name


class FabricTag(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return '%s' % self.name


class Fabric(models.Model):
	fabric_id = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	color = models.CharField(max_length=200, null=True, blank=True)
	pattern = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	fabric_tag = models.ManyToManyField('app.FabricTag', null=True, blank=True)

	def __unicode__(self):
		return '%s' % self.name



# class Demo(models.Model):


class Measurment(models.Model):
	customer = models.ForeignKey('app.CustomUser')
	demo = models.FileField(upload_to = 'demos', null=True, blank=True)
	neck = models.FloatField(null=True, blank=True, default=0.00)
	shoulder = models.FloatField(null=True, blank=True, default=0.00)
	arm_hole = models.FloatField(null=True, blank=True, default=0.00)
	upper_arm = models.FloatField(null=True, blank=True, default=0.00)
	bust = models.FloatField(null=True, blank=True, default=0.00)
	length = models.FloatField(null=True, blank=True, default=0.00)
	sleeve = models.FloatField(null=True, blank=True, default=0.00)
	waist = models.FloatField(null=True, blank=True, default=0.00)
	hips = models.FloatField(null=True, blank=True, default=0.00)
	thighs = models.FloatField(null=True, blank=True, default=0.00)
	bottom_length = models.FloatField(null=True, blank=True, default=0.00)
	ankle = models.FloatField(null=True, blank=True, default=0.00)
	# font_color = ColorField(blank=True)

	def __unicode__(self):
		return '%s' % self.customer


class CustomUserManager(BaseUserManager):
	def __create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not email:
			raise ValueError('Email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email,
						  username=username,
						  is_staff=is_staff,
						  is_active=True, 
						  is_superuser=is_superuser, 
						  last_login=now, 
						  date_joined=now, 
						  **extra_fields
						)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, username, password=None, **extra_fields):
		return self.__create_user(email, username, password, False, False, **extra_fields)

	def create_superuser(self, email, username, password, **extra_fields):            
		return self.__create_user(email, username, password, True, True, **extra_fields)

		
class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField('email address', max_length=255, unique=True)
	username = models.CharField('username', max_length=255, unique=True)
	first_name = models.CharField('first name', max_length=255, blank=True, null=True)
	last_name = models.CharField('last name', max_length=255, blank=True, null=True)
	is_staff = models.BooleanField('staff status', default=False)
	is_active = models.BooleanField('active', default=False)
	date_joined = models.DateTimeField('date joined', auto_now_add=True)
	objects = CustomUserManager()


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'

	def __unicode__(self):
		return self.email


	def get_absolute_url(self):
		return '/users/%s' % urlquote(self.mail)


	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()


	def get_short_name(self):
		return self.first_name


	def email_user(self, subject, message, from_email=None):
		send_email(subject, message, from_email, [self.email])
