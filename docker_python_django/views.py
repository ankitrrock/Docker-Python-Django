from django.shortcuts import redirect

def my_redirect_view_main1(request):
    # Your view logic here
    return redirect('/some-url/')

def my_redirect_view_main2(request):
    # Your view logic here
    return redirect('/another-url/')
