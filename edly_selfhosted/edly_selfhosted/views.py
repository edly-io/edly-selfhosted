from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import OnboardingSurvey
from .serializer import OnboardingSurveySerializers


class OnboardingSurveyAPI(APIView):
    """
    Return information that tells the frontend to display the onboarding survey (or not).

    The form is displayed only for a single admin user, and only once. If they dismiss
    or submit the survey, it is not displayed anymore. It is the responsibility of the
    frontend to display the form and to cache backend responses.
    """

    permission_classes = [IsAdminUser]

    def get(self, request):
        onboarding_survey = OnboardingSurvey.objects.last()
        show_form = not (onboarding_survey and onboarding_survey.form_filled)
        load_form = onboarding_survey and onboarding_survey.load_form
        response = Response(
            {
                "username": request.user.username,
                "email": request.user.email,
                "show_form": show_form,
                "load_form": load_form
            }
        )

        return response

    def post(self, request):
        """
        Create an OnboardingSurvey singleton, such that
        """
        serializer = OnboardingSurveySerializers(data=request.data)

        if serializer.is_valid():
            form_filled = serializer.validated_data["form_filled"]
            load_form = serializer.validated_data["load_form"]
            onboarding_survey = OnboardingSurvey.objects.last()
            if not onboarding_survey:
                OnboardingSurvey.objects.create(
                    form_filled=form_filled,
                    load_form=load_form
                )
            else:
                onboarding_survey.form_filled = form_filled
                onboarding_survey.load_form = load_form
                onboarding_survey.save()
            return Response(
                {"message": "Edly form status updated successfully."},
                status=HTTP_200_OK,
            )

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
