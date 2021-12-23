from model import EtmEVsModel

parameters = {
    'steps': 96 * 5,
    'g': 0.000076,
    'm': 3,
    'percentage_ev': 0.00003,#0.0000029 * 0.2,# 0.0003,
    'VTG_percentage': 0.15,
    'charging_speed_min': 20,
    'charging_speed_max': 60,
    'l_dep': 20*1.5,
    'm_dep': 23*1.5,
    'h_dep': 44*1.5,
    'offset_dep': 2,
    'l_dwell': 12,
    'm_dwell': 28,
    'h_dwell': 36,
    'offset_dwell': 3,
    'average_driving_speed': 10,
    'l_vol': 16.7,
    'm_vol': 59.6,
    'h_vol': 107.8,
    'l_energy': 0.104,
    'm_energy': 0.192,
    'h_energy': 0.281,
    'p_smart': 0.2,
    'seed': 421,
}

model = EtmEVsModel(parameters)
print('starting simulation')
results = model.run()
results.variables.EtmEVsModel.plot()
results.variables.EtmEVsModel['average_battery_percentage'].plot()