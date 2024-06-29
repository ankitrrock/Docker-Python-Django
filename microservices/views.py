from django.shortcuts import redirect
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def my_redirect_view_1(request):
    # Your view logic here
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Connection successful:", result)
    except Exception as e:
        print("Connection error:", e)
        return HttpResponse(str(e))
    return HttpResponse(str(result))

def my_redirect_view_2(request):
    # Your view logic here
    return HttpResponse("Hello world!")
