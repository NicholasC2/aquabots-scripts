import pygame
import serial
import serial.tools.list_ports

BAUD = 9600

pygame.init()
pygame.joystick.init()

if (pygame.joystick.get_count() == 0):
    print("Error: No Controller is connected!")
    pygame.quit()
    exit()

print("Using controller 0")
controller = pygame.joystick.Joystick(0)
controller.init()

print(f"Controller Name: {controller.get_name()}")
print(f"Buttons: {controller.get_numbuttons()}, Axis: {controller.get_numaxes()}")

# for port in serial.tools.list_ports.comports():
#     print(port.device)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit()

    lh = controller.get_axis(0)
    lv = controller.get_axis(1)

    rh = controller.get_axis(3)
    rv = controller.get_axis(4)

    lt = controller.get_axis(2)
    rt = controller.get_axis(5)

    print(f"left stick\nhorizontal: {lh}\nvertical: {lv}\nright stick\nhorizontal: {rh}\nvertical: {rv}\nlt: {lt}\nrt: {rt}")

    clock.tick(60)