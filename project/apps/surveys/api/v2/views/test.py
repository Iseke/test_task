from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from apps.surveys.api.v2.serializers import QuestionSerializer1, AnswerSerializer1
from apps.surveys.models import Question, Answer


class QuestionViewSet(GenericViewSet,
                      ListModelMixin,
                      CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer1


class AnswerViewSet(GenericViewSet,
                    ListModelMixin,
                    CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer1

