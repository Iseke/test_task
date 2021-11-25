from django.urls import path

from apps.surveys.api.v1 import views

urlpatterns = [
    path('', views.SurveyView.as_view()),
    path('<int:pk>/', views.SurveyDetailView.as_view()),
    path('<int:pk>/questions/', views.QuestionView.as_view()),
    path('<int:pk>/questions/<int:pk1>/', views.QuestionDetailView.as_view()),
    path('<int:pk>/questions/<int:pk1>/answers/', views.AnswerView.as_view()),
    path('<int:pk>/questions/<int:pk1>/answers/<int:pk2>/', views.AnswerDetailView.as_view())
]