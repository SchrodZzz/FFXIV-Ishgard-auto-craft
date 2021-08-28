import pyvjoy
import time
import random

# time constants
MACRO_DURATION = 40.5
BUTTON_DELAY = 0.5

# location of the macro in your hotbar
A = 4
RT = 8

print("> Imports are done")

j = pyvjoy.VJoyDevice(1)

print("> Joy is set")

def on(num):
    j.set_button(num, 1)

def off(num):
    j.set_button(num, 0)

def press(num, delay=BUTTON_DELAY):
    time.sleep(delay)
    print(">> Press on button number %s" % num)
    on(num)
    time.sleep(BUTTON_DELAY)
    off(num)

def press_with_RT(num, delay=BUTTON_DELAY):
    time.sleep(delay)
    print(">>> Press %s" % RT)
    on(RT)
    press(num)
    off(RT)
    print(">>> Unpress %s" % RT)

def wait_macro(t=MACRO_DURATION):
    bonus = random.randint(1, 25) / 10
    print(">>> Wait Macro to complete for %s sec" % (t + bonus))
    time.sleep(t+bonus)


def craft(n=20):
    minutes_to_finish = ((MACRO_DURATION + 5 * 2 * BUTTON_DELAY) * n / 60)
    print("> Expected time to complete: %.2f min" % minutes_to_finish)
    print("> Wait 5 sec to focus game screen")
    time.sleep(5)
    for i in range(n):
        print("> Starting craft %s/%s" % (i+1, n))
        for i in range(3):
            press(A)
        press_with_RT(A)
        wait_macro()
    print("> Craft is complete!!!")


print("INFO: Use craft(n) to start crafting, dont forget to open crafting log and focus on the recipe")
