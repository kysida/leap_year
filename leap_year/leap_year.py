#_*_ coding=utf-8
__author__ = 'kysida'
#定义函数
def leap_year(year):
    if year % 4 == 0:
        if (year / 100) % 4 == 0:
            return "the year is a leap year"

    return "the year is not a leap year"
#主程序
if __name__ == '__main__':
    year = int(raw_input("Please input the year:"))
    print leap_year(year)