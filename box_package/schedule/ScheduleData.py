

class ScheduleData:
    def __init__(self):
        self.data = []

        self.example_1 = {
            "name": 'voenka',
            "time_start": '12:00',
            "lecturer": 'Kozlov',
            "cabinet": '33',
            "week": "4",
            "match": "1",
        }

        self.example_2 = {
            "name": 'voenka1',
            "time_start": '13:30',
            "lecturer": 'Kozlov',
            "cabinet": '4',
            "week": "4",
            "match": "2",
        }

        self.example_3 = {
            "name": 'voenka2',
            "time_start": '15:00',
            "lecturer": 'Kozlov',
            "cabinet": '3',
            "week": 4,
            "match": "3",
        }

    def push(self):
        self.data.append(self.example_1)
        self.data.append(self.example_2)
        self.data.append(self.example_3)

    def push_new(self, data):
        self.data.append(data)
