import os
from glob import glob

import importlib_resources
from tutor import hooks
from tutormfe.hooks import PLUGIN_SLOTS

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        # Typeform ID
        ("EDLY_SELFHOSTED_FORM_ID", "WHBX8vDV"),
        # Install edx-platform plugin from this GitHub branch
        ("EDLY_SELFHOSTED_GIT_BRANCH", "sumac"),
    ]
)

########################################
# PATCH LOADING
########################################

# For each file in tutoredlyselfhosted/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    str(importlib_resources.files("tutoredlyselfhosted") / "patches" / "*")
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

########################################
# MFE footer customisation
########################################

# Display onboarding survey in MFEs
PLUGIN_SLOTS.add_item(
    (
        "all",
        "footer_slot",
        """{
    op: PLUGIN_OPERATIONS.Insert,
    widget: {
        id: 'custom_footer',
        type: DIRECT_PLUGIN,
        RenderWidget: () => <EdlyOnboardingSurvey />
    }
}""",
    )
)

########################################
# edx-platform app development
########################################
hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", "edly_selfhosted"))
