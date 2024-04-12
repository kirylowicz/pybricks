from pybricks.hubs import PrimeHub
from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.robotics import Car

# Set up all devices.
controller = XboxController()
drive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
steer = Motor(Port.B, Direction.COUNTERCLOCKWISE)
sensor = UltrasonicSensor(Port.C)
car = Car(steer, drive)
hub = PrimeHub()

# Initialize the flags
was_pressed = controller.buttons.pressed()
light = 0

# The main program starts here.
while True:
    pressed = controller.buttons.pressed()

    # Drive using the trigger inputs.
    brake, acceleration = controller.triggers()
    car.drive_power(acceleration - brake)

    # Steer with the left joystick.
    horizontal, vertical = controller.joystick_left()
    car.steer(horizontal * 0.50)


    # Press X to beep.
    if Button.X in pressed:
        hub.speaker.beep(100)

    # Press A to switch the lights on/off.
    if Button.A in pressed and not Button.A in was_pressed:
        light = 100 if light == 0 else 0
        sensor.lights.on(light)

    was_pressed = pressed
      