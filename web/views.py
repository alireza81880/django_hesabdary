import datetime
from json import JSONEncoder
import token
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User,Token,Expense,Income
# Create your views here.

@csrf_exempt
def submit_income(request):
    #return render(request,'submit_expense.html')
    #TODO: validate data. user migh be fake, token might be fake, amount might be ...
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    if 'date' in request.POST:

        date=datetime.datetime.now() 
    Income.objects.create(User=this_user,amount=request.POST['amount'],
        text=request.POST['text'],data=date)

        
    print("I 'm in submit expense'")
    print (request.POSt)


    return JsonResponse({
        'status':'ok',
        
    },encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):
    #return render(request,'submit_expense.html')
    #TODO: validate data. user migh be fake, token might be fake, amount might be ...
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    if 'date' in request.POST:

        date=datetime.datetime.now() 
    Expense.objects.create(User=this_user,amount=request.POST['amount'],
        text=request.POST['text'],data=date)
    print("I 'm in submit expense'")
    print (request.POSt)


    return JsonResponse({
        'status':'ok',
        
    },encoder=JSONEncoder)