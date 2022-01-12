import agentpy as ap
from ema_workbench import (Model, RealParameter, TimeSeriesOutcome, 
                           ScalarOutcome, SequentialEvaluator, 
                           MultiprocessingEvaluator, ema_logging)
from model import EtmEVsModel

if __name__ == '__main__':
    
    # convert model to function
    EtmEVs = EtmEVsModel.as_function()

    ema_logging.LOG_FORMAT = '%(message)s'
    ema_logging.log_to_stderr(ema_logging.INFO)

    model = Model('EtmEVsModel', function=EtmEVs)
    model.uncertainties = [IntegerParameter('weekend_week_ratio', 0, 1)]
    model.constants = [Constant('steps', 100)]
    model.outcomes = [ScalarOutcome('gini')]

    with SequentialEvaluator(model) as evaluator:
        experiments, results = evaluator.perform_experiments(model, scenarios=10)