from ema_workbench import (Model, RealParameter,
                           ScalarOutcome,  
                           Constant, IntegerParameter)
from model import EtmEVsModel

def ema_problem(problem):
    
    # convert model to function
    EtmEVs = EtmEVsModel.as_function()

    
    model = Model('EtmEVsModel', function=EtmEVs)
    
    # problem 1 with all the model uncertainties, constans and outcomes
    if problem == 1:
        model.uncertainties = [
            RealParameter('p_smart', 0, 1), 
            RealParameter('weekend_week_ratio', 0, 1),
            RealParameter('p_pref', 0, 1), 
            RealParameter('pref_home', 0, 1), 
            RealParameter('pref_strictness', 0, 1),
            RealParameter('VTG_percentage', 0, 1),
            IntegerParameter('offset_dep', 0, 4),
            IntegerParameter('offset_dwell', 0, 4),
            IntegerParameter('average_driving_speed', 4, 25)
            ]
        model.constants = [
            Constant('steps', 96), 
            Constant('g', 0.000076), 
            Constant('m', 3), 
            Constant('n_evs', 17400),
            Constant('charging_speed_min', 20),
            Constant('charging_speed_max', 60),
            Constant('l_dep', 30),
            Constant('m_dep', 34.5),
            Constant('h_dep', 66),
            Constant('l_dwell', 12),
            Constant('m_dwell', 28),
            Constant('h_dwell', 36),
            Constant('l_vol', 16.7),
            Constant('m_vol', 59.6),
            Constant('h_vol', 107.8),
            Constant('l_energy', 0.104),
            Constant('m_energy', 0.192),
            Constant('h_energy', 0.281),]
        model.outcomes = [
            ScalarOutcome('min_average_battery_percentage'),
            ScalarOutcome('mean_average_battery_percentage'),
            ScalarOutcome('min_power_demand'),
            ScalarOutcome('mean_power_demand'),
            ScalarOutcome('max_power_demand'),
            ScalarOutcome('min_VTG_capacity'),
            ScalarOutcome('mean_VTG_capacity'),
            ScalarOutcome('max_VTG_capacity'),
            ScalarOutcome('min_mean_charging'),
            ScalarOutcome('mean_mean_charging'),
            ScalarOutcome('max_mean_charging')
            ]
        return model
    if problem == 2:
        pass