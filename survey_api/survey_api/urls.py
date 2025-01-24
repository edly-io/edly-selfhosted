"""
URLs for survey_api.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import OnboardingSurveyAPI

urlpatterns = [
    re_path('api/onboarding-survey', OnboardingSurveyAPI.as_view(), name='onboarding-survey'),
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="survey_api/base.html")),
]
