basic.showIcon(IconNames.Heart)
music.playSoundEffect(music.builtinSoundEffect(soundExpression.spring), SoundExpressionPlayMode.UntilDone)
music.setVolume(62)
music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.ForeverInBackground)
basic.forever(function on_forever() {
    if (SuperBitV2_Digital.Ultrasonic(SuperBitV2_Digital.mwDigitalNum.P10P9) < 32) {
        basic.showArrow(ArrowNames.South)
        SuperBitV2.MotorRunDual(SuperBitV2.enMotors.M1, -119, SuperBitV2.enMotors.M3, -144)
        basic.pause(200)
        SuperBitV2.MotorRunDual(SuperBitV2.enMotors.M1, -132, SuperBitV2.enMotors.M3, 132)
    } else {
        SuperBit.RGB_Program().showColor(neopixel.colors(NeoPixelColors.Purple))
        SuperBit.RGB_Program().show()
        basic.showArrow(ArrowNames.North)
        SuperBitV2.MotorRunDual(SuperBitV2.enMotors.M1, 169, SuperBitV2.enMotors.M3, 193)
    }
    
})
