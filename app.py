import graphene
from graphene import ObjectType, String, Field, List, Int
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User


class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User, id=String())
    get_users = List(User)

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

def create_user():
    result = schema.execute('''
        mutation {
            createUser(id: "3", name: "Tim Doe", email: "jdoe3@gmail.com", password: "test") {
                    user {
                        id,
                        name,
                        email,
                        password
                    }
                }
            }
                            ''')

    print(result.data)
    return result.data

def update_user():
    result = schema.execute('''
        mutation {
            updateUser(id: "3", name: "Tim Doe", email: "tim.doe@gmail.com", password: "test") {
                    user {
                        id,
                        name,
                        email,
                        password
                    }
                }
            }
                            ''')
    print(result.data)
    return result.data

def delete_user():
    result = schema.execute('''
        mutation {
            deleteUser(id: "3") {
                    user {
                        id,
                        name,
                        email,
                        password
                    }
                }
            }
                            ''')
    print(result.data)
    return result.data


def get_user():
    result = schema.execute('''
        query {
            getUser(id: "3") {
                id,
                name,
                email,
                password
            }
        }
                            ''')
    print(result.data)
    return result.data

if __name__ == '__main__':
    create_user()
    update_user()
    # delete_user()
    get_user()

    print("Done!")
