
import insulin_absorption

minimum_fraction = 0.025
seconds_per_hour = 3600

class BasalSegment(object):
    def __init__(self, hour, units_per_hour):
        self.hour = hour
        self.units_per_hour = units_per_hour

    def __str__(self):
        return "@{} : {}/hr".format(self.hour, self.units_per_hour)

class BasalPattern(object):
    def __init__(self):
        self.pattern_rates = []

    # hour in the form of 0 for midnight, 5.5 for 5:30 am, 17.5 for 5:30 pm
    def add_basal(self, basal_segment):
        self.pattern_rates.append(basal_segment)

    def sort(self):
        self.pattern_rates.sort(key=lambda p: p.hour)

    def create_three_day_pattern(self):
        self.sort()
        pattern_rates = []
        for p in self.pattern_rates:
            s = BasalSegment(
                p.hour - 24,
                p.units_per_hour)
            pattern_rates.append(s)
        pattern_rates += self.pattern_rates
        for p in self.pattern_rates:
            s = BasalSegment(
                p.hour + 24,
                p.units_per_hour)
            pattern_rates.append(s)

        return pattern_rates

    def create_doses(self):
        pattern_rates = self.create_three_day_pattern()
        c = 0
        remaining = 0
        doses = []
        epsilon = 1e-5
        while(c < len(pattern_rates)-1):
            p = pattern_rates[c]
            hours_till_next_pattern = pattern_rates[c + 1].hour - p.hour
            min_dose_count = (p.units_per_hour / minimum_fraction) * hours_till_next_pattern
            seconds_per_min_dose = hours_till_next_pattern * seconds_per_hour / min_dose_count
            for i in range(int(min_dose_count + epsilon)):
                if i > 0:
                    delta = (i * seconds_per_min_dose) / 3600
                else:
                    delta = 0
                doses.append(insulin_absorption.Dose(
                    minimum_fraction,
                    p.hour + delta,
                    "{} #{}".format(p, i)
                ))
            c += 1
        return doses
