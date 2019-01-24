from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #Return a rendered response to send to the client.
    #The first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # Construct a dictionary to pass the template engine as its context.
    context_dict = {}
    
    #Return a rendered response to send to the client.
    #The first parameter is the template we wish to use
    return render(request, 'rango/about.html', context=context_dict)
