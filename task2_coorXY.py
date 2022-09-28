class ProgramXY:
    def __init__(this):
        this.strLegend = ["Введите пожалуйста координату для X: ", "Введите пожалуйста координату для Y: "]
        this.counterInput = 0
        this.coorXY = []

        this.InitClear()

    def InitClear(this):
        import os
        clear = lambda: os.system("CLS")
        clear()

    def InputFunc(this):
        while this.counterInput < 2:
            this.inputStr = input(this.strLegend[this.counterInput])
            if this.inputStr.lstrip("-").isdigit() and this.inputStr != "0":
                this.coorXY.append(int(this.inputStr))
                this.counterInput += 1
            else:
                print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
            this.InputFunc()
        return

    def CheckQuater(this):
        check = this.coorXY[0] * this.coorXY[1]
        if check > 0:
            if this.coorXY[0] > 0:
                print(f"Ваши координаты x: {this.coorXY[0]}, y: {this.coorXY[1]} находятся в первой четверти")
            else:
                print(f"Ваши координаты x: {this.coorXY[0]}, y: {this.coorXY[1]} находятся в третьей четверти")
        else:
            if this.coorXY[0] > 0:
                print(f"Ваши координаты x: {this.coorXY[0]}, y: {this.coorXY[1]} находятся в четвертой четверти")
            else:
                print(f"Ваши координаты x: {this.coorXY[0]}, y: {this.coorXY[1]} находятся во второй четверти")



#   исполнение программы

exec = ProgramXY()
exec.InputFunc()
exec.CheckQuater()