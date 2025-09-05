basic.show_string("Z sender")
input.set_accelerometer_range(AcceleratorRange.FOUR_G)
radio.set_group(42)

def on_forever():
    radio.send_number(input.acceleration(Dimension.Z))
basic.forever(on_forever)
