from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from models import Bubble
import json
import csv
import  pandas as pd


def bubble(request):
    data=pd.read_csv("data_visualize/all.csv")
    data=data.to_json(orient='records')
    return render(request,'bubbleMarket.html',{'data':data})


def candle(request):
    data=pd.read_csv("data_visualize/candlebtc.csv")
    data=data.to_json(orient='records')
    return render(request,'candle-brush.html',{'data':data})


def line(request):
    data=pd.read_csv("data_visualize/btc.csv")
    data=data.to_json(orient='records')
    return render(request,'btclinchart.html',{'data':data})

def index(request):
    data = pd.read_csv("data_visualize/btc.csv")
    data = data.to_json(orient='records')
    return render(request,'index.html',{'data':data})

def cf(request):
    data=pd.read_csv('data_visualize/cf1.csv')
    bitcoin=data.to_json(orient='records')
    return render(request,'crossfilter.html',{'bitcoin':bitcoin})
