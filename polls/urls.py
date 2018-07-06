from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.number_one, name='number_one'),

    path('sayhi', views.sayHi, name='index'),
    path('iitr', views.iitr, name='index'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
           ]
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]