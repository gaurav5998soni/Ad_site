from .views import validate, get_user
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import Profile, AdUnit, TextAd, ImageAd, Tags

def wm_index(request):
	user = get_user(request)
	if user and is_user_valid(user):
		context = profile_details(user)
		return render(request,'WebAd/website/index.html',context)
	return redirect('index')


class WmEdit(View):
	def get(self,request):
		user = get_user(request)
		if user and is_user_valid(user):
			unit = AdUnit.objects.get(id=request.GET['adId'])
			profile = Profile.objects.get(user=user)

			if unit.user != user:
				return redirect('wm_manage')
			
			context = {
				'unit' : unit,
				'profile' : profile,
				'tags': ["food", "tavel", "eduction", "ecommerce", "trade", "game", "entertainment"]
			}
			return render(request,'WebAd/website/editAd.html',context)
		return redirect('index')

	def post(self,request):
		user = get_user(request)
		adUnitId = request.POST['adUnitId']
		if user and is_user_valid(user):
			unit = AdUnit.objects.get(id=adUnitid)
			if unit.user != user:
				return redirect('wm_manage')
			unit.name = request.POST['ad_name']
			unit.website = request.POST['site_url']
			unit.ad_type = request.POST['ad_type']
			unit.ad_shape = request.POST['ad_shape']
			unit.ad_alternate = request.POST['ad_alternate']
			unit.set_tags(request.POST.getlist('ad_tags'))
			unit.save()			
			context = profile_details(user)
			return render(request,'WebAd/website/addAd.html',context)

def wm_manage(request):
	user = get_user(request)
	if user and is_user_valid(user):
		units = AdUnit.objects.filter(user=user)
		context = {
		'units' : units,
		'profile' : Profile.objects.get(user=user),
		}
		return render(request,'WebAd/website/manage.html',context)

def wm_setting(request):
	user = get_user(request)
	if user and is_user_valid(user):
		context = profile_details(user)
		return render(request,'WebAd/website/setting.html',context)
	return redirect('index')

def wm_transaction(request):
	user = get_user(request)
	if user and is_user_valid(user):
		context = profile_details(user)
		return render(request,'WebAd/website/payment.html',context)
	return redirect('index')

def is_user_valid(user):
	profile = Profile.objects.get(user=user)
	if profile.ac_type:
		return True
	return False	

def profile_details(user):
	profile = Profile.objects.get(user = user);
	details = {
		'profile' : profile, 
	}
	return details;


class WmAdd(View):
	def get(self,request):
		user = get_user(request)
		if user and is_user_valid(user):
			context = profile_details(user)
			return render(request,'WebAd/website/addAd.html',context)
		return redirect('index')

	def post(self,request):
		user = get_user(request)
		if user and is_user_valid(user):
			unit = AdUnit.objects.create(user = user)
			unit.name = request.POST['ad_name']
			unit.website = request.POST['site_url']
			unit.ad_type = request.POST['ad_type']
			unit.ad_shape = request.POST['ad_shape']
			unit.ad_alternate = request.POST['ad_alternate']
			unit.set_tags(request.POST.getlist('ad_tags'))
			unit.save()			
			context = profile_details(user)
			return render(request,'WebAd/website/addAd.html',context)

def wm_viewCode(request):
	user = get_user(request)
	if user and is_user_valid(user):
		unit = AdUnit.objects.get(id=request.GET['adUnitId'])		
		if unit.user != user:
				return redirect('wm_manage')
		profile = Profile.objects.get(user=user)
		context = {
		'unit':unit,
		'profile':profile,
		}
		return render(request,'WebAd/website/viewCode.html',context)
	return redirect('index')
