from model import EmtAgentsModel

parameters = {
    'vehicles': 10,
    'steps': 10,
    'g': 0.000076,
    'm': 3,
    'percentage_ev': 0.0029,
    'charging_speed': 10,
    'l_dep': 20,
    'm_dep': 23,
    'h_dep' : 44,
    'l_dwell': 12,
    'm_dwell': 28,
    'h_dwell': 36,
    'average_driving_speed': 10
}

model = EmtAgentsModel(parameters)
print('starting simulation')
results = model.run()

