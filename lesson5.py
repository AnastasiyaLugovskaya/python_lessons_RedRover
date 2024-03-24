class HybeEmployee():
    __salary = None

    def __init__(self, fname, lname, category, salary):
        self.fname = fname
        self.lname = lname
        self.category = category
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def work(self):
        return f"My name is {self.lname} {self.fname}. I'm working for Hybe"


class HybeStaff(HybeEmployee):
    def __init__(self, fname, lname, category, salary, position, working_hours):
        super().__init__(fname, lname, category, salary)
        self.position = position
        self.working_hours = working_hours

    def work(self):
        return f"My name is {self.lname} {self.fname}. I'm working for Hybe as a {self.position} for {self.working_hours}" \
               f" hours per week"


class HybeArtist(HybeEmployee):
    def __init__(self, fname, lname, category, salary, group_name, fandom_name):
        super().__init__(fname, lname, category, salary)
        self.group_name = group_name
        self.fandom_name = fandom_name

    def work(self):
        return f"My name is {self.lname} {self.fname}. I'm working for Hybe as a member of group {self.group_name}. I " \
               f"work to make my {self.fandom_name} happy"


# task 5.1
bang_sihyuk = HybeEmployee('Si Hyuk', 'Bang', 'Producer', 500000)
print(bang_sihyuk.work())
print("_" * 30)

kim_sejin = HybeStaff('Sejin', 'Kim', 'full-time staff', 95000, 'Manager', 40)
print(kim_sejin.work())
print("_" * 30)

min_yoongi = HybeArtist('Yoongi', 'Min', 'Group member', 1000000, 'BTS', 'ARMY')
print(min_yoongi.work())
print("_" * 30)
