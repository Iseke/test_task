# from rest_framework import serializers
#
# from apps.surveys.models import Survey
#
#
# class SurveySerializer(serializers.ModelSerializer):
#     start_date = serializers.DateField(required=False)
#
#     class Meta:
#         model = Survey
#         fields = ('id', 'name', 'start_date', 'end_date', 'description', 'created_at', 'updated_at')
#         extra_kwargs = {
#             'created_at': {
#                 'read_only': True
#             },
#             'updated_at': {
#                 'read_only': True
#             }
#         }
#
#
# class SurveyUpdateSerializer(SurveySerializer):
#     start_date = serializers.DateField(read_only=True)
#
#     class Meta(SurveySerializer.Meta):
#         model = SurveySerializer.Meta.model
#         fields = SurveySerializer.Meta.fields
