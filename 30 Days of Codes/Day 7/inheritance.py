class Robot:

    def __init__(self, name , version):
        self.name = name
        self.version = version
    
    def move_forward(self):
        print(f'{self.name} is moving forward!')

    def move_backward(self):
        print(f'{self.name} is moving backward!')
    
    def move_right(self):
        print(f'{self.name} is moving right!')

    def move_left(self):
        print(f'{self.name} is moving left!')

class HouseBot(Robot):
    def __init__(self, name, version, area_covered):
        super().__init__(name, version)
        self.area_covered = area_covered

    def clean(self):
        if self.area_covered > 0:
            print(f'{self.name} is cleaning house!')
            self.area_covered -= 30
            if self.area_covered < 0:
                self.area_covered = 0
        else:
            print('Cannot clean!, please reset the area covered parameter')
    def set_area_covered(self,area):
        if self.area_covered == 0:
            self.area_covered = area
        else:
            print("I can still clean more area!")




hBot = HouseBot('hBot',1.1,40)
print(hBot.name)
hBot.move_forward()