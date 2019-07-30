from django.urls import path, include
from . import views, ap_views

urlpatterns = [
	path('',ap_views.ap_index,name="ap_index"),
	path('addAd',ap_views.apAdd.as_view(),name="ap_add"),
	path('editAd',ap_views.apEdit.as_view(),name="ap_edit"),
	path('manageAd',ap_views.ap_manage,name="ap_manage"),
	path('setting',ap_views.ap_setting,name="ap_setting"),
	path('transaction',ap_views.ap_transaction,name="ap_transaction"),
]