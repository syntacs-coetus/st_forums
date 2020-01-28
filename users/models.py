from django.db import models

# Create your models here.
class Users(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=65, unique=True)
	user_password = models.CharField(max_length=65)
	user_email = models.CharField(max_length=65)
	user_confkey = models.CharField(max_length=7, null=True)
	user_pin = models.CharField(max_length=16)
	user_registered = models.DateTimeField(auto_now_add=True, null=True)
	user_logged_in = models.DateTimeField(null=True)
	class Meta:
		db_table = 'user_accounts'

class Profile(models.Model):
	profile_id = models.OneToOneField(Users, primary_key=True, on_delete=models.PROTECT)
	profile_fname = models.CharField(max_length=65)
	profile_mname = models.CharField(max_length=65)
	profile_lname = models.CharField(max_length=65)
	profile_bday = models.DateField(null=True)
	profile_address = models.CharField(null=True, max_length=128)
	profile_updated = models.DateTimeField(null=True)
	class Meta:
		db_table = 'user_profiles'
