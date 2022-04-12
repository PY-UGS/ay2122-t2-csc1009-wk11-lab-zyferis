class clockTime:
    def __init__(self):
        self.hours = ""
        self.minutes =""
        self.seconds = ""

    def setHours(self, hours):
        self.hours = hours


    def setMinutes(self, minutes):
        self.minutes = minutes

    def setSeconds(self,seconds):
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)

    def showTime(self):
        print("{} hr:{} min:{} s".format(self.hours, self.minutes, self.seconds))

clock = clockTime()
hours = int(input("Enter integer for hours: "))
minutes = int(input("Enter integer for minutes: "))
seconds = int(input("Enter integer for seconds: "))

clock.setTime(hours,minutes, seconds)
clock.showTime()