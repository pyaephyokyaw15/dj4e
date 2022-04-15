from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def myview(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('view_count', 1)
    resp = HttpResponse('view_count= ' + str(oldval))
    if oldval:
        resp.set_cookie('view_count', int(oldval) + 1)  # No expired date = until browser close

    resp.set_cookie('dj4e_cookie', 'eaebf0b6', max_age=1000)  # seconds until expire
    return resp
