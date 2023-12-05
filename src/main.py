#     AUTOR:    BrincandoComIdeias
#     APRENDA:  https://cursodearduino.net/
#     SKETCH:   Servo Motor
#     DATA:     10/01/23

from tcs34725 import TCS34725
from machine import Pin
from machine import I2C
from utime import sleep_ms as delay

# Configurando pinos
pinSDA = Pin(16)
pinSCL = Pin(17)

pinLed = Pin(18, Pin.OUT)

# Configurando I2C0
i2c = I2C(0, scl=pinSCL, sda=pinSDA)
sensor = TCS34725(i2c)

# Valores calibrados para o BRANCO
calibR = 0.28
calibG = 0.36
calibB = 0.31

margem = 0.01

# Ligando LED
pinLed.value(False)
# Ativando o sensor
sensor.active(True)
# Configurando Sensor
sensor.integration_time(50)
sensor.gain(4)

delay(500)

while True:
    leitura = sensor.read(True)
        
    r = leitura[0]
    g = leitura[1]
    b = leitura[2]
    c = leitura[3]
    
    if c:
        rp = r / c
        gp = g / c
        bp = b / c
        
        cor = "NA"        
        if rp <= (calibR + margem) and gp <= (calibG + margem) and bp <= (calibB+ margem):
            cor = "Branco"
        elif rp > (calibR + margem) and gp <= (calibG + margem) and bp <= (calibB+ margem):
            cor = "Vermelho"
        elif rp <= (calibR + margem) and gp > (calibG + margem) and bp <= (calibB+ margem):
            cor = "Verde"
        elif rp <= (calibR + margem) and gp <= (calibG + margem) and bp > (calibB+ margem):
            cor = "Azul"
        elif rp <= (calibR + margem) and gp > (calibG + margem) and bp > (calibB+ margem):
            cor = "Azul Claro"
        elif rp > (calibR + margem) and gp > (calibG + margem) and bp <= (calibB+ margem):
            cor = "Amarelo"
        elif rp > (calibR + margem) and gp <= (calibG + margem) and bp > (calibB+ margem):
            cor = "Roxo"
        
        print(f"Red: {rp:.2f}% Green: {gp:.2f}% Blue: {bp:.2f}% Luz: {c:.2f} Cor: {cor}       ", end='\r') 
        delay(250)
    else:
        print("Iluminação insuficiente                                                         ", end='\r')
        delay(2000)
        
