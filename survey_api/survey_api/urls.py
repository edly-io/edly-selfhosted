"""
URLs for survey_api.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import SurveyFormAPI

urlpatterns = [
    re_path('api/survey-data', SurveyFormAPI.as_view(), name='survey-data'),
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="survey_api/base.html")),
]
