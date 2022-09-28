import os
import math

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class Quater:
    def __init__(this):
        this.strLegend = "Введите пожалуйста целое число от 1 до 4: "
        this.counterInput = 0
        this.InputFunc()

    def InputFunc(this):
        while True:
            try:
                inputStr = int(input(this.strLegend))
            except:
                print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
            else:
                if inputStr >= 1 and inputStr <= 4: 
                    this.Quater = inputStr
                    return
                else: print("Число не в диапазоне")

    def FindQuater(this):
        match this.Quater:
            case 1:
                print("Для первой четверти координаты по X - от 0 до +бескончноси; по Y - от 0 до +бескончноси")
            case 2:
                print("Для второй четверти координаты по X - от 0 до -бескончноси; по Y - от 0 до +бескончноси")
            case 3:
                print("Для третьей четверти координаты по X - от 0 до -бескончноси; по Y - от 0 до -бескончноси")
            case 4:
                print("Для второй четверти координаты по X - от 0 до +бескончноси; по Y - от 0 до -бескончноси")

initClear = InitSets()
data = Quater()
print(f"Вы ввели {data.Quater} четверть")
data.FindQuater()

