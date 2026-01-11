
licht = False
input.set_sound_threshold(SoundThreshold.LOUD, 70)
mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
for index in range(1000):
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 30)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 30)
for index2 in range(1000):
    mecanumRobotV2.state()
    mecanumRobotV2.set_servo(30)
# ------------------------------------------------------------
def on_sound_loud():
    global licht
    licht = not (licht)
    basic.show_leds("""
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            """)
    if licht:
        basic.clear_screen()
def on_forever():
    on_sound_loud()
    for index3 in range(100000):
        mecanumRobotV2.set_servo(60)
    for index4 in range(100000):
        mecanumRobotV2.set_servo(30)
    for index5 in range(100000):
        mecanumRobotV2.set_servo(0)
    for index6 in range(100000):
        mecanumRobotV2.set_servo(30)
basic.forever(on_forever)
