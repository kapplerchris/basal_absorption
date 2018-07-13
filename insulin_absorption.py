# Reverse engineered absorption per 15-minutes from the humalog insert.
# https://www.google.com/search?q=humalog+absorption+curve&tbm=isch

increment_minutes = 15
absorption = [
 0,
 0.014767,
 0.075178,
 0.108739,
 0.116794,
 0.105249,
 0.107397,
 0.093167,
 0.075178,
 0.064170,
 0.052356,
 0.041079,
 0.030340,
 0.025507,
 0.020674,
 0.019063,
 0.017452,
 0.012753,
 0.008055,
 0.006041,
 0.004027,
 0.002014
 ]
events_per_dose = len(absorption)

class Dose(object):
    def __init__(self, units, given_at_time, name = ""):
        self.units = units
        self.name = name
        self.given_at_time = given_at_time

    def __str__(self):
        return "@{} : {}u {}".format(self.given_at_time, self.units, self.name)

class AbsorptionMarker(object):
    def __init__(self, dose, interval):
        self.dose = dose
        self.interval = interval
        self.effective_time = (
            dose.given_at_time + (increment_minutes * interval / 60.0))

    def get_fraction(self):
        return absorption[self.interval]

    def __str__(self):
        return "etm={} :: {}% of {}  idx {}".format(self.effective_time, 100 * self.get_fraction(), self.dose, self.interval)

    def __repr__(self):
        return "<Marker={}>".format(self.__str__())


class Timeline(object):
    def __init__(self):
        self.timeline = []

    def add_dose(self, dose):
        for e in range(events_per_dose):
            marker = AbsorptionMarker(dose, e)
            self.timeline.append(marker)

    def sort(self):
        self.timeline.sort(key=lambda a: a.effective_time)

    def get_through(self, effective_time):
        values = []
        idx = 0
        while self.timeline and idx < len(self.timeline) and self.timeline[idx].effective_time < effective_time:
            values.append(self.timeline[idx])
            idx += 1
        self.timeline = self.timeline[idx:]
        return values

    def empty(self):
        return len(self.timeline) == 0
