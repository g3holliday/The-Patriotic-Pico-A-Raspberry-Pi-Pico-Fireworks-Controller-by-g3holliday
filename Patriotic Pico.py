import machine
p16 = machine.Pin(16)
servo = machine.PWM(p16)
servo.freq(50)
servo.duty_u16(9000)


from machine import Pin, PWM
servo=PWM(Pin(23),freq=50)
servo.duty(20)
servo.duty(70)
servo.duty(120)
