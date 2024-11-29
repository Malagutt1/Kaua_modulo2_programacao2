from datetime import datetime,date,time 

""" Pytz é uma biblioteca no Python que permite calcular fuso horarios e resolver problemas com 
horarios amniguos no final do horario de verão"""

"""O tzdata é um 'pacote' de dados do puthon que fornece dados de fuso horario IANA. 
Ele é principalmente usado pelo modulo 'zoneinfo' da biblioteca padrão, mas também pode
ser usado como fonte de dados de suso horario para outras bibliotecas de fuso horario"""
###pip install pytz   || pip install tzdata

"""Obtenha a data e hora atuais do computadoir em que você esta usando, e as imprima no terminal do VScode"""
print("obeter data e hora")
data_hora=datetime.now()
print(data_hora)

print("obeter data")
data=datetime.now().date()
print(data)

print("represente o horario '14:30:59' ")
horario_especifico=time(14, 30, 59)
print(horario_especifico)