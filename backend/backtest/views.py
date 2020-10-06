from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
import json
from .Backtest import Backtest
import pandas as pd
from .models import BacktestModel,BacktestDate,Log
from .serializers import BacktestModelSerializer
import ast
from django.forms.models import model_to_dict
from django.core.cache import cache
# Create your views here.
@permission_classes((AllowAny,))
class BackTestView(APIView):
    def post(self,request):

        data = request.data
        backtest = Backtest(data['start'],data['end'],data['strategy'],data['budget'],data['rebalance'])

        df,logs = backtest.run()
        
        df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='raise')
        test_data = df.to_json(orient="values",date_format="iso")
        strategy = data["strategy"]
        log_array = []
        btm = BacktestModel()
        # btm = BacktestModel(user=request.user)
        btm.strategy = strategy
        for row in logs:
            log = {"date":row['date'],"types":row['types'],"datas":row['datas']}
            log_array.append(log)
        btm.log = log_array
        data_array = []
        test_data = ast.literal_eval(test_data)
        for row in test_data:
            data = {"date":row[0],"budget":row[1]}
            data_array.append(data)
        
        btm.data = data_array
        btm.save()

        return Response({"strategy":strategy,"datas":data_array,"logs":logs},status=status.HTTP_200_OK)

    
    def get(self,request):
        test_datas = cache.get("backtests")
        if not test_datas:
            test_datas = BacktestModel.objects.all()
            cache.set("backtests",test_datas)
        test_list = []
        for i in test_datas:
            test_list.append({"strategy":i.strategy,"datas":i.data,"logs":i.log})

        return Response(test_list)