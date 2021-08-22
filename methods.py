# These functions need to be implemented
class Token:

    def generate_token(self, username, password):
        saltpass = username + password + salt
        return hashlib.sha256(saltpass.encode()).hexdigest()


class Restricted:

    def access_data(self, authorization):
        return 'test'
