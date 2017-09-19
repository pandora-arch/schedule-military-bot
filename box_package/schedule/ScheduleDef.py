from src.box_package.schedule.ScheduleData import ScheduleData


class ScheduleDef:
    def __init__(self):
        self.schedule = ScheduleData()
        self.schedule.push()

    def get_week(self, week):
        data = []
        for box in self.schedule.data:
            if int(box["week"]) == week:
                data.append(box)
        return data

    def to_string(self, data):
        string = ""
        str_space = " "
        str_enter = "\n"
        for box in data:
            string += box["time_start"] +\
                      str_space + box["name"] +\
                      str_space + box["cabinet"] +\
                      str_space + box["lecturer"] + str_enter
        return string

    def now(self):
        pass

example = ScheduleDef()
data = example.get_week(4)
print(example.to_string(example.get_week(4)))
