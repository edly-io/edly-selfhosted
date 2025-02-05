"""
edly_selfhosted Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)
from openedx.core.djangoapps.plugins.constants import ProjectType


class EdlySelfHostedConfig(AppConfig):
    """
    Configuration for the edly_selfhosted Django application.
    """

    name = 'edly_selfhosted'

    plugin_app = {
    # Configuration setting for Plugin URLs for this app.
    PluginURLs.CONFIG: {
        ProjectType.LMS: {
            # The namespace to provide to django's urls.include.
            PluginURLs.NAMESPACE: 'edly_selfhosted',

            # The application namespace to provide to django's urls.include.
            # Optional; Defaults to None.
            PluginURLs.APP_NAME: 'edly_selfhosted',

            # The regex to provide to django's urls.url.
            # Optional; Defaults to r''.
            PluginURLs.REGEX: r'^edly/',

            # The python path (relative to this app) to the URLs module to be plugged into the project.
            # Optional; Defaults to 'urls'.
            PluginURLs.RELATIVE_PATH: 'urls',
        },
        ProjectType.CMS: {
            # The namespace to provide to django's urls.include.
            PluginURLs.NAMESPACE: 'edly_selfhosted',

            # The application namespace to provide to django's urls.include.
            # Optional; Defaults to None.
            PluginURLs.APP_NAME: 'edly_selfhosted',

            # The regex to provide to django's urls.url.
            # Optional; Defaults to r''.
            PluginURLs.REGEX: r'',

            # The python path (relative to this app) to the URLs module to be plugged into the project.
            # Optional; Defaults to 'urls'.
            PluginURLs.RELATIVE_PATH: 'urls',
        },
    },
}
