from django.shortcuts import render
import random


# Create your views here.

def Home(request):
    return render(request, 'home.html')


def Result(request):
    length = int(request.GET.get('length', 8))
    character = list('abcdefghijklmnopqrstuvwxyz')
    randpassowrd = ''
    if request.GET.get('uppercase'):
        character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        character.extend('0123456789')
    if request.GET.get('specialChar'):
        character.extend('~`!@#$%^&*()_-+=><?/|}{][')

    for i in range(length):
        randpassowrd += random.choice(character)

    return render(request, 'result.html', {'newspassword': randpassowrd})
