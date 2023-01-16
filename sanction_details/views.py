from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import SanctionLetters, SanctionDetails, TrnDetails
from .serializers import  SanctionDetailsSerializer, SanctionLettersSerializer, TrnDetailsSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone



@api_view(['GET','POST'])
def get_trn_details(request):
    data = {}
    if request.method == 'GET':
        queryset = TrnDetails.objects.all()
        data_serializer = TrnDetailsSerializer(queryset, many=True)
        print(data)
        # print(request.data.get())    
        return Response(data_serializer.data)

    elif request.method == 'POST':
        
        data = {
            'customer_name': request.data.get('customer_name'), 
            'customer_address': request.data.get('customer_address'), 
            'customer_email_id': request.data.get('customer_email_id'), 
            'customer_num': request.data.get('customer_num'), 
            'trn_time': request.data.get('trn_time'), 
            'product_name': request.data.get('product_name'), 
            'product_price': request.data.get('product_price'), 
            'product_quantity': request.data.get('product_quantity'), 
            'product_amount': request.data.get('product_amount'), 
            'trn_type': request.data.get('trn_type'), 
            'additional_details': request.data.get('additional_details'), 
        }
        # print(data)
        # print(request.data.get())
        serializer = TrnDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

