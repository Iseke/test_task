from rest_framework import generics, status
from rest_framework.exceptions import ValidationError

from apps.surveys.api.v1.serializers import QuestionSerializer, AnswerSerializer
from apps.surveys.models import Question, Answer, Survey
from apps.surveys.decorators import get_survey_decorator


def get_survey(idd: int):
    try:
        survey = Survey.objects.get(id=idd)
    except Survey.DoesNotExist:
        raise ValidationError({"status": "Survey not found!"})
    return survey


def get_question(idd: int):
    try:
        question = Question.objects.get(id=idd)
    except Question.DoesNotExist:
        raise ValidationError({"status": "Question not found!"})
    return question


def get_answer(idd: int):
    try:
        answer = Answer.objects.get(id=idd)
    except Answer.DoesNotExist:
        raise ValidationError({"status": "Answer not found!"})
    return answer


class QuestionView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        survey = get_survey(idd=self.kwargs['pk'])
        return Question.objects.filter(survey=survey, )

    def perform_create(self, serializer):
        survey = get_survey(idd=self.kwargs['pk'])
        serializer.save(survey=survey)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        get_survey(idd=self.kwargs['pk'])
        question = get_question(idd=self.kwargs['pk1'])
        return question


class AnswerView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        get_survey(idd=self.kwargs['pk'])
        question = get_question(idd=self.kwargs['pk1'])
        return Answer.objects.filter(question=question)

    def perform_create(self, serializer):
        get_survey(idd=self.kwargs['pk'])
        question = get_question(idd=self.kwargs['pk1'])
        serializer.save(question=question)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer

    def get_object(self):
        get_survey(idd=self.kwargs['pk'])
        get_question(idd=self.kwargs['pk1'])
        answer = get_answer(idd=self.kwargs['pk2'])
        return answer
