# FFXIV Ishgard auto craft

*Simple script to automate procces of crafting dozens of same items in ishgard*

__Using this script might violate ToS so don't get banned ^^__

# How to use

## Required preparations

* Install [python 3](https://www.python.org/downloads/).
* Install [vJoy](https://github.com/shauleiz/vJoy).
* git clone [pyvjoy](https://github.com/tidzo/pyvjoy) to dir with main.py and copy vJoy SDK DLL to pyvjoy folder or change path in _sdk.py.

## Prepare game

* Add your crafting macros to hotbar in RT B slot. (I'm used to nintendo button layout, so B button is called A in the code)
If your want to use another slot -- by default ABXY button are first 4 in vJoy.
* In system configuration -> gamepad setting, select vJoy Device.
* Open crafting log and select the recipe you want to craft by clicking it, so controller button suggestions disappears.


## Launch

* In main.py change constants if needed (time your macro requires, button numbers for RT and B, button press delay)
* Launch main.py and use craft(n) to start the craft cycle.
* Select window with the game so it gets input signals from vJoy.
* Enjoy your free time without need to start croft every minute. (:
