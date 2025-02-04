# Edly plugins for self-hosted Open edX platform

This repository contains some custom changes for self-hosted Open edX platforms, such as the [machine image](https://aws.amazon.com/marketplace/pp/prodview-iji6gmbfbpi3o) that is available on the AWS marketplace.

## Installation

Install and enable the "edly-selfhosted" plugin:

    pip install -e "git+https://github.com/edly-io/edly-selfhosted.git@main#egg=tutor-edly-selfhosted&subdirectory=tutor-edly-selfhosted"
    tutor plugins enable edly-selfhosted

Build the "mfe", "openedx" and "openedx-dev" Docker images:

    tutor images build mfe openedx openedx-dev

Launch the platform:

    tutor local launch

## License

This work is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://github.com/edly-io/edly-selfhosted/blob/main/LICENSE.txt>).
