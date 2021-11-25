from django.urls import path

from rest_framework.routers import DefaultRouter

from apps.surveys.api.v2 import views

router = DefaultRouter()
router.register(r'surveys', views.SurveyViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

urlpatterns = []
urlpatterns += router.urls
