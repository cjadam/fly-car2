basic.show_icon(IconNames.HEART)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
    SoundExpressionPlayMode.UNTIL_DONE)
music.start_melody(music.built_in_melody(Melodies.ODE),
    MelodyOptions.FOREVER_IN_BACKGROUND)

def on_forever():
    if input.is_gesture(Gesture.LOGO_UP) == False or input.is_gesture(Gesture.SHAKE) == True:
        SuperBitV2.motor_stop_all()
    else:
        if SuperBitV2_Digital.ultrasonic(SuperBitV2_Digital.mwDigitalNum.P10P9) < 30 or SuperBitV2_Digital.IR(SuperBitV2_Digital.mwDigitalNum.P4P6,
            SuperBitV2_Digital.enObstacle.OBSTACLE):
            basic.show_arrow(ArrowNames.SOUTH)
            SuperBitV2.motor_run_dual(SuperBitV2.enMotors.M1, -119, SuperBitV2.enMotors.M3, -144)
        else:
            basic.show_arrow(ArrowNames.NORTH)
            SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.RED))
            SuperBit.RGB_Program().show()
            SuperBit.motor_run(SuperBit.enMotors.M1, 255)
            SuperBit.motor_run(SuperBit.enMotors.M3, 255)
            basic.pause(2000)
            SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.GREEN))
            SuperBit.motor_run(SuperBit.enMotors.M1, -255)
            SuperBit.motor_run(SuperBit.enMotors.M3, -255)
            basic.pause(2000)
            SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.BLUE))
            SuperBit.motor_run(SuperBit.enMotors.M1, -255)
            SuperBit.motor_run(SuperBit.enMotors.M3, 255)
            basic.pause(1000)
            SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.VIOLET))
            SuperBit.motor_run(SuperBit.enMotors.M1, 255)
            SuperBit.motor_run(SuperBit.enMotors.M3, -255)
            basic.pause(1000)
            SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.RED))
            SuperBit.motor_run(SuperBit.enMotors.M1, -255)
            SuperBit.motor_run(SuperBit.enMotors.M3, 255)
            basic.pause(1000)
            SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.GREEN))
            SuperBit.motor_run(SuperBit.enMotors.M1, 255)
            SuperBit.motor_run(SuperBit.enMotors.M3, -255)
            basic.pause(1000)
basic.forever(on_forever)
