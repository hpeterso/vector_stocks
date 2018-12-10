#!/usr/bin/env python3

"""
Make Vector react to the current stock status
"""

import time
import threading

import anki_vector
import iexstocksretriever
from anki_vector.events import Events
from anki_vector.util import degrees, distance_mm, speed_mmps

from vecstock import VecStock

wake_word_heard = False

def main():
    args = anki_vector.util.parse_command_args()

    # The robot drives straight, stops and then turns around
    with anki_vector.Robot(args.serial) as robot:
        check_stocks(robot)


def check_stocks(robot):
    allstocks = iexstocksretriever.getStocks(['ADBE', 'DOMO'])
    for stock in allstocks:
        performance_animation(robot, stock)

def performance_animation(robot, stock):
    print('__________Performance Animation__________')
    if stock.change > 0:
        print('__________Good Performance__________')
        robot.behavior.set_eye_color(hue=.20, saturation=1.0)
        robot.behavior.turn_in_place(degrees(360))
        robot.say_text(stock.name)
        robot.say_text(stock.current_price_string())
        robot.say_text(stock.change_string())
        robot.anim.play_animation('anim_pounce_success_02')
    else:
        print('__________Bad Performance__________')
        robot.behavior.set_eye_color(hue=0.00, saturation=1.0)
        robot.say_text(stock.name)
        robot.say_text(stock.current_price_string())
        robot.say_text(stock.change_string())
        print('Sleep 1 seconds...')
        time.sleep(1)


if __name__ == "__main__":
    main()
