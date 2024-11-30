from datetime import datetime,date,time, timedelta
import locale
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

print("Formatação de data")
agora=datetime.now()
data_formatada=agora.strftime("%d/%m/%Y ")
print(f"A data formatada é: {data_formatada}")

print("Formatação de hora")
agora=datetime.now()
hora_formatada=agora.strftime("%H:%M:%S")
print(f"A hora formatada é: {hora_formatada}")

print("Definir local/região/pais")   #erro line 36!!!!   dando erro line 608?

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
data_hora_no_pais_do_Locale = datetime.now()
data_formatada_BR=data_hora_no_pais_do_Locale.strftime("%x")
hora_formatada_BR=data_hora_no_pais_do_Locale.strftime("%X")
print(f"A data formatada para PT-BR é{data_formatada_BR}")
print(f"A data formatada para PT-BR é{hora_formatada_BR}")