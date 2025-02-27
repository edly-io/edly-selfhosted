from rest_framework import serializers


class OnboardingSurveySerializers(serializers.Serializer):
    form_filled = serializers.BooleanField()
    auto_load_form = serializers.BooleanField()

