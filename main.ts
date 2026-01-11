let licht = false
input.setSoundThreshold(SoundThreshold.Loud, 70)
mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
for (let index = 0; index < 1000; index++) {
    mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, 30)
    mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, 30)
}
for (let index2 = 0; index2 < 1000; index2++) {
    mecanumRobotV2.state()
    mecanumRobotV2.setServo(30)
}
//  ------------------------------------------------------------
function on_sound_loud() {
    
    licht = !licht
    basic.showLeds(`
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    if (licht) {
        basic.clearScreen()
    }
    
}

basic.forever(function on_forever() {
    on_sound_loud()
    for (let index3 = 0; index3 < 100000; index3++) {
        mecanumRobotV2.setServo(60)
    }
    for (let index4 = 0; index4 < 100000; index4++) {
        mecanumRobotV2.setServo(30)
    }
    for (let index5 = 0; index5 < 100000; index5++) {
        mecanumRobotV2.setServo(0)
    }
    for (let index6 = 0; index6 < 100000; index6++) {
        mecanumRobotV2.setServo(30)
    }
})
