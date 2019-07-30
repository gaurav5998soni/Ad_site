from django.db import models
from django.contrib.auth.models import User
import json

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=12)
	pri_site = models.CharField(max_length=200)
	ac_type = models.BooleanField(default=True) # True : WebSiteMonetize && False : AdProvider

	def __str__(self) :
		return str(self.user)

class AdUnit(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=12)	
	website = models.CharField(max_length=200)
	tags = models.CharField(max_length=1000)
	ad_type = models.CharField(max_length=20)
	ad_shape = models.CharField(max_length=10)
	alternate = models.CharField(max_length=20)
	total_views = models.IntegerField(default=0)
	total_click = models.IntegerField(default=0)

	def set_tags(self, x):	##Store Tags In  JSON
		self.tags = json.dumps(x)

	def get_tags(self):		##Fetch Tags in JSON
		return json.loads(self.tags)

class TextAd(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=12)	
	link = models.CharField(max_length=500)
	content = models.CharField(max_length=500)
	tags = models.CharField(max_length=1000)
	duration = models.IntegerField()
	total_views = models.IntegerField(default=0)
	total_click = models.IntegerField(default=0)

	def set_tags(self, x):	##Store Tags In  JSON
		self.tags = json.dumps(x)

	def get_tags(self):		##Fetch Tags in JSON
		return json.loads(self.tags)

class ImageAd(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=12)	
	link = models.CharField(max_length=500)
	tags = models.CharField(max_length=1000)
	square_img = models.ImageField(upload_to = 'adImages')
	verticle_img = models.ImageField(upload_to = 'adImages')
	horizontal_img = models.ImageField(upload_to = 'adImages')
	duration = models.IntegerField()
	total_views = models.IntegerField(default=0)
	total_click = models.IntegerField(default=0)

	def set_tags(self, x):	##Store Tags In  JSON
		self.tags = json.dumps(x)

	def get_tags(self):		##Fetch Tags in JSON
		return json.loads(self.tags)

class Tags(models.Model):
	tag = models.CharField(max_length=20)
	textAd = models.ForeignKey(TextAd, on_delete=models.CASCADE,related_name="textAd", default= None, null=True, blank=True)
	imageAd = models.ForeignKey(ImageAd, on_delete=models.CASCADE,related_name="imageAd", default= None, null=True, blank=True)
	