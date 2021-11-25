import functools

from rest_framework.exceptions import ValidationError

from apps.surveys.models import Question, Answer, Survey


def get_survey_decorator(view_method):
    @functools.wraps(view_method)
    def wrapper(self):
        try:
            survey = Survey.objects.get(id=self.kwargs['pk'])
            return view_method(self)
        except Exception as e:
            raise ValidationError(detail={'status': "Survey not found!"})
    return wrapper
