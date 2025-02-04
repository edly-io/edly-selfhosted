import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutoredlyselfhosted", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-edly-selfhosted",
    version=ABOUT["__version__"],
    url="https://github.com/edly-io/tutor-edly-selfhosted",
    project_urls={
        "Code": "https://github.com/edly-io/tutor-edly-selfhosted",
        "Issue tracker": "https://github.com/edly-io/tutor-edly-selfhosted/issues",
    },
    license="AGPLv3",
    author="Edly",
    author_email="hello@edly.io",
    description="Tutor plugin for self-hosted Open edX platforms supported by Edly",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=["tutor>=19.0.0,<20.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>=19.0.0,<20.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "edly-selfhosted = tutoredlyselfhosted.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
