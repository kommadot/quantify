from datetime import datetime
import backtrader as bt

#Create a subclass to define the indicators and Logic
class Momentum(bt.Strategy):
    #list of parameters which are configurable for the strategy
    params = dict(
        pfast = 5, # period for the fast moving average
        pslow = 20  # period for the slow moving average
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.smaSlow = bt.ind.SimpleMovingAverage(period=self.p.pslow)
        self.smaFast = bt.ind.SimpleMovingAverage(period=self.p.pfast)
        self.order = None

    def log(self,txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s,%s' % (dt.isoformat(), txt))

    def notify_order(self, order):
        # 1. If order is submitted/accepted, do nothing
        if order.status in [order.Submitted, order.Accepted]:
            return
        # 2. If order is buy/sell executed, report price executed
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, Price: {0:8.2f} Cost : {2:8.2f}, Comm: {3:8.2f}'.format(
                    order.executed.price,
                    order.executed.size,
                    order.executed.value,
                    order.executed.comm
                ))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else :
                self.log('SELL EXECUTED. Price: {0:8.2f} Cost : {2:8.2f}, Comm: {3:8.2f}'.format(
                    order.executed.price,
                    order.executed.size,
                    order.executed.value,
                    order.executed.comm
                ))
                self.bar_executed = len(self) # when was trade executed
            # 3. If order is canceled/margin/rejected, report order canceled
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        self.order = None

    def next(self):
        cash = self.broker.get_cash()
        value = self.broker.get_value()
        size = int(cash / self.data.close[0])
        if self.order :
            return

        if not self.position: # not in the market
            if self.smaSlow > self.data.close[0]:
                self.order = self.buy(size=size)

        elif self.getposition().size > 0: # in the market
            if self.smaSlow < self.data.close[0]:
                self.order = self.sell(size=self.getposition().size)

def run(args=None):
    cerebro = bt.Cerebro() # create a "Cerebro" engine instance
    cerebro.broker.setcash(1000000)
    data = bt.feeds.YahooFinanceData(dataname='005930.KS', fromdate=datetime(2019, 1, 1),
                                  todate=datetime(2019, 12, 31))
    cerebro.adddata(data)
    cerebro.addstrategy(Momentum)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfollio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()

if __name__ == '__main__':
    run()