"""
This is the file that the user has to edit, the strategy function to be precise. 
How to modify:
1. specify the list of options you are going to trade on 
2. specify the enter conditions and exit conditions
3. To get access to the latest minute data just use self.data[instrument_name][-1] where instrument_name is an instrument from the list specified in the 1st step.
4. You can add additional parameters to the init of the Strategy class if needed. 
"""
from broker import *

class Strategy(broker):
    def __init__(self): 
        self.instrument_name="NIFTY 2 DEC 19000 CE"
        super().__init__()

    def strategy(self):
        if self.index%2==1:
            self.buy_order(self.instrument_name,1)
        else:
            self.sell_order(self.instrument_name,1)


model=Strategy()
model.run()