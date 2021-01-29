import board
import digitalio
import mido

button = digitalio.DigitalInOut(board.C0)
button.direction = digitalio.Direction.INPUT

button.value

print(button.value)

msg = mido.Message('control_change', value=1)

port = mido.open_output()
port.send(msg)