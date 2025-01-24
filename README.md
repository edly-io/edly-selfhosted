## Steps

1. Use authoring mfe with changes branch and mount it.
2. Mount survey_api
3. Install dependencies and enable tutor-survey-plugin
4. Re-build the openedx-dev image and run the platform

### Authoring

The authoring mfe has an open PR with latest changes

### survey_api

Survey_api contains the custom api.
Files with changes

- views.py
- urls.py
- apps.py

### tutor-survey-plugin

It only has a hook that introduces the api in the platform in plugin.py
