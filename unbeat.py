# coding=utf-8

import sys, os

##-----TODO------
#
#
# Nothing
#
# Suggestions?
#
##----------------

money = 12

def printCoins(amount):
    for i in range(0,amount):
        print """($)""",

def discount(amount):
    global money
    money = money - amount

def machine():
    print ""
    if (money > 3):
        desition = money % 4
        print "computer take : %s" % desition
        discount(desition)
        printCoins(money)
        user()
    else :
        print "And the machine take the last coin, sorry"
        sys.exit()

def user():
    print ""
    try:
        userTake = int(raw_input("I take : "))
        if (userTake == 1 or userTake == 2 or userTake == 3):
            discount(userTake)
            printCoins(money)
            machine()
        else:
            print "Sorry but you can't take %s coins" % userTake
            user()
    except ValueError:
        print "Sorry but you can only take 1, 2 or 3 coins, try again"
        user()

def start():
    printCoins(money)
    user()

def welcome():
    print """
    Welcome, your goal is to get the LAST coin ($). There are 12 coins in total. Each turn you and the machine can take 1, 2 or 3 coins and then is the other player turn. Good luck.
    """
    res = raw_input("Press any key to start or 'Q' to quit. > ")
    if (res == "q" or res == "Q"):
        sys.exit()
    else:
        start()


welcome()
