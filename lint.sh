#!/bin/bash

isort -rc treebank_atlas
black treebank_atlas
flake8 treebank_atlas
