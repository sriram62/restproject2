from django.shortcuts import render
from django.views import View
from restapp2.serializers import CustSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
class Cust:
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
class Home(View):
    def get(self,request):
        c1=Cust('scott','mumbai',1001,100000.00)
        c2=Cust('blake','banglore',1002,10000.00)
        c3=Cust('smith','hyderabad',1003,1000.00)
        custs=[c1,c2,c3]
        cs1=CustSerializer(custs,many=True)
        data=JSONRenderer().render(cs1.data)
        return HttpResponse(data,content_type='application/json')