import pump_dosages
import insulin_absorption
import insulin_plotter

basal = pump_dosages.BasalPattern()
basal.add_basal(pump_dosages.BasalSegment(0, 0.4))
basal.add_basal(pump_dosages.BasalSegment(2.5, 0.575))
basal.add_basal(pump_dosages.BasalSegment(8, 0.45))
basal.add_basal(pump_dosages.BasalSegment(10, 0.3))
basal.add_basal(pump_dosages.BasalSegment(18, 0.4))

insulin_plotter.plot_basal_pattern(basal)

timeline = insulin_absorption.Timeline()
for d in basal.create_doses():
    timeline.add_dose(d)

#insulin_plotter.scatter_plot_dosage_and_absorption(timeline)
insulin_plotter.plot_absorption(timeline)

insulin_plotter.three_day_xticks()
insulin_plotter.show()


basal = pump_dosages.BasalPattern()
basal.add_basal(pump_dosages.BasalSegment(0, 1.4))
basal.add_basal(pump_dosages.BasalSegment(1.5, 0.4))
basal.add_basal(pump_dosages.BasalSegment(2.5, 0.575))
basal.add_basal(pump_dosages.BasalSegment(8, 0.45))
basal.add_basal(pump_dosages.BasalSegment(10, 0.3))
basal.add_basal(pump_dosages.BasalSegment(18, 0.4))
basal.add_basal(pump_dosages.BasalSegment(22.5, 1.4))

insulin_plotter.plot_basal_pattern(basal)

timeline = insulin_absorption.Timeline()
for d in basal.create_doses():
    timeline.add_dose(d)

#insulin_plotter.scatter_plot_dosage_and_absorption(timeline)
insulin_plotter.plot_absorption(timeline)



insulin_plotter.three_day_xticks()
insulin_plotter.show()

timeline = insulin_absorption.Timeline()
dose = insulin_absorption.Dose(6, 6.5)
timeline.add_dose(dose)
insulin_plotter.scatter_plot_dosage_and_absorption(timeline)
insulin_plotter.plot_absorption(timeline)
insulin_plotter.show()
