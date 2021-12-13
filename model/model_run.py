from model import EtmEVsModel

parameters = {
    'steps': 96 * 31,
    'g': 0.000076,
    'm': 3,
    'percentage_ev': 0.000029,
    'charging_speed_min': 20,
    'charging_speed_max': 60,
    'l_dep': 20,
    'm_dep': 23,
    'h_dep': 44,
    'l_dwell': 12,
    'm_dwell': 28,
    'h_dwell': 36,
    'average_driving_speed': 10,
    'l_vol': 16.7,
    'm_vol': 59.6,
    'h_vol': 107.8,
    'l_energy': 0.104,
    'm_energy': 0.192,
    'h_energy': 0.281,
    'p_smart': 0,
}

model = EtmEVsModel(parameters)
print('starting simulation')
results = model.run()
results.variables.EtmEVsModel.plot()