import urllib.request
import matplotlib.pyplot as plt

try:
    file = urllib.request.urlopen("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat").read().decode('utf-8').split("\n")[1:]
except Exception as error:
    print(f"При открытии файла возникла ошибка: {str(error)}")

pension = []
date_y = []

try:
    for st in file:
        st = st.split(",")
        if st[0] == "Средняя пенсия":
            if st[1] == 'Забайкальский край':
                date=st[2].split("-")
                if date[0] == '2018':
                    pension.append(int(st[3]))
                    date_y.append(int(date[1]))
except Exception as error:
    print(f"При обработке файла возникла ошибка: {error}")

try:
    print(f"Средняя пенсия в Забайкальском крае за 2018 год составляет: {round(sum(pension)/len(pension),1)}")
except Exception as error:
    print(f"При работе с обработанными данными возникла ошибка: {error}")

try:
    plt.plot(date_y, pension) #Построение линейного графика
    plt.title("График изменения средней пенсии") #Добавление заголовка
    plt.ylabel("Cредняя пенсия за месяц") #Подпись для оси y
    plt.xlabel("Месяц") #для x
    plt.grid(True) #Добавил сетку
    plt.show() #Показ графика
except Exception as error:
    print(f"При постороении графика возникла ошибка: {error}")
