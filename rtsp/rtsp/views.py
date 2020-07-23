
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from os import path as p
@csrf_exempt
def source_view(request):
    print("Method: " + request.method)
    if (len(request.FILES) > 0):
        print("there are files:" + ";".join(str(key) for key in request.FILES))
    if (len(request.COOKIES) > 0):
        print("there are cookies:" + ";".join(str(key) for key in request.FILES))
    print ("body lenght: " + str(len(request.body)))

    print("headers:")
    print(request.META)
    
    return HttpResponse(200)