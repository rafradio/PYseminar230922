class ProgramClass:
    def __init__(this):
        this.dictWeekDay = {
            "1": "Понедельник",
            "2": "Вторник",
            "3": "Среда",
            "4": "Четверг",
            "5": "Пятница",
            "6": "Суббота",
            "7": "Воскресение"
        }
        this.strForInput = "Введите пожалуйста число: "

    def InputFunc(this):
        this.inputStr = input(this.strForInput)

        if this.inputStr in this.dictWeekDay.keys():
            return
        else:
            this.strForInput = "Введите пожалуйста еще раз: "
            this.InputFunc()

    def ExecFunc(this):
        if this.inputStr == "6" or this.inputStr == "7":
            print("Да, это выходной день - ", this.dictWeekDay[this.inputStr])
        else:
            print("Нет, это рабочий день - ", this.dictWeekDay[this.inputStr])

#   исполнение программы

exec = ProgramClass()
exec.InputFunc()
exec.ExecFunc()

