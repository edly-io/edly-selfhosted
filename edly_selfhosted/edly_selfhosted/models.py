from django.db import models


class OnboardingSurvey(models.Model):
    # Indicates whether the user has completed the onboarding form
    form_filled = models.BooleanField(default=False)
    
    # Flag to control whether the form should be automatically loaded on the frontend
    auto_load_form = models.BooleanField(default=True)
