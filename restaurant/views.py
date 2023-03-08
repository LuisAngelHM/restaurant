from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request, day):
    menu = {
        "lunes": ["Sopal", "Carnel", "Verdurasl"],
        "martes": ["Sopam", "Carnem", "Verdurasm"],
        "miercoles": ["Sopam", "Carnem", "Verdurasm"],
        "jueves": ["Sopaj", "Carnej", "Verdurasj"],
        "viernes": ["Sopav", "Carnev", "Verdurasv"],
    }
    try: 
        response = {"menu": menu[day]}
        return JsonResponse(response)

    except Exception as error: 
        print(error)
        response = { "message": error, "code": 500}
        return JsonResponse(response)

def menuEspecial(request): 
    menuEspecial = {
        "LunesEsp": ["Sopa", "Carne", "Verduras"],
        "MartesEsp": ["Sopa", "Carne", "Verduras"],
        "MiercolesEsp": ["Sopa", "Carne", "Verduras"],
        "JuevesEsp": ["Sopa", "Carne", "Verduras"],
        "ViernesEsp": ["Sopa", "Carne", "Verduras"],
    }

    return JsonResponse(menuEspecial)