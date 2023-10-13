let direction = 0
basic.showIcon(IconNames.Heart)
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
let ut = 0
radio.setGroup(99)
radio.setTransmitPower(5)
loops.everyInterval(100, function on_every_interval() {
    radio.sendValue("name", ut)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    xgo.execution_action(xgo.action_enum.Whirl)
    basic.pause(5000)
})
basic.forever(function on_forever() {
    
    ut = input.magneticForce(Dimension.X)
    if (input.magneticForce(Dimension.X) > 50) {
        xgo.execution_action(xgo.action_enum.Request_feeding)
        soundExpression.giggle.playUntilDone()
    } else {
        xgo.execution_action(xgo.action_enum.Crawl_forward)
        soundExpression.yawn.playUntilDone()
    }
    
    
    direction = input.compassHeading()
    if (direction < 45 || direction > 315) {
        basic.showString("N")
        xgo.move_xgo(xgo.direction_enum.Forward, 50)
    } else if (direction < 135 && direction > 45) {
        basic.showString("X")
        xgo.move_xgo(xgo.direction_enum.Forward, 0)
        xgo.rotate(xgo.rotate_enum.Left, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.Left, 0)
    } else if (direction < 315 && direction > 225) {
        basic.showString("X")
        xgo.move_xgo(xgo.direction_enum.Forward, 0)
        xgo.rotate(xgo.rotate_enum.Right, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.Right, 0)
    } else {
        basic.showString("X")
        xgo.rotate(xgo.rotate_enum.Right, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.Right, 0)
    }
    
    
    direction = input.compassHeading()
    if (direction < 45 || direction > 315) {
        basic.showString("N")
        xgo.move_xgo(xgo.direction_enum.Forward, 50)
    } else if (direction < 135 && direction > 45) {
        basic.showString("X")
        xgo.move_xgo(xgo.direction_enum.Forward, 0)
        xgo.rotate(xgo.rotate_enum.Left, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.Left, 0)
    } else if (direction < 315 && direction > 225) {
        basic.showString("X")
        xgo.move_xgo(xgo.direction_enum.Forward, 0)
        xgo.rotate(xgo.rotate_enum.Right, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.Right, 0)
    } else {
        basic.showString("X")
        xgo.rotate(xgo.rotate_enum.Right, 50)
        basic.pause(500)
        xgo.rotate(xgo.rotate_enum.Right, 0)
    }
    
})
