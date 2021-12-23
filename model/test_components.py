import pytest
from components import EV, Municipality
from model import EtmEVsModel


# tests for EV model component
@pytest.fixture
def example_model():
    example_params = {
        'steps': 1,
        'g': 0.000076,
        'm': 3,
        'percentage_ev': 0.0000029 * 0.2,# 0.0000029 * 0.2,0.00003
        'VTG_percentage': 0.15,
        'charging_speed_min': 20,
        'charging_speed_max': 60,
        'l_dep': 20,
        'm_dep': 23,
        'h_dep': 44,
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
        'p_smart': 1,
        'seed': 4,
    }
    example_model = EtmEVsModel(example_params)
    example_model.run() # model must be run to fully initialize, set to one step only
    return example_model

def test_choose_cheapest_timesteps(example_model):
    ev = example_model.EVs[0]
    ev.charging_speed = 4
    ev.choose_cheapest_timesteps(0,50,10) # charge between time 0 and time 50
    assert len(ev.cheapest_timesteps) == 10

def test_charging_exceed(example_model):
    ev = example_model.EVs[0]
    ev.current_battery_volume = 20
    ev.battery_volume = 25
    ev.charging_speed = 40 # makes a charge of 10 per 15 minutes, exceeding 25
    ev.charge()
    assert ev.current_battery_volume == 25

def test_departure_work(example_model):
    ev = example_model.EVs[0]
    example_model.t = 20
    ev.departure_time = 20
    ev.offset_dep = 0
    ev.current_location = 'home'
    ev.current_battery_volume = 20
    ev.energy_required = 20
    ev.step()
    assert ev.current_location == 'onroad'

def test_low_charge_departure_work(example_model):
    ev = example_model.EVs[0]
    example_model.t = 20
    ev.departure_time = 20
    ev.offset_dep = 0
    ev.current_location = 'home'
    ev.current_battery_volume = 20
    ev.energy_required = 30
    ev.step()
    assert ev.current_location == 'home'

def test_arrive_work(example_model):
    ev = example_model.EVs[0]
    example_model.t = 50
    ev.arrival_time_work = 50
    ev.current_location = 'onroad'
    ev.step()
    assert ev.current_location == 'work'

def test_departure_home(example_model):
    ev = example_model.EVs[0]
    example_model.t = 80
    ev.arrival_return_time = 80
    ev.current_location = 'work'
    ev.current_battery_volume = 20
    ev.energy_required = 10
    ev.step()
    assert ev.current_location == 'onroad'

def test_delay_home_departure(example_model):
    ev = example_model.EVs[0]
    example_model.t = 80
    ev.arrival_return_time = 80
    ev.current_location = 'work'
    ev.current_battery_volume = 20
    ev.energy_required = 30
    ev.step()
    assert ev.current_location == 'work'

def test_arrive_home(example_model):
    ev = example_model.EVs[0]
    example_model.t = 100
    ev.arrival_time_home = 100
    ev.current_location = 'onroad'
    ev.step()
    assert ev.current_location == 'home'

def test_discharge(example_model):
    ev = example_model.EVs[0]
    example_model.t = 100
    ev.arrival_time_home = 105
    ev.current_location = 'onroad'
    old_charge = ev.current_battery_volume
    ev.step()
    assert ev.current_battery_volume < old_charge


