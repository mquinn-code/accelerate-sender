basic.showString("Z sender")
input.setAccelerometerRange(AcceleratorRange.FourG)
radio.setGroup(42)
basic.forever(function on_forever() {
    radio.sendNumber(input.acceleration(Dimension.Z))
})
