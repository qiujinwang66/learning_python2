
from django.http import HttpResponse

def index(request):
    return HttpResponse("龙腾测试！！！ <a href='/navigation/about'>关于</a>")

def about(request):
    return HttpResponse("龙腾测试！！！ <a href='/navigation/index'>首页</a>")