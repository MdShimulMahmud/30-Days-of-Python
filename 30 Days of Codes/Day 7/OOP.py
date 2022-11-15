class StoryBook:
    # class variable are defined here 
    class_varibles = "Boss"

    def __init__(self, name, age, id,school):
        self.name = name
        self.age = age
        self.id = id
        self.school = school 
    # methods
    def get_info(self):
        print(f'Name : {self.name} \n Age : {self.age} \n  ID : {self.id}\n School : {self.school} ')
    

book_1 = StoryBook("Shimul", 21, 1804021,'CUET')
# book_2 = StoryBook("Yahan",22,1804007)

# print(book_1.id)

book_1.get_info()

