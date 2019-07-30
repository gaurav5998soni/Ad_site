from django.urls import path, include
from . import views, wm_views

urlpatterns = [
	path('',wm_views.wm_index,name="wm_index"),
	path('addAd',wm_views.WmAdd.as_view(),name="wm_add"),
	path('editAd',wm_views.WmEdit.as_view(),name="wm_edit"),
	path('manageAd',wm_views.wm_manage,name="wm_manage"),
	path('setting',wm_views.wm_setting,name="wm_setting"),
	path('transaction',wm_views.wm_transaction,name="wm_transaction"),
	path('viewCode',wm_views.wm_viewCode,name="viewCode"),
]