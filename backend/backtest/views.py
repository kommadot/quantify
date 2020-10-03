from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
from .Backtest import Backtest
import pandas as pd
# Create your views here.
@permission_classes((AllowAny,))
class BackTestView(APIView):
    def post(self,request):
        data = request.data
        backtest = Backtest(data['start'],data['end'],1,data['budget'],data['rebalance'])

        df = backtest.run()

        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='raise')

        # stock_price = price.get_price(code)
        # price_json = {'code':code,'price':int(stock_price.replace(",",""))}
        return Response(df.to_json(orient="values",date_format="iso"),status=status.HTTP_200_OK)