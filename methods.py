# These functions need to be implemented
class Token:

    def generate_token(self, username, password):
        saltpass = username + password + self
        return hashlib.sha256(saltpass.encode()).hexdigest()


class Restricted:

    def access_data(self, authorization):
        return 'You are under protected data'
