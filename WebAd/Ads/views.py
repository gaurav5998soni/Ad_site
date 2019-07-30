from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse ,HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile, AdUnit, TextAd, ImageAd, Tags

def index(request):
	user = get_user(request)
	if user:
		return resolver(request,user)
	return render(request,'WebAd/index.html',{});

def signUp(request):
	if request.method == 'POST':
		u_name = request.POST['name']
		u_phone = request.POST['phone']
		u_email = request.POST['email']
		u_site = request.POST['site']
		u_pwd = request.POST['pwd']
		u_choice = request.POST['choice']

		if not validate(u_email):
			user = User.objects.create_user(username=u_email,email=u_email,password=u_pwd)
			print('User_created')
			user.first_name = u_name
			profile = Profile(user = user)
			profile.phone = u_phone
			profile.pri_site = u_site
			profile.ac_type = u_choice
			user.save()
			profile.save()
			return logIn(request)
	return redirect('index')
	
def logIn(request):
	if request.method == 'POST':
		u_email = request.POST['email']
		u_pass = request.POST['pwd']
		user = authenticate(username=u_email, password=u_pass)
		if user:
			request.session['sessionId'] = user.id
			return resolver(request,user)
	return redirect('index')


def logOut(request):				## function to logout a user and flush session
    try:
        request.session.flush();
    except KeyError:
        return HttpResponse('Error Occur While Logging You Out, Please Try Again')
    return redirect('index')


def resolver(request,user):
	profile = Profile.objects.get(user=user)
	if profile.ac_type:
		return redirect('/webMonetize/')
	else:
		return redirect('/adProvider/')	

def get_user(request):
	if 'sessionId' in request.session:
		return User.objects.get(id = request.session['sessionId']);
	return False;

def validate(mail):			
	mail_list = User.objects.values('email')
	for item in mail_list:
		if item['email'] == mail:
			return True;
	return False;

##############################################################	

def adServiceRedirect(request):
	adId  = request.GET['adId']
	adUnitId  = request.GET['adUnitId']

	unit = AdUnit.objects.get(id=adUnitId)
	unit.total_click += 1

	ad = TextAd.objects.get(id=adId)
	ad.total_click +=1

	unit.save()
	ad.save()

	return redirect(ad.link)

@api_view(['GET'])
def fetchTextAd(request):
	userId = request.GET['userId']
	adUnitId = request.GET['adUnitId']

	unit = AdUnit.objects.get(id=adUnitId)
	unit.total_views += 1
	tags = unit.get_tags();

	rnd = random.randint(0,len(tags)-1)
	tag = tags[rnd]
	print('------------> Showing Ad of ',tag)

	ads = Tags.objects.filter(tag=tag)

	if(len(ads) == 0):
		return Response({'text':'No Ads Available','id':'0'})

	rnd = random.randint(0,len(ads)-1)
	ad = ads[rnd]

	ad.textAd.total_views += 1

	ad.textAd.save()
	unit.save()

	ad_content = {
		'text' : ad.textAd.content,
		'id' : ad.textAd.id,
	}

	return Response(ad_content)	

##############################################################	