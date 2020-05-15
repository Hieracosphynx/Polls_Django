from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # index(/polls/)
    path('', views.IndexView.as_view(), name='index'),
    # details(/polls/#)
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # result(/polls/#/results)
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # vote(/polls/#/vote)
    path('<int:question_id>/vote/', views.vote, name='vote'),
]