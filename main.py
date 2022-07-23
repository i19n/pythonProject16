import dateutil
from datetime import datetime,timedelta
now=datetime.datetime.now()
resembles=(input(''))
tomorrow=now+datetime.timedelta('hour'+1)
class FixDataFinder:    #Класс, объеденяющий в себе все функции, которые отвечают за фиксированную дату
    months= [
        'января',
        'февраля',
        'марта',
        'апреля',
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        'ноября',
        'декабря']
    week = ['понедельник','вторник','среду','четверг','пятницу','субботу','воскресенье']

    def mounth(str):
        if 'января' or 'январе' or 'январь' in resembles:
            return 1
        elif 'февраля' or 'феврале' or 'февраль' in resembles:
            return 2
        elif 'марта' or 'марте' or 'март' in resembles:
            return 3
        elif 'апреля' or 'апрель' or 'апреле' in resembles:
            return 4
        elif 'мая' or 'май' or 'мае' in resembles:
            return 5
        elif 'июня' or 'июне' or 'июнь' in resembles:
            return 6
        elif 'июля' or 'июль' or 'июле' in resembles:
            return 7
        elif 'августа' or 'август' or 'августе' in resembles:
            return 8
        elif 'сентября' or 'сентябре' or 'сентябрь' in resembles:
            return 9
        elif 'октябре' or 'октября' or 'октябрь' in resembles:
            return 10
        elif 'ноября' or 'ноябре' or 'ноябрь' in resembles:
            return 11
        elif 'декабрь' or 'декабре' or 'декабря' in resembles:
            return 12
        else:
            print(now)
        return 0

    def number(self, m):
        if (m=="первый") or  (m=="первого") in resembles:
                return "1"
        elif (m=="второй") or  (m=="второго") in resembles:
                return "2"
        elif (m=="третий") or (m=="третьего") in resembles:
                return "3"
        elif (m=="четвёртый") or (m=="четвёртого") in resembles:
                return "4"
        elif (m=="пятый") or (m=="пятого") in resembles:
                return "5"
        elif (m=="шестой") or (m=="шестого") in resembles:
                return "6"
        elif (m=="седьмой") or (m=="седьмого") in resembles:
                return "7"
        elif (m=="восьмой") or (m=="восьмого") in resembles:
                return "8"
        elif (m=="девятый") or (m=="девятого") in resembles:
                return "9"
        elif (m=="десятый") or (m=="десятого") in resembles:
                return "10"
        elif (m== "одиннадцатый") or (m=="одиннадцатого") in resembles:
                return "11"
        elif (m=="двенадцатый") or (m=="двенадцатого") in resembles:
                return "12"
        elif (m=="тринадцатый") or (m=="тринадцатого") in resembles:
                return "13"
        elif (m=="четырнадцатый") or (m=="четырнадцатого") in resembles:
                return "14"
        elif (m=="пятнадцатый") or (m=="пятнадцатогого") in resembles:
                return "15"
        elif (m=="шестнадцатый") or (m=="шестнадцатого") in resembles:
                return "16"
        elif (m == "семнадцатый") or (m=="семнадцатого")in resembles:
                return "17"
        elif (m=="восемнадцатый") or (m=="восемнадцатого")in resembles:
                return "18"
        elif (m=="девятнадцатый") or (m=="девятнадцатого") in resembles:
                return "19"
        elif (m=="двадцатого")  or (m=="двадцать") in resembles:
                return "20"
        elif (m=="тридцатого") or (m=="тридцать") in resembles:
                return "30"
        else:
            print(now)

    def chisla(self):
        if 'числа' in resembles:
            number(m)
            return m

    def updateDynTime(c):

        MESSAGE['DATE']['year'] = c.year
        MESSAGE['DATE']['month'] = c.month
        MESSAGE['DATE']['day'] = c.day
        MESSAGE['DATE']['hour'] = c.hour
        MESSAGE['DATE']['minute'] = c.minute

    def cherez(str):
        if 'через' in resembles:
            if 'день' in resembles:
                tomorrow = now + datetime.timedelta(days=1)
            elif 'час' in resembles:
                tomorrow=now+datetime.timedelta(hours=1)
            elif 'месяц' in resembles:
                tomorrow = now + datetime.timedelta(mounth=1)
            elif 'год' in resembles:
                tomorrow=now+datetime.timedelta(year=1)
            elif 'минуту' in resembles:
                tomorrow=now+datetime.timedelta(minute=1)
            elif 'два' or 'две' or '2' in resembles:
                if 'дня' in resembles:
                    tomorrow = now + datetime.timedelta(days=2)
                elif 'часа' in resembles:
                    tomorrow=now+datetime.timedelta(hours=2)
                elif 'месяца' in resembles:
                    tomorrow = now + datetime.timedelta(mounth=2)
                elif 'года' in resembles:
                    tomorrow=now+datetime.timedelta(year=2)
                elif 'минуты' in resembles:
                    tomorrow=now+datetime.timedelta(minute=2)
            elif '5' or 'пять':
                if 'дней' in resembles:
                    tomorrow=now+datetime.timedelta(days=5)
                elif 'часов' in resembles:
                    tomorrow=now+datetime.timedelta(hours=5)
                elif 'месяцев' in resembles:
                    tomorrow = now + datetime.timedelta(mounth=5)
                elif 'лет' in resembles:
                    tomorrow=now+datetime.timedelta(year=5)
                elif 'минут' in resembles:
                    tomorrow=now+datetime.timedelta(minute=5)
            elif 'неделю' in resembles:
                tomorrow=now+datetime.timedelta(days=7)
            elif '10' or 'десять' in resembles:
                if 'дней' in resembles:
                    tomorrow=now+datetime.timedelta(days=10)
                elif 'часов' in resembles:
                    tomorrow = now + datetime.timedelta(hours=10)
                elif 'месяцев' in resembles:
                    tomorrow = now + datetime.timedelta(mounth=10)
                elif 'лет' in resembles:
                    tomorrow = now + datetime.timedelta(year=10)
                elif 'минут' in resembles:
                    tomorrow = now + datetime.timedelta(minute=10)
        else:
            return None

    def space(str,ms):
        global ms
        while '  ' in ms:
            ms=ms.replace('  ',' ')

    def zavtra(self):
        if 'завтра' in ms:
            tomorrow=now+datetime.timedelta(days=1)
        else:
            tomorrow=now+datetime.timedelta(days=2)


try:
    ms=input()
    space(ms)
    MESSAGE = {'STATUS': None, 'DATE': {'year': None, 'month': None, 'day': None, 'hour': None, 'minute': None}, 'TEXT': None}

if 'через' in ms:  # здесь происходит обработка сообщения с предлогом через
    str = ms[ms.rfind('через') + 6:]
    list = str.split(' ')
    current_time = datetime.now()
    while list:
        dynamic_time(list[:2])
        list.remove(list[0])
        if list:
            list.remove(list[0])
    updateDynTime(current_time)

elif 'завтра' in msgin or 'послезавтра' in msgin:
    current_time = datetime.now()
    if 'завтра' in ms:
        current_time += timedelta(days=1)
    if 'послезавтра' in ms:
        current_time += timedelta(days=2)
    updateDynTime(current_time)


