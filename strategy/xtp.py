# -*- coding: UTF-8 -*-
import kungfu.yijinjing.time as kft
from kungfu.wingchun.constants import *
import time
import requests

SOURCE = "zhaosStock"
ACCOUNT = "0025200135"
tickers = ["000001","000002"]
VOLUME = 200
EXCHANGE = Exchange.SZE


# 启动前回调，添加交易账户，订阅行情，策略初始化计算等
def pre_start(context):
    # time.sleep(10)
    context.add_account(SOURCE, ACCOUNT, 100000.0)
    context.subscribe(SOURCE, tickers, EXCHANGE)


# 启动准备工作完成后回调，策略只能在本函数回调以后才能进行获取持仓和报单
def post_start(context):
    context.log.warning("post_start {}".format(context.now()))

# 收到快照行情时回调，行情信息通过quote对象获取
def on_quote(context, quote):
    context.log.info("[on_quote] {}----{}".format(quote.instrument_id, quote.last_price))

    if quote.instrument_id in tickers:
        order_id = context.insert_order(quote.instrument_id, EXCHANGE, ACCOUNT, quote.last_price, VOLUME,
                                        PriceType.Limit, Side.Buy, Offset.Open)


        context.log.info("ticker---{},order_id---{}".format(quote.instrument_id, order_id))


def on_order(context, order):
    context.log.info('[on_order] {}---{}--{}--{}'.format(order, order.status, order.price_type, order.side))
