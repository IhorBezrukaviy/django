from django.urls import path
from .views import *
urlpatterns=[
	path('', ArticleList.as_view(),name='home'),
	path('article/<int:pk>',ArticleDetailView.as_view(),name='detail')

]