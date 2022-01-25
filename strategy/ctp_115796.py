import kungfu.yijinjing.time as kft
from kungfu.wingchun.constants import *
import time
import requests

# 期货
SOURCE = "ctp"
ACCOUNT = "115796"
# # tickers = ["j2201", "SA201"]
tickers = ["cu2110", "fu2201", "bu2112", "ni2111"]
VOLUME = 1
# # EXCHANGE = Exchange.DCE
EXCHANGE = Exchange.SHFE


# 启动前回调，添加交易账户，订阅行情，策略初始化计算等
def pre_start(context):
    context.add_account(SOURCE, ACCOUNT, 100000.0)
    context.subscribe(SOURCE, tickers, EXCHANGE)


# 启动准备工作完成后回调，策略只能在本函数回调以后才能进行获取持仓和报单
def post_start(context):
    context.log.warning("[post_start]{}")


# 收到快照行情时回调，行情信息通过quote对象获取
def on_quote(context, quote):
    context.log.info("[on_quote] {}".format(quote.instrument_id))

    if quote.instrument_id in tickers:
        #获取策略的投资组合，并打印相关参数
        book = context.get_account_book(SOURCE, ACCOUNT)
        context.log.warning("[account capital] (avail){} (margin){} ".format(book.asset.avail, book.asset.margin))
        order_id = context.insert_order(quote.instrument_id, EXCHANGE, ACCOUNT, quote.last_price, VOLUME,
                                        PriceType.Limit, Side.Buy, Offset.Open)


def on_order(context, order):
    context.log.info('[on_order]---{}  -----{}'.format(order, order.status))


def on_trade(context, trade):
    context.log.info('[on_trade] {}---{}'.format(trade, trade.trading_day))
 
