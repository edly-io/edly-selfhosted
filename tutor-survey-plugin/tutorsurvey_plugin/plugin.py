import os
from glob import glob

import importlib_resources
from tutor import hooks
from tutormfe.hooks import PLUGIN_SLOTS

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

hooks.Filters.CONFIG_DEFAULTS.add_item(
    # Typeform ID
    ("SURVEY_PLUGIN_FORM_ID", "WHBX8vDV")
)

########################################
# PATCH LOADING
########################################

# For each file in tutorsurvey_plugin/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    str(importlib_resources.files("tutorsurvey_plugin") / "patches" / "*")
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

########################################
# MFE footer customisation
########################################
PLUGIN_SLOTS.add_items(
    [
        (
            "all",
            "footer_slot",
            """{
    op: PLUGIN_OPERATIONS.Insert,
    widget: {
        id: 'custom_footer',
        type: DIRECT_PLUGIN,
        RenderWidget: () => <OnboardingSurvey />
    }
}""",
        )
    ]
)

########################################
# Survey API development
########################################
hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", "survey_api"))
