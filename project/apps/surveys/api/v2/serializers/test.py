from rest_framework import serializers

from apps.surveys.models import Question, Answer
from apps.surveys.api.v1.serializers import SurveySerializer


class QuestionSerializer1(serializers.ModelSerializer):
    survey = SurveySerializer(required=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'survey')


class AnswerSerializer1(serializers.ModelSerializer):
    question = QuestionSerializer1(required=True)

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'is_correct', 'question')