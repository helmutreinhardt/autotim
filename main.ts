let item = 0
let ms = 0
let licht = false
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    
    licht = !licht
    if (licht) {
        mecanumRobotV2.setLed(LedCount.Right, LedState.OFF)
        mecanumRobotV2.setLed(LedCount.Left, LedState.OFF)
    } else {
        mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
        mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
    }
    
})
input.setSoundThreshold(SoundThreshold.Loud, 70)
irRemote.connectInfrared(DigitalPin.P0)
mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
mecanumRobotV2.state()
mecanumRobotV2.setServo(30)
basic.forever(function on_forever() {
    
    ms = sonar.ping(DigitalPin.P15, DigitalPin.P10, PingUnit.Centimeters)
    item = irRemote.returnIrButton()
    //  basic.show_number(ms)
    if (item == 21) {
        mecanumRobotV2.setServo(60)
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, 30)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, 30)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, 30)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, 30)
    } else if (item == 70) {
        mecanumRobotV2.setServo(0)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, 30)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, 30)
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, 30)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, 30)
    } else if (item == 67) {
        mecanumRobotV2.setServo(0)
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, 30)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, 30)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, 30)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, 30)
    } else {
        mecanumRobotV2.state()
        mecanumRobotV2.setServo(30)
    }
    
})
