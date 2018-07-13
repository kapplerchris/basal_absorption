
from matplotlib import pyplot
import itertools

def flatten(l):
    return list(itertools.chain(*l))

def show():
    pyplot.show(True)

def three_day_xticks():
    xlocations = range(-24, 48)
    xlabels = ['{}:00'.format(h%24) for h in xlocations]
    pyplot.xticks(xlocations, xlabels)

def plot_basal_pattern(basal_pattern):
    pattern = basal_pattern.create_three_day_pattern()
    y_values_x1 = [p.units_per_hour for p in pattern]
    # to make a square wave
    # duplicate each x value at two y values
    y_values_x2 = flatten(zip(y_values_x1, y_values_x1))[:-1]
    x_values_x1 = [p.hour for p in pattern]
    # and duplicate each y value at two x values
    x_values_x2 = flatten(zip(x_values_x1, x_values_x1))[1:]
    pyplot.plot(x_values_x2, y_values_x2, '-')
    div_4 = map(lambda x: x/4, y_values_x2)
    pyplot.plot(x_values_x2, div_4, '--')

def scatter_plot_dosage_and_absorption(timeline):
    timeline.sort()
    increment = 15.0 / 60
    offset = increment
    x_values = []
    y_values = []
    x_dose = []
    y_dose = []
    seen_doses = set()
    for em in timeline.timeline:
        if (em.dose not in seen_doses):
            seen_doses.add(em.dose)
            x_dose.append(em.dose.given_at_time)
            y_dose.append(em.dose.units)
        x_values.append(em.effective_time)
        y_values.append(em.dose.units * em.get_fraction())
    pyplot.plot(x_dose, y_dose, '+')
    pyplot.plot(x_values, y_values, 's')


def plot_absorption(timeline):
    timeline.sort()
    increment = 15.0 / 60
    skew = 7.5 / 60
    offset = increment + timeline.timeline[0].dose.given_at_time
    x_values = []
    y_values = []
    while not timeline.empty():
        sum_dosage = 0
        for em in timeline.get_through(offset + skew):
            sum_dosage += em.dose.units * em.get_fraction()
        x_values.append(offset)
        y_values.append(sum_dosage)
        offset += increment
    pyplot.plot(x_values, y_values, '-s')
