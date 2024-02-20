from graphene import ObjectType, String, Field, List, Int

class User(ObjectType):
    id = String()
    name = String()
    email = String()
    password = String()


