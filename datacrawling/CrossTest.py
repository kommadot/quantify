from datetime import datetime
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=5), bt.ind.SMA(period=20)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()

cerebro.broker.setcash(100000) #자산을 10만원으로 초기화

cerebro.addstrategy(SmaCross)

data0 = bt.feeds.YahooFinanceData(dataname='005930.KS', fromdate=datetime(2019, 1, 1),
                                  todate=datetime(2019, 12, 31))
cerebro.adddata(data0)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue()) #시작 시 자산

cerebro.run()

print('Final Portfollio Value: %.2f' % cerebro.broker.getvalue()) #종료 시 자산

cerebro.plot()