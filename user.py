from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM users;"
        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    # Data is holding a dictionary of things that come from our form. The insert into in parentheses has names matching the columns in database and values names need to match the keys in the dictionaries that you are giving the values for
    def create(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) "
        query += "VALUES( %(first_name)s, %(last_name)s, %(email)s)"

        new_user = connectToMySQL('users_schema').query_db(query, data)
        return new_user