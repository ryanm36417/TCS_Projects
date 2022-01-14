from turtle import*

num = 2

# if num == 1:
#     print("monday")
# elif num == 2:
#     print("tuesday")
# elif num == 3:
#     print("wednesday")


match num:
    case 0:
        print("monday")
    case 1:
        print("tuesday")
    case 2:
        print("wednesday")
    case 3:
        print("thursday")
    case 4:
        print("friday")
    case 5:
        print("saturday")
    case 6:
        print("sunday")


# speed(0)
#
# def make_square():
#     color("blue")
#     begin_fill()
#     circle(100)
#     end_fill()
#     for i in range(14):
#         make_square()
#
# make_square()
#
#
# mainloop()