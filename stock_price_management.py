from articles import *
import random as r
import threading
import requests

url = "http://127.0.0.1:8000/start-timer"

stock1_price_list = []
stock2_price_list = []
stock3_price_list = []
stock4_price_list = []

stock1_return = []
stock2_return = []
stock3_return = []
stock4_return = []

news_return = []

# format = {'open' : 1, 'high' : 1, 'low' : 1, 'close' : 1}

def stock_price_init(val1, val2, val3, val4):
    if len(stock1_return) > 0:
        stock1_price_list.clear()
        stock2_price_list.clear()
        stock3_price_list.clear()
        stock4_price_list.clear()
        stock1_return.clear()
        stock2_return.clear()
        stock3_return.clear()
        stock4_return.clear()
        news_return.clear()
    stock1_price_list.append(val1)
    stock1_price_list.append(stock1_price_list[-1])
    stock1_price_list.append(stock1_price_list[-1])
    stock2_price_list.append(val2)
    stock2_price_list.append(stock2_price_list[-1])
    stock2_price_list.append(stock2_price_list[-1])
    stock3_price_list.append(val3)
    stock3_price_list.append(stock3_price_list[-1])
    stock3_price_list.append(stock3_price_list[-1])
    stock4_price_list.append(val4)
    stock4_price_list.append(stock4_price_list[-1])
    stock4_price_list.append(stock4_price_list[-1])
    res = requests.get(url)


def root_update():
    if len(stock1_return) > 100:
        return "라운드가 종료되었습니다."
    else:
        # X1, Y1, X2, Y2, X3, Y3, X4, Y4 = 0
        w = [0,0,0,0]
        decision = r.randint(1,2)
        if len(stock1_return) == 20:
            v1 = select_positive_news()
            decision = 1
            w[v1[1]-1] = 10*v1[2]
            news_return.append(v1[-1])
        elif len(stock1_return) == 40:
            v2 = select_negative_news()
            decision = 2
            w[v2[1] - 1] = 10 * v2[2]
            news_return.append(v2[-1])
        elif len(stock1_return) == 60:
            v3 = select_positive_news()
            decision = 1
            w[v3[1] - 1] = 10 * v3[2]
            news_return.append(v3[-1])
        elif len(stock1_return) == 80:
            v4 = select_negative_news()
            decision = 2
            w[v4[1] - 1] = 10 * v4[2]
            news_return.append(v4[-1])

        else:
            decision = r.randint(1, 2)

        stock1_price_update(decision, w[0])
        stock2_price_update(decision, w[1])
        stock3_price_update(decision, w[2])
        stock4_price_update(decision, w[3])

        threading.Timer(6, root_update).start()

def stock1_price_update(decision, X1):
    # 1 -> upper / 2 -> lower
    x = stock1_price_list[-3]
    y = stock1_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 40 + X1
        b += 45 + X1
    else:
        a -= 45 + X1
        b -= 40 + X1
        if a <= 0 or b <= 0:
            a += 45
            b += 46

    val = r.randint(a,b)

    stock1_price_list.append(val)

    res = {'open': stock1_price_list[-2], 'high': stock1_price_list[-2], 'low': stock1_price_list[-1],
           'close': stock1_price_list[-1]}
    stock1_return.append(res)

    return stock1_price_list

def stock2_price_update(decision, X2):
    # 1 -> upper / 2 -> lower
    x = stock2_price_list[-3]
    y = stock2_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 45 + X2
        b += 50 + X2
    else:
        a -= 50 + X2
        b -= 45 + X2
        if a <= 0 or b <= 0:
            a += 50
            b += 51

    val = r.randint(a,b)

    stock2_price_list.append(val)

    res = {'open' : stock2_price_list[-2], 'high' : stock2_price_list[-2], 'low' : stock2_price_list[-1], 'close' : stock2_price_list[-1]}
    stock2_return.append(res)

    return stock2_price_list

def stock3_price_update(decision, X3):
    # 1 -> upper / 2 -> lower
    x = stock3_price_list[-3]
    y = stock3_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 50 + X3
        b += 55 + X3
    else:
        a -= 55 + X3
        b -= 50 + X3
        if a <= 0 or b <= 0:
            a += 55
            b += 56

    val = r.randint(a,b)

    stock3_price_list.append(val)

    res = {'open': stock3_price_list[-2], 'high': stock3_price_list[-2], 'low': stock3_price_list[-1],
           'close': stock3_price_list[-1]}
    stock3_return.append(res)

    return stock3_price_list

def stock4_price_update(decision, X4):
    # 1 -> upper / 2 -> lower
    x = stock4_price_list[-3]
    y = stock4_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 40 + X4
        b += 45 + X4
    else:
        a -= 45 + X4
        b -= 40 + X4
        if a <= 0 or b <= 0:
            a += 45
            b += 46

    val = r.randint(a,b)

    stock4_price_list.append(val)

    res = {'open': stock4_price_list[-2], 'high': stock4_price_list[-2], 'low': stock4_price_list[-1],
           'close': stock4_price_list[-1]}
    stock4_return.append(res)

    return stock4_price_list
