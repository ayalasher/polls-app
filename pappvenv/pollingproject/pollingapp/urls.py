from django.urls import path
from . import views

urlpatterns =[
    path('',views.greeting , name="greeting" ),
    path('<int:question_id>/',views.details , name="details" ),
    path('<int:question_id>/', views.results , name="results"  ),
    path('<int:question_id>/',views.vote, name="vote" )
]