from rest_framework import generics
from rest_framework.response import Response

from apps.surveys.api.v1.serializers import SurveySerializer, SurveyUpdateSerializer
from apps.surveys.models import Survey


class SurveyView(generics.ListCreateAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()


class SurveyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveyUpdateSerializer
    queryset = Survey.objects.all()
