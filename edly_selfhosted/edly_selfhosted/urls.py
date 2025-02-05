"""
URLs for edly_selfhosted.
"""

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r"^api/onboarding-survey/$",
        views.OnboardingSurveyAPI.as_view(),
        name="onboarding-survey",
    ),
]
