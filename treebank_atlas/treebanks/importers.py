import json
import os

from django.conf import settings

from .models import Treebank


TREEBANKS_DATA_PATH = os.path.join(settings.PROJECT_ROOT, "data", "treebanks")
TREEBANKS_METADATA_PATH = os.path.join(TREEBANKS_DATA_PATH, "metadata.json")


def _import_treebank(data):
    treebank_obj, _ = Treebank.objects.update_or_create(
        urn=data["urn"],
        defaults=dict(name=data["metadata"]["work_title"], metadata=data["metadata"]),
    )
    full_content_path = os.path.join(TREEBANKS_DATA_PATH, data["content_path"])
    print(full_content_path)
    raise NotImplementedError()


def import_treebanks(reset=False):
    if reset:
        # Delete all previous Treebank instances.
        Treebank.objects.all().delete()

    treebanks_metadata = json.load(open(TREEBANKS_METADATA_PATH))
    for treebank_metadata in treebanks_metadata["treebanks"]:
        _import_treebank(treebank_metadata)
