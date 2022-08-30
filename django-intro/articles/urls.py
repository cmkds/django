from django.urls import path
from . import views

#ariticles/urls.py

urlpatterns = [
    ###뒤에다가 쉼표 붙히는 거는 파이썬에서 좋아하는 습관.
    path('index/', views.index, name='index'),  
    ## 인덱스로 접근 했을때 이페이지 뜨도록 만든것.
    path('dtl/', views.dtl, name='dtl'),
    # views에 dtl 이란거에 접근 할거야. 
    path('greeting/', views.greeting),

    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch),
    
    #꺽쇠로 Variable routing 에 대한 변수를 집어 넣는다.
    path('hello/<str:name>/', views.hello),
]

