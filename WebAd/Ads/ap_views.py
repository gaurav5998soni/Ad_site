from .views import validate, get_user
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import Profile, AdUnit, TextAd, ImageAd, Tags

def ap_index(request):
	user = get_user(request)
	if user and is_user_valid(user):
		context = {
		"profile" : Profile.objects.get(user=user)
		}
		return render(request,'WebAd/provider/provider.html',context)
	return redirect('index')

class apAdd(View):
	def get(self,request):
		user = get_user(request)
		if user and is_user_valid(user):
			context = {
			"profile" : Profile.objects.get(user=user),
			'tags'	  :  ["food", "tavel", "eduction", "ecommerce", "trade", "game", "entertainment"],
			}
			return render(request,'WebAd/provider/addAd.html',context)
		return redirect('index')

	def post(self,request):
		user = get_user(request)
		if user and is_user_valid(user):
			ad_type = request.POST['ad_type']

			if ad_type == 'text':
				ad = TextAd()
				ad.user = user
				ad.name = request.POST['ad_name']
				ad.link = request.POST['ad_url']
				ad.content = request.POST['ad_text']
				ad.duration = request.POST['ad_duration']
				ad.set_tags(request.POST.getlist('ad_tags'))
				ad.save()

				#Save Tags
				tags = ad.get_tags()
				for tag in tags:
					t = Tags.objects.create(tag=tag,textAd=ad)
					t.save()
				return redirect('ap_manage')


			elif ad_type == 'image':
				ad = ImageAd()
				ad.user = user
				ad.name = request.POST['ad_name']
				ad.link = request.POST['ad_url']
				ad.duration = request.POST['ad_duration']

				ad.square_img = request.FILES['square']
				ad.verticle_img = request.FILES['verticle']
				ad.horizontal_img = request.FILES['horizontal']

				ad.set_tags(request.POST.getlist('ad_tags'))
				ad.save()

				#Save Tags
				tags = ad.get_tags()
				for tag in tags:
					t = Tags.objects.create(tag=tag,imageAd=ad)
					t.save()
				return redirect('ap_manage')

		return redirect('index')

class apEdit(View):
	def get(self,request):
		user = get_user(request)
		ad_id = request.GET['adId']
		ad_type = request.GET['type']
		ad = TextAd.objects.get(id=ad_id)

		if user and is_user_valid(user) and ad.user == user:
			if ad_type == 'text' :
				ad = TextAd.objects.get(id=ad_id)
				profile = Profile.objects.get(user=user)
			context = {
				'type': ad_type,
				'ad' : ad,
				'profile' : profile,
				'tags': ["food", "tavel", "eduction", "ecommerce", "trade", "game", "entertainment"]
			}
			return render(request,'WebAd/provider/editAd.html',context)
		return redirect('index')

	def post(self,request):
		user = get_user(request)
		ad_id = request.POST['adId']
		ad_type = request.POST['type']
		ad = TextAd.objects.get(id=ad_id)

		if user and is_user_valid(user) and ad.user == user:
			if ad_type == 'text':
				ad = TextAd.objects.get(id=ad_id)
				ad.name = request.POST['ad_name']
				ad.link = request.POST['ad_url']
				ad.content = request.POST['ad_text']
				ad.set_tags(request.POST.getlist('ad_tags'))
				ad.save()
				return redirect('ap_manage')
			return redirect('index')

def ap_manage(request):
	user = get_user(request)
	if user and is_user_valid(user):
		textAds = TextAd.objects.filter(user=user) 
		context = {
		"profile" : Profile.objects.get(user=user),
		'textAds' : textAds,
		}
		return render(request,'WebAd/provider/manage.html',context)
	return redirect('index')

def ap_setting(request):
	user = get_user(request)
	if user and is_user_valid(user):
		context = {
		"profile" : Profile.objects.get(user=user)
		}
		return render(request,'WebAd/provider/setting.html',context)
	return redirect('index')

def ap_transaction(request):
	user = get_user(request)
	if user and is_user_valid(user):
		context = {
		"profile" : Profile.objects.get(user=user)
		}
		return render(request,'WebAd/provider/payment.html',context)
	return redirect('index')

def is_user_valid(user):
	profile = Profile.objects.get(user=user)
	if profile.ac_type:
		return False
	return True		