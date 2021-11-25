from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin,\
    DestroyModelMixin
from rest_framework.permissions import AllowAny

from drf_yasg2.utils import swagger_auto_schema


from apps.surveys.api.v2.serializers import SurveySerializer, SurveyUpdateSerializer
from apps.surveys.models import Survey
from apps.surveys.permissions import IsAuthenticatedAdmin


class SurveyViewSet(ListModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    RetrieveModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    action_serializers = {
        'create': SurveySerializer,
        'list': SurveySerializer,
        'retrieve': SurveyUpdateSerializer,
        'update': SurveyUpdateSerializer,
        'delete': SurveyUpdateSerializer,
    }

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'POST' or self.request.method == 'DELETE':
            return [IsAuthenticatedAdmin()]
        else:
            return [AllowAny()]

    @swagger_auto_schema(
        operation_description='Вернет все опросы.',
        operation_summary='Показать все опросы.',
    )
    def list(self, request, *args, **kwargs):
        return super(SurveyViewSet, self).list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Вернет опрос.',
        operation_summary='Покозать опрос.',
    )
    def retrieve(self, request, *args, **kwargs):
        return super(SurveyViewSet, self).retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Вернет созданный опрос.',
        operation_summary='Создать опрос.',
    )
    def create(self, request, *args, **kwargs):
        return super(SurveyViewSet, self).create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Вернет обновленный опрос.',
        operation_summary='Обновить опрос.',
    )
    def update(self, request, *args, **kwargs):
        return super(SurveyViewSet, self).update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Удалит опрос.',
        operation_summary='Удалить опрос.',
    )
    def destroy(self, request, *args, **kwargs):
        return super(SurveyViewSet, self).destroy(request, *args, **kwargs)

