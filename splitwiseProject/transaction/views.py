import inspect
import time

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Transaction
from user_group.models import User


# Create your views here.
# @method_decorator(ensure_csrf_cookie)
def createTransaction(request):
    if request.method == "GET":
        transactions = Transaction.objects.all().values()
        return JsonResponse(list(transactions), safe=False)

    if request.method == "POST":
        userid = int(request.POST['user'])
        amount = float(request.POST['amount'])
        owner = User.objects.get(pk=userid)
        Transaction.objects.create(owner=owner, amount=amount)

        return HttpResponse("Hello from POST " + inspect.stack()[0][3])


# @method_decorator(ensure_csrf_cookie)
def updateTransaction(request):
    if request.method == "POST":
        transactionid = int(request.POST['transactionid'])
        transaction = Transaction.objects.get(pk=transactionid)
        amount = transaction.amount
        transaction.amount = amount + 100
        time.sleep(0.005)
        transaction.save()

        return JsonResponse(serializers.serialize("json",[transaction,]), safe=False)

    if request.method == "GET":
        return HttpResponse("Hello from Get " + inspect.stack()[0][3])

def restoreTransaction(request):
    if request.method == "POST":
        transactionid = int(request.POST['transactionid'])
        transaction = Transaction.objects.get(pk=transactionid)
        amount = transaction.amount
        time.sleep(0.007)
        transaction.amount = amount - 100
        transaction.save()

        return JsonResponse(serializers.serialize("json",[transaction,]), safe=False)

    if request.method == "GET":
        return HttpResponse("Hello from Get " + inspect.stack()[0][3])

def resetTransaction(request):
    if request.method == "POST":
        transactionid = int(request.POST['transactionid'])
        transaction = Transaction.objects.get(pk=transactionid)
        amount = transaction.amount
        transaction.amount = 0
        transaction.save()

        return JsonResponse(serializers.serialize("json",[transaction,]), safe=False)

    if request.method == "GET":
        return HttpResponse("Hello from Get " + inspect.stack()[0][3])


# @method_decorator(ensure_csrf_cookie)
def getTransactions(request):
    if request.method == "POST":
        return HttpResponse("Hello from Post " + inspect.stack()[0][3])

    if request.method == "GET":
        return HttpResponse("Hello from Get " + inspect.stack()[0][3])
