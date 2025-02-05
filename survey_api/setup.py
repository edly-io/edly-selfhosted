#!/usr/bin/env python
"""
Package metadata for survey_api.
"""
import os
import re

from setuptools import find_packages, setup


def get_version(*file_paths):
    """
    Extract the version string from the file.

    Input:
     - file_paths: relative path fragments to file with
                   version string
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename, encoding="utf8").read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')



VERSION = get_version('survey_api', '__init__.py')
README = open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding="utf8").read()

setup(
    name='survey_api',
    version=VERSION,
    description="""Edly onboarding form for self-hosted Open edX platforms.""",
    long_description=README,
    author='Edly',
    author_email='hello@edly.io',
    url='https://github.com/edly-io/edly-selfhosted',
    packages=find_packages(
        include=['survey_api', 'survey_api.*'],
        exclude=["*tests"],
    ),
    entry_points={
        "lms.djangoapp": [
            "survey_api = survey_api.apps:SurveyApiConfig",
        ],
        "cms.djangoapp": [
            "survey_api = survey_api.apps:SurveyApiConfig",
        ],
    },
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8",
    license="AGPL 3.0",
    zip_safe=False,
    keywords='Python openedx',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)
