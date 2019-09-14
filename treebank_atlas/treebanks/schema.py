from graphene import ObjectType, relay
from graphene.types import generic
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Treebank


class TreebankNode(DjangoObjectType):
    metadata = generic.GenericScalar()

    class Meta:
        model = Treebank
        interfaces = (relay.Node,)
        filter_fields = ["name", "urn"]


class Query(ObjectType):
    treebank = relay.Node.Field(TreebankNode)
    treebanks = DjangoFilterConnectionField(TreebankNode)
