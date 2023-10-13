direction = 0
basic.show_icon(IconNames.HEART)
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
ut = 0
radio.set_group(99)
radio.set_transmit_power(5)

def on_forever():
    global ut
    ut = input.magnetic_force(Dimension.X)
    if input.magnetic_force(Dimension.X) > 50:
        xgo.execution_action(xgo.action_enum.REQUEST_FEEDING)
        soundExpression.giggle.play_until_done()
    else:
        xgo.execution_action(xgo.action_enum.CRAWL_FORWARD)
        soundExpression.yawn.play_until_done()
    global direction
    direction = input.compass_heading()
    if direction < 45 or direction > 315:
        basic.show_string("N")
        xgo.move_xgo(xgo.direction_enum.FORWARD, 50)
    elif direction < 135 and direction > 45:
        basic.show_string("X")
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
        xgo.rotate(xgo.rotate_enum.LEFT, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.LEFT, 0)
    elif direction < 315 and direction > 225:
        basic.show_string("X")
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
        xgo.rotate(xgo.rotate_enum.RIGHT, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.RIGHT, 0)
    else:
        basic.show_string("X")
        xgo.rotate(xgo.rotate_enum.RIGHT, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.RIGHT, 0)
    global direction
    direction = input.compass_heading()
    if direction < 45 or direction > 315:
        basic.show_string("N")
        xgo.move_xgo(xgo.direction_enum.FORWARD, 50)
    elif direction < 135 and direction > 45:
        basic.show_string("X")
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
        xgo.rotate(xgo.rotate_enum.LEFT, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.LEFT, 0)
    elif direction < 315 and direction > 225:
        basic.show_string("X")
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
        xgo.rotate(xgo.rotate_enum.RIGHT, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.RIGHT, 0)
    else:
        basic.show_string("X")
        xgo.rotate(xgo.rotate_enum.RIGHT, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.RIGHT, 0)

def on_every_interval():
    radio.send_value("name", ut)
loops.every_interval(100, on_every_interval)

def on_logo_touched():
    xgo.execution_action(xgo.action_enum.WHIRL)
    basic.pause(5000)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

basic.forever(on_forever)