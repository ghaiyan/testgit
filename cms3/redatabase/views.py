from django.shortcuts import render

# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from redatabase.models import  User
from redatabase.models import users,smcoinformation,materialsinformation,info_conductivity,info_cp
from redatabase.models import info_resistivity,info_tec
from django.core.paginator import Paginator
#表单
class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())


#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, )

#登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/redatabase/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/redatabase/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},)

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

def About(req):
    return render_to_response('About.html')
def changePW(req):
    return render_to_response('changePW.html')


def About2(req):
    return render_to_response('About2.html')
def top(req):
    return render_to_response('top.html')
def ViewData(req):
    return render_to_response('ViewData.html')
def Formula(req):
    limit = 1  # 限制每一页显示的条目数量
    smoinfo = smcoinformation.objects
    paginator = Paginator(smoinfo, limit)
    page_num = req.GET.get('page', 1)  # 从url中获取页码参数
    loaded = paginator.page(page_num)
    context = {
        "smcoinformation": loaded
    }
    return render(req,'Formula.html', context)

def insertFormulaData(request):
    if request.method == 'POST':
        #update field values and save to mongo
        Formula=request.POST['Formula']
        Grainsize = request.POST['Grainsize']
        Latticeparameters = request.POST['Latticeparameters']
        Crystalstructure = request.POST['Crystalstructure']
        Phasetransformationtemperature = request.POST['Phasetransformationtemperature']
        Debyetemperature = request.POST['Debyetemperature']
        Curietemperature = request.POST['Curietemperature']
        Heatcapacity = request.POST['Heatcapacity']
        Thermalexpansioncoefficient = request.POST['Thermalexpansioncoefficient']
        Elasticmodulus = request.POST['Elasticmodulus']
        Saturationmagnetization = request.POST['Saturationmagnetization']
        Remanence = request.POST['Remanence']
        Coercivity = request.POST['Coercivity']
        max = request.POST['max']
        smoinfo=smcoinformation(Formula=Formula)
        smoinfo.Grainsize=Grainsize
        smoinfo.Latticeparameters = Latticeparameters
        smoinfo.Crystalstructure = Crystalstructure
        smoinfo.Phasetransformationtemperature = Phasetransformationtemperature
        smoinfo.Debyetemperature = Debyetemperature
        smoinfo.Curietemperature = Curietemperature
        smoinfo.Heatcapacity =Heatcapacity
        smoinfo.Thermalexpansioncoefficient =Thermalexpansioncoefficient
        smoinfo.Elasticmodulus = Elasticmodulus
        smoinfo.Saturationmagnetization = Saturationmagnetization
        smoinfo.Remanence =Remanence
        smoinfo.Coercivity = Coercivity
        smoinfo.max = max
        smoinfo.save()
    smcoinformations=smcoinformation.objects
    context={'smcoinformations': smcoinformation.objects}
    return render(request,'insertFormulaData.html',context )

def deleteFormulaData(request):
    if request.method == 'POST':
        id=request.POST['id']
        smcoinfo=smcoinformation.objects(id=id)[0]
        smcoinfo.delete()
        template='Formula.html'
        params={'smcoinformations':smcoinformation.objects}
    elif request.method == 'GET':
        id = request.POST['id']
        template ='deleteFormulaData.html'
        params ={'id':id}
    return render(request,template,params)
def conductivity(req):
    #limit = 1  # 限制每一页显示的条目数量
    conductivityinfo = info_conductivity.objects[:]

    #paginator = Paginator(conductivityinfo, limit)
    #page_num = req.GET.get('page', 1)  # 从url中获取页码参数
    #loaded = paginator.page(page_num)

    context = {
        "info_conductivity":conductivityinfo
    }
    return render(req,'conductivity.html', context)
def cp(req):
    cpinfo = info_cp.objects[:]
    context = {
        "info_cp":cpinfo
    }
    return render(req,'cp.html', context)
def resistivity(req):
    resistivityinfo = info_resistivity.objects[:]
    context = {
        "info_resistivity":resistivityinfo
    }
    return render(req,'resistivity.html', context)
def tec(req):
    tecinfo = info_tec.objects[:]
    context = {
        "info_tec":tecinfo
    }
    return render(req,'tec.html', context)

def materialsData(req):
    limit = 1  # 限制每一页显示的条目数量
    materialsinfo = materialsinformation.objects
    paginator = Paginator(materialsinfo, limit)
    page_num = req.GET.get('page', 1)  # 从url中获取页码参数
    loaded = paginator.page(page_num)
    context = {
        "materialsinformation": loaded
    }
    return render(req,'materialsData.html', context)
def About(req):
    return render_to_response('About.html')


def search(req):
    materialsinfo = materialsinformation.objects
    context = {
        "materialsinformation": materialsinfo
    }
    return render(req, 'search.html', context)

def CompSearch(req):
    return render_to_response('CompSearch.html')
