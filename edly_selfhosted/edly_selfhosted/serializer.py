from rest_framework import serializers


class OnboardingSurveySerializers(serializers.Serializer):
    form_filled = serializers.BooleanField()
    load_form = serializers.BooleanField()

