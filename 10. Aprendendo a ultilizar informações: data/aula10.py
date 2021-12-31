# TRABALAHNDO COM DATAS

from datetime import date, time, datetime, timedelta

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2025, 6, 20, 15, 10, 5)
    print(data_criada)
    data_string = '01/01/2001'
    nova_data = data_string - timedelta(days=365)
    print(nova_data)

def trabalhando_date():
    data_atual = date.today()
    date_atual_str = data_atual.strftime('%A de %B de %Y')
    print(type(date_atual))
    print(date_atual_str)
    print(type(date_atual_str))

def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_date()
    #trabalhando_time()
    trabalhando_datetime()
