def on_sound_loud():
    global licht
    licht = not (licht)
    if licht:
        mecanumRobotV2.set_led(LedCount.RIGHT, LedState.OFF)
        mecanumRobotV2.set_led(LedCount.LEFT, LedState.OFF)
    else:
        mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
        mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
item = 0
ms = 0
licht = False
input.on_sound(DetectedSound.LOUD, on_sound_loud)
input.set_sound_threshold(SoundThreshold.LOUD, 70)
irRemote.connect_infrared(DigitalPin.P0)
mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
mecanumRobotV2.state()
mecanumRobotV2.set_servo(30)

def on_forever():
    global ms, item
    ms = sonar.ping(DigitalPin.P15, DigitalPin.P10, PingUnit.CENTIMETERS)
    item = irRemote.return_ir_button()
    # basic.show_number(ms)
    if item == 21:
        mecanumRobotV2.set_servo(60)
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 30)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, 30)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, 30)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 30)
    elif item == 70:
        mecanumRobotV2.set_servo(0)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 30)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, 30)
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, 30)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 30)
    elif item == 67:
        mecanumRobotV2.set_servo(0)
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, 30)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, 30)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, 30)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, 30)
    else:
        mecanumRobotV2.state()
        mecanumRobotV2.set_servo(30)
basic.forever(on_forever)
