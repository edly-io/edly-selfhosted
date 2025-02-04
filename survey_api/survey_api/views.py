from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import OnboardingSurvey
from .serializer import OnboardingSurveySerializers


class OnboardingSurveyAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        onboarding_survey = OnboardingSurvey.objects.last()

        show_form = not (onboarding_survey and onboarding_survey.form_filled)

        response = Response(
            {
                "username": request.user.username,
                "email": request.user.email,
                "show_form": show_form,
            }
        )

        return response

    def post(self, request):
        serializer = OnboardingSurveySerializers(data=request.data)

        if serializer.is_valid():
            form_filled = serializer.validated_data["form_filled"]
            onboarding_survey = OnboardingSurvey.objects.last()

            if not onboarding_survey:
                onboarding_survey = OnboardingSurvey.objects.create(
                    form_filled=form_filled
                )
            else:
                onboarding_survey.form_filled = form_filled
                onboarding_survey.save()
            return Response(
                {"message": "Form status updated successfully."}, status=HTTP_200_OK
            )

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
