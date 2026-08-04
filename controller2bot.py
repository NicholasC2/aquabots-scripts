import pygame
import serial
import serial.tools.list_ports
import time

BAUD = 9600
PORT = None
SER = None

MOTOR_SPEED = 255

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

for port in serial.tools.list_ports.comports():
    try:
        ser = serial.Serial(port.device, BAUD, timeout=1)
        PORT = port.device
        print(f"Connected to {port.device}, {port.manufacturer} - {port.product}")
    except Exception as e:
        print(f"coulnt not connect to {port.device}, {port.manufacturer} - {port.product}: {e}")
        continue

if not PORT:
    print(f"no port found")
    pygame.quit()
    exit()

def send_command(motor_index, speed):
    if ser and ser.is_open:
        command = f"{motor_index},{int(speed * MOTOR_SPEED)}\n"
        ser.write(command.encode())
try:
    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()

        lh = controller.get_axis(0)
        if abs(lh) < 0.15:
            lh = 0
        lv = -controller.get_axis(1)
        if abs(lv) < 0.15:
            lv = 0

        rh = controller.get_axis(3)
        if abs(rh) < 0.15:
            rh = 0
        rv = -controller.get_axis(4)
        if abs(rv) < 0.15:
            rv = 0

        lt = controller.get_axis(2)
        rt = (controller.get_axis(5) + 1) / 2

        send_command(1, rt)
        time.sleep(1)

finally:
    if ser and ser.is_open:
        ser.close()
    pygame.quit()