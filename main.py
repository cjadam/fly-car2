basic.show_icon(IconNames.HEART)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
    SoundExpressionPlayMode.UNTIL_DONE)
music.set_volume(62)
music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
    MelodyOptions.FOREVER_IN_BACKGROUND)

def on_forever():
    if SuperBitV2_Digital.ultrasonic(SuperBitV2_Digital.mwDigitalNum.P10P9) < 32:
        basic.show_arrow(ArrowNames.SOUTH)
        SuperBitV2.motor_run_dual(SuperBitV2.enMotors.M1, -119, SuperBitV2.enMotors.M3, -144)
        basic.pause(200)
        SuperBitV2.motor_run_dual(SuperBitV2.enMotors.M1, -132, SuperBitV2.enMotors.M3, 132)
    else:
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.PURPLE))
        SuperBit.RGB_Program().show()
        basic.show_arrow(ArrowNames.NORTH)
        SuperBitV2.motor_run_dual(SuperBitV2.enMotors.M1, 169, SuperBitV2.enMotors.M3, 193)
basic.forever(on_forever)
