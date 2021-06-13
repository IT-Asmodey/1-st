

# june = [25, 16, 28, 24, 17, 29, 16, 32, 30, 20, 18]
#
# def good_day(temperature):
#     count_good_days = 0
#     for temp in temperature:
#         if 20 <= temp <= 26:
#             count_good_days += 1
#
#     print("Комфортных дней в июне:", count_good_days)
# good_day(june)



# def first_task():
#     a = 1
#     b = 1.2
#     c = True
#     d = "1"
#
#     a = str(a)
#     b = str(b)
#     print(type(a), "\n", type(b),"\n", c, "\n", d)
#
# first_task()

# def second_task():
#     a = 1
#     b = 1
#
#     c = a = b
#
#     if c:
#         print("Правильно")
#     else:
#         print("Неправильно")
#
# second_task()


# def third_task():
#     a = input()
#     if len(a) > 2:
#
#         print(a[::3])
#
#         print(a[0] + a[-1])
#
#         print(a.upper())
#
#         print(a[::-1])
#
#         if a.isdigit():
#             print(True)
#         else:
#             print(False)
#     else:
#         print("В стоке не может быть меньше двух символов")
#
# third_task()


# def fourth_task():
#     s = "Hello word 1"
#
#     first_word = s[:s.find(' ')]
#     second_word = s[s.find(' ') + 1:]
#
#     print(second_word + ' ' + first_word)
#     print(s.replace("1", "one"))
# fourth_task()

# def fifth_task():
#     a=1
#     while a<=10:
#         b=1
#         while b<=10:
#             c=a*b
#             print(c, end=" ")
#             b+=1
#         print(" ")
#         a+=1
#
# fifth_task()

# def sixth_task():
#     a = int(input())
#     b = int(input())
#     for i in range((a + 1), b):
#         if i < 0:
#             print(i)
#
# sixth_task()

# седьмую не знаю как доделать
# def seventh_task():
#     a = int(input())
#
#     even_count = 0
#     odd_count = 0
#
#     summ = 0
#     while a != 0:
#         c = a % 10
#         if c % 2 == 0:
#             even_count += 1
#
#         else:
#             odd_count += 1
#
#         a = a // 10
#         summ += c
#
#     u = a % 10
#     print(a)
#     if even_count > odd_count:
#         print(summ)
#     else:
#         print(u)
#
# seventh_task()


# def eighth_task():
#     a = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 10]
#
#     b = int(input("введите число"))
#     c = int(input("введите кол во"))
#     for i in a:
#         if a.count(b) >= c:
#             print("число", b, "встречается в списке", a.count(b), "раз(а)")
#             break
#         else:
#             print("либо вашего числа нет с списке, либо ")
# eighth_task()


def calc():
    try:
        while (True):
            a = input("Введите ваше выражение (enter to exit) ")
            if a == "":
                break
            print(a + "=" + str(eval(a)))
    except TypeError:
        print("Нельзя складывать числа и буквы")
    except NameError:
        print("Нельзя складывать числа и буквы")
    except SyntaxError:
        print("Что то пошло не так")
    except ZeroDivisionError:
        print("На ноль делить нельзя")


calc()