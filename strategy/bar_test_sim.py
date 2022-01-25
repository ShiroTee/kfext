import kungfu.yijinjing.time as kft
from kungfu.wingchun.constants import *
import os, signal, time
import json

# 期货
# source = Source.CTP
# account = "089270"
# tickers = ["ag2012","ag2101"]
# VOLUME = 2


# 股票
source = "sim"
account = "test"
# tickers = [str(600000 + index) for index in range(2)]
# tickers2 = [str(600003 + index) for index in range(2)]
tickers = [str(600000 + index) for index in range(10)]
tickers2 = [str(600000 + index) for index in range(20)]
# tickers3 = [str(600000 + index) for index in range(30)]

VOLUME = 200
EXCHANGE = Exchange.SSE


# 启动前回调，添加交易账户，订阅行情，策略初始化计算等
def pre_start(context):
    context.add_account(source, account, 100000.0)
    context.subscribe(source, tickers2, "SSE")
    # context.subscribe("zhaosStock", tickers3, "SSE")
    context.subscribe('bar', tickers, "SSE")
    context.ordered = False


# 启动准备工作完成后回调，策略只能在本函数回调以后才能进行获取持仓和报单
def post_start(context):
    context.log.warning("post_start")


# 收到快照行情时回调，行情信息通过quote对象获取
def on_quote(context, quote):
    # context.log.info("[on_quote--------------------------] {}".format(quote.instrument_id))
    # if quote.instrument_id == "600005":
    context.insert_order(quote.instrument_id, EXCHANGE, account, quote.last_price, VOLUME,
                                    PriceType.Limit, Side.Buy, Offset.Open)

def on_bar(context, bar):
    context.log.info("{}_{}".format(bar.instrument_id, bar.exchange_id))

