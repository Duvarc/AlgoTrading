from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume
 
def initialize(context):
    """
    Called once at the start of the algorithm.
    """   
    context.security = symbol('BMY')
    set_benchmark(symbol('BMY'))
    schedule_function(handle_data, date_rules.every_day(), time_rules.market_close(hours=0, minutes=1))

def handle_data(context,data):
    MA1 = data.history(context.security, 'price', 50, '1d').mean()
    MA2 = data.history(context.security, 'price', 200, '1d').mean()
    
    current_price = data.current(context.security, 'price')
    current_positions = context.portfolio.positions[symbol('SPY')].amount
    cash = context.portfolio.cash
    
    if (MA1 > MA2 and current_positions == 0):
        number_of_shares = cash // current_price
        order(context.security, number_of_shares)
    elif (MA1 < MA2 and current_positions > 0):
        order(context.security, -1 * current_positions)
    
    
    
    

