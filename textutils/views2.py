# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    
    Pera = request.GET.get('Pera','default')
    Rpunc = request.GET.get('Rpunc','off')
    Upper = request.GET.get('Upper','off')
    Lower = request.GET.get('Lower','off')
    Capitalize = request.GET.get('Capitalize','off')
    Rnewline = request.GET.get('Rnewline','off')
    result = ""
    #REMOVE PUNTUATION
    punc='''!@#$%^&*()_+{}|:"?></.,';\][]~'''
    if Rpunc == 'on':
        for char in Pera:
            if char not in punc:
                result = result + char

        params = {'PURPOSE':"REMOVE PUNCTUATIONS",'before':Pera,'after':result}
        return render(request, 'analyze.html',params)
    #UPPERCASE
    elif (Upper == 'on'):
        for char in Pera:
            result = result + char.upper()
    
        params = {'PURPOSE':"UPPERCASE",'before':Pera,'after':result}
        return render(request, 'analyze.html',params)
    #LOWERCASE
    elif (Lower == "on"):
        for char in Pera:
            result = result + char.lower()
    
        params = {'PURPOSE':"LOWERCASE",'before':Pera,'after':result}
        return render(request, 'analyze.html',params)
    #R-NEWLINE
    elif (Rnewline=='on'):        
        result = ""
        for char in Pera:
            if char != "\n" and char !="\r":
                result = result + char
        params = {'PURPOSE':"Remove NewLine",'before':Pera,'after':result}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("ERROR")


