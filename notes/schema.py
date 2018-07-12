from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel


class Note(DjangoObjectType):
    class Meta:
        model = NoteModel
    interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    notes = graphene.List(Note)

    def resolve_notes(self, info):
    #  user = self.request.user
    #  print(user)
     pass

schema = graphene.Schema(query=Query)