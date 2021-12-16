from django.urls import path
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path("signup/", views.SignUp.as_view(), name="signup"),
	path("about/",views.about, name="about"),
	path("contact/",views.contact, name="contact"),
    path('success/', views.successView, name='success'),
	path('view/<int:id>/',views.productdetail, name='productdetail')
]