import json
import os

from django.conf import settings

from lxml import etree

from .models import Treebank, Sentence, Word


TREEBANKS_DATA_PATH = os.path.join(settings.PROJECT_ROOT, "data", "treebanks")
TREEBANKS_METADATA_PATH = os.path.join(TREEBANKS_DATA_PATH, "metadata.json")


def _import_treebank(data):
    treebank_obj, _ = Treebank.objects.update_or_create(
        urn=data["urn"],
        defaults=dict(name=data["metadata"]["work_title"], metadata=data["metadata"]),
    )
    full_content_path = os.path.join(TREEBANKS_DATA_PATH, data["content_path"])

    last_sentence = Sentence.objects.order_by("-idx").first()
    if last_sentence:
        sentence_idx = last_sentence.idx + 1
    else:
        sentence_idx = 0

    last_word = Word.objects.order_by("-idx").first()
    if last_word:
        word_idx = last_word.idx + 1
    else:
        word_idx = 0

    with open(full_content_path) as f:
        root = etree.parse(f).getroot()
        sentence_position = 1
        for child in root:
            if child.tag == "sentence":
                sentence_obj = Sentence.objects.create(
                    position = sentence_position,
                    idx = sentence_idx,
                    treebank = treebank_obj
                )
                word_position = 1
                words = {}
                heads = []
                for gchild in child:
                    if gchild.tag == "word":
                        words[gchild.attrib["id"]] = Word.objects.create(
                            position = word_position,
                            idx = word_idx,
                            treebank = treebank_obj,
                            sentence = sentence_obj,
                            form = gchild.attrib["form"],
                            lemma = gchild.attrib.get("lemma"),
                            postag = gchild.attrib.get("postag"),
                            relation = gchild.attrib["relation"],
                            head = None
                        )
                        heads.append((gchild.attrib["id"], gchild.attrib["head"]))
                        word_idx += 1
                        word_position += 1

                for dep, head in heads:
                    if head not in ["0", ""]:
                        words[dep].head = words[head]
                        words[dep].save()

                sentence_idx += 1
                sentence_position += 1


def import_treebanks(reset=False):
    if reset:
        # Delete all previous Treebank, Sentence, and Word instances.
        Treebank.objects.all().delete()
        Sentence.objects.all().delete()
        Word.objects.all().delete()

    treebanks_metadata = json.load(open(TREEBANKS_METADATA_PATH))
    for treebank_metadata in treebanks_metadata["treebanks"]:
        _import_treebank(treebank_metadata)
