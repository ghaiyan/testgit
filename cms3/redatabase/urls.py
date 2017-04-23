from django.conf.urls import url,include
from django.contrib import admin
from redatabase import views

urlpatterns = [
                        url(r'^$', views.login, name='login'),
                        url(r'^login/$',views.login,name = 'login'),
                        url(r'^regist/$',views.regist,name = 'regist'),
                        url(r'^index/$',views.index,name = 'index'),
                        url(r'^logout/$',views.logout,name = 'logout'),
                        url(r'^About/$', views.About, name='About'),
                        url(r'^changePW/$', views.changePW, name='changePW'),
                        url(r'^nan/search/$', views.search, name='search'),
                        url(r'^nan/CompSearch/$', views.CompSearch, name='CompSearch'),
                        url(r'^nan/deleteFormulaData/$', views.deleteFormulaData, name='deleteFormulaData'),
                        url(r'^nan/insertFormulaData/$', views.insertFormulaData, name='insertFormulaData'),
                        url(r'^nan/ViewData/$', views.ViewData, name='ViewData'),
                        url(r'^nan/ViewData/Formula/$', views.Formula, name='Formula'),
                        url(r'^nan/ViewData/materialsData/$', views.materialsData, name='materialsData'),
                        url(r'^nan/ViewData/conductivity/$', views.conductivity, name='conductivity'),
                        url(r'^nan/ViewData/cp/$', views.cp, name='cp'),
                        url(r'^nan/ViewData/resistivity/$', views.resistivity, name='resistivity'),
                        url(r'^nan/ViewData/tec/$', views.tec, name='tec'),
                        url(r'^About2/$', views.About2, name='About2'),
                        url(r'^top/$', views.top, name='top'),
]