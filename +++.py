

june = [25, 16, 28, 24, 17, 29, 16, 32, 30, 20, 18]

def good_day(temperature):
    count_good_days = 0
    for temp in temperature:
        if 20 <= temp <= 26:
            count_good_days += 1

    print("Комфортных дней в июне:", count_good_days)
good_day(june)
