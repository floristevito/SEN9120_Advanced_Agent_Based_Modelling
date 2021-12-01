from model import EmtAgentsModel

parameters = {
    'vehicles': 10,
    'steps': 10,
    'g': 0.000076,
    'percentage_ev': 0.0029,
    'charging_speed': 10,
}

model = EmtAgentsModel(parameters)
results = model.run()