# info 
class User:
    def __init__(self, username, email, password):
        # Based on the feedback, the variable 'id'  has been deleted.
        self.username = username
        self.email = email
        self.password = password


    def __str__(self):
        return f"User( username={self.username}, email={self.email})"

# Test. In the future, the test will be from file main.py.
user1 = User("Hosawi", "Hoawi@iastate.edu", "MyPassword123")
print(user1)