# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter é usado para setar o "user"
        self.user = user

    def set_password(self, password):
        self.password = password

# Toda vez que preciso utilizar qualquer método com "self", qualquer
# coisa.

    # @classmethod
    # def create_with_auth(cls, user, password):
    #     connection = cls
    #     connection.user = user
    #     connection.password = password
    #     return connection

    # @staticmethod
    # def soma(x, y):
    #     return x + y

    @staticmethod
    def log(msg):
        print('LOG', msg)


def connection_log(msg):
    print('LOG', msg)


# c1 = Connection.create_with_auth('rafael', '1234')
# c1 = Connection()
# c1.set_user('rafael')
# c1.set_password('123')
# print(Connection.soma(2, 3))
print(Connection.log('Essa é a mensagem de lo'))
# print(c1.user)
# print(c1.password)
