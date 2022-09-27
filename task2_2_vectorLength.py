import os
import math

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class Coordinates:
    def __init__(this, dotname):
        this.strLegend = [f"Введите координату X для {dotname} точки: ", f"Введите координату Y для {dotname} точки: "]
        this.counterInput = 0
        this.InputFunc()

    def InputFunc(this):
        while this.counterInput < 2:
            try:
                inputStr = float(input(this.strLegend[this.counterInput]))
            except:
                print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
            else:
                if this.counterInput == 0: this.X = inputStr
                if this.counterInput == 1: this.Y = inputStr
                this.counterInput += 1

class VectorLength:
    def __init__(this, firstDot, secondtDot):
        this.firstDot = firstDot
        this.secondtDot = secondtDot
        this.FindLength()

    def FindLength(this):
        length = math.sqrt((this.secondtDot.X - this.firstDot.X)**2 + (this.secondtDot.Y - this.firstDot.Y)**2)
        length = round(length, 2)
        print(f"Длина вектора между точками равна {length}")

initClear = InitSets()
firstDot = Coordinates("первой")
secondtDot = Coordinates("второй")
execModule = VectorLength(firstDot, secondtDot)