from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from models import Bubble
import json
import csv
import  pandas as pd


def bubble(request):
    data=pd.read_csv("data_visualize/data/bubble.csv")
    data=data.to_json(orient='records')
    return render(request,'bubbleMarket.html',{'data':data})


def candle(request):
    data=pd.read_csv("data_visualize/data/candlebtc.csv")
    data=data.to_json(orient='records')
    return render(request,'candle-brush.html',{'data':data})


def line(request):
    data=pd.read_csv("data_visualize/data/btc.csv")
    data=data.to_json(orient='records')
    return render(request,'btclinchart.html',{'data':data})

def index(request):
    data = pd.read_csv("data_visualize/data/btc.csv")
    data = data.to_json(orient='records')
    return render(request,'index.html',{'data':data})

def cf(request):
    data=pd.read_csv('data_visualize/data/crossfilter.csv')
    bitcoin=data.to_json(orient='records')
    return render(request,'crossfilter.html',{'bitcoin':bitcoin})


def sentiment(request):
    data=pd.read_csv('data_visualize/data/senti.csv')
    data=data.to_json(orient='records')
    return render(request,'sentiment.html',{'data':data})


def sentiline(request):
    data=pd.read_csv('data_visualize/data/sentiline.csv')
    data=data.to_json(orient='records')
    return render(request,'sentiline.html',{'data':data})


def prediction(request):
    data=pd.read_csv('data_visualize/data/prediction/RNN_bitcoin.csv')
    data=data.to_json(orient='records')
    return render(request,'prediction.html',{'data':data})


def coin(request):
    if request.method=='POST':
        coin_name=request.POST.get('coin_name')
        data=None
        if coin_name=='bitcoin':
            data=pd.read_csv('data_visualize/data/prediction/RNN_bitcoin.csv')
        elif coin_name=='ethereum':
            data = pd.read_csv('data_visualize/data/prediction/RNN_ethereum.csv')
        elif coin_name=='monero':
            data=pd.read_csv('data_visualize/data/prediction/RNN_monero.csv')
        elif coin_name=='litecoin':
            data=pd.read_csv('data_visualize/data/prediction/RNN_litecoin.csv')
        elif coin_name=='dash':
            data=pd.read_csv('data_visualize/data/prediction/RNN_dash.csv')
        elif coin_name=='bitcoincash':
            data=pd.read_csv('data_visualize/data/prediction/RNN_bitcoin-cash.csv')
        elif coin_name=='eos':
            data=pd.read_csv('data_visualize/data/prediction/RNN_eos.csv')
        elif coin_name=='neo':
            data=pd.read_csv('data_visualize/data/prediction/RNN_neo.csv')
        elif coin_name=='nano':
            data=pd.read_csv('data_visualize/data/prediction/RNN_nano.csv')
        elif coin_name=='iota':
            data=pd.read_csv('data_visualize/data/prediction/RNN_iota.csv')


        data=data.to_json(orient='records')
        print coin_name
        return HttpResponse(data)