from rest_framework import serializers

from apps.surveys.models import Question, Answer
from apps.surveys.api.v1.serializers import SurveySerializer


class QuestionSerializer(serializers.ModelSerializer):
    # survey = SurveySerializer(required=False)

    class Meta:
        model = Question
        fields = ('id', 'question',)


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'is_correct',)