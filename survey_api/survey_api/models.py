from django.db import models


class OnboardingSurvey(models.Model):
    form_filled = models.BooleanField(default=False)
