from datetime import datetime


class User:
    def __init__(self, username="", password="", real_name="", email="", gender=None, birthday: str = None):
        self.username = username
        self.password = password
        self.real_name = real_name
        self.email = email
        self.gender = gender
        if birthday is None:
            self.birthdate = None
        else:
            self.birthdate = datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.__class__} object: username={self.username}, real_name={self.real_name}"

    def __repr__(self):
        return f"{self.__class__}(username='{self.username}', password='{self.password}', real_name='{self.real_name}', email='{self.email}', gender={self.gender}, birthday='{self.birthdate}')"

    def __eq__(self, other):
        return self.username == other.username and self.real_name == other.real_name

    def __lt__(self, other):
        pass


if __name__ == '__main__':
    d = datetime(year=2000, month=12, day=2, hour=3, minute=1)
    user1 = User(username="Bob", birthday="2000-12-02 00:00:00")
    user2 = User(username="Bob", birthday="2000-12-02 00:00:00")
    print(user1 is user2)
    print(user1 == user2)
