"""
URLs for survey_api.
"""

from django.urls import re_path
from .views import OnboardingSurveyAPI

urlpatterns = [
    re_path(
        r"^api/onboarding-survey/$",
        OnboardingSurveyAPI.as_view(),
        name="onboarding-survey",
    ),
]
