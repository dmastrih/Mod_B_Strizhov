hello = "Start game"
start_1 = "-" * len(hello)
print(start_1)
print(hello)
print(start_1)

field = [["-"] * 3 for _ in range(3)]
count = 0

def show_field(f):
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i) + " " + " ".join(field[i]))

def users_input(f):
    place = input("Введите координаты :").split()
    if len(place) == 2:
        pass
    else:
        print("Введите 2 координаты!")
        return users_input(f)
    if place[0].isdigit() and place[1].isdigit():
        pass
    else:
        print("Введите числа!")
        return users_input(f)
    x,y = map(int,place)
    if not (0 <= x <= 2 and 0 <= y <= 2):
        print("Введите число в диапазоне от '0' до '2'")
        return users_input(f)
    if f[x][y] != "-":
        print("Клетка занята")
        return users_input(f)
    return x,y

def win_1(f,user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
            check_line(f[0][n], f[1][n], f[2][n], user) or \
            check_line(f[0][0], f[1][1], f[2][2], user) or \
            check_line(f[0][2], f[1][1], f[2][0], user):
            return True
    return False

while True:
    if count == 9:
        print("Ничья!")
        break
    if count % 2 == 0:
        user = "X"
    else:
        user = "O"
    print()
    show_field(field)
    print()
    x,y = users_input(field)
    field[x][y] = user
    if win_1(field,user):
        show_field(field)
        print(f"Выиграл {user}")
        break
    count += 1