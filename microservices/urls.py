from django.urls import path
from microservices import views as test



urlpatterns = [
	path('registerPage/', view=test.my_redirect_view_1, name="registerPage"),
	path('loginPage/', view=test.my_redirect_view_2, name="loginPage"),

]