class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("My name is ", name, "I am ", age, "years old "
              "my tracks is ", tracks, "and my score ", score)

    # method
    def change_name(self, name):
        self.name = name
        print("For change_name function", self.name)

    def change_age(self, age):
        self.age = age
        print("For change_age function", self.age)

    def add_tracks(self, tracks):
        self.tracks = tracks
        print("For add_tracks function", self.tracks)

    def get_score(self, score):
        self.score = score
        print("For get_score function", self.score)


# call class
Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
(Bob.change_name("Peter"))
(Bob.change_age(34))
(Bob.add_tracks("UI/UX"))
(Bob.get_score(75.0))
