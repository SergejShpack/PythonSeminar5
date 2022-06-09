#1 Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
# результат: "гдеж рабав копыто ф Абкн абрыволк олк"

exe_text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
sub_text = "абв" # удаляемая строка
len_remove = len(sub_text) # длина удаляемой строки

in_point = lambda: exe_text.lower().find(sub_text.lower())
remove_text = lambda in_txt, a, b : in_txt[:a] + (in_txt[(a + b):])

while in_point() != -1:
    #exe_text = exe_text[:in_point()] + exe_text[(in_point()+len_remove):]
    exe_text = remove_text (exe_text, in_point(), len_remove )
print(exe_text)

#2. Вы когда-нибудь играли в игру "Крестики-нолики"? 
# Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

from random import randint


game_board = [i for i in range(1, 10)] # игровое поле
prizer = 0
count_step = 0
priz_comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def print_game_board (game_board): #вывод поля на экран

    for i in range(0,7,3):
        print("|-----|-----|-----|")
        print(f"|  {game_board[i]}  |  {game_board[i+1]}  |  {game_board[i+2]}  |")
    print("|-----|-----|-----|")

def check_finish(game_b): # проверка финиша
 
    for var in priz_comb:
        if game_b[var[0]-1] == game_b[var[1]-1] == game_b[var[2]-1] == "X":
            return  -1
            
        elif game_b[var[0]-1] == game_b[var[1]-1] == game_b[var[2]-1] == "O":
            return 1

    if count_step == 9:
        return -2
        
    return 0

def check_input(tmp_step): # ввод хода и его проверка (проверяет не занята ли клетка и есть ли такая клетка.)
    
    if (tmp_step > 0) and (tmp_step < 10):
        if (game_board[tmp_step-1] != "X")and ((game_board[tmp_step-1] != "O")):
            return True
        
    return False

def step_zero():
    step_zero = randint(1,10)
    while check_input(step_zero) == False:
        step_zero = randint(1,10)
    return step_zero

def check_out ():

    if prizer == -1:
        print("\033[31m{}\033[0m".format("Крестики выиграли"))
        print_game_board (game_board)
        
    elif prizer == 1:
        print("\033[31m{}\033[0m".format("Нолики выиграли"))
        print_game_board (game_board)

    elif prizer == -2:
        print("\033[31m{}\033[0m".format("Ничья"))
        print_game_board (game_board)
        

print_game_board (game_board) # вывод доски

while prizer == 0: # играем пока не финиш

    step = int(input("\033[31m{}\033[0m".format("делайте ход. укажите номер клетки: ")))
    while check_input(step) == False: # проверка на валидность
        step = int(input("\033[31m{}\033[0m".format("делайте ход. укажите номер клетки: ")))

    game_board[step-1] = "X"
    count_step += 1
    
    print_game_board (game_board) # напечатали доску

    prizer = check_finish(game_board)
    if prizer !=0 :
        check_out ()
        break

    game_board[step_zero()-1] = "O" # сделали ход ноликом
    count_step += 1
    print("\033[31m{}\033[0m".format("Ход компьютера:"))   
    print_game_board (game_board)

    prizer = check_finish(game_board)
    if prizer !=0 :
        check_out ()
        break
    
    #3. Вот вам текст:
#«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, 
# кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. 
# Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. 
# Упал в нее. И снова вышел, короче, из подъезда. 
# Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. 
# Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. 
# В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. 
# Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

exe_text = ("Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. "
    "Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. "
    "Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. "
    "И снова вышел, короче, из подъезда. Ясен пень, в магазин. "
    "В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. "
    "Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. "
    "Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. "
    "В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. "
    "Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил")

trash_list = ["ну", "короче", "говоря", "эээээ", "кажется", "ээээ", "ясен пень", "эээ", "…", "в общем", "как бы", "..."]

in_point = lambda exe_txt, sub_txt: exe_txt.lower().find(sub_txt.lower())
remove_text = lambda in_txt, a, b : in_txt[:a] + (in_txt[(a + b):])

def remove_trash (full_text, sub_text):
    len_remove = len(sub_text)

    while in_point(full_text, sub_text) != -1:
        full_text = remove_text (full_text, in_point(full_text, sub_text), len_remove )  
    return full_text  
      

for word in trash_list: # убираем все лишнее

    exe_text = remove_trash (exe_text, f", {word},")
    exe_text = remove_trash (exe_text, f", {word}")
    exe_text = remove_trash (exe_text, f"{word},")
    exe_text = remove_trash (exe_text, f"{word}")

# уберем лишние пробелы и сделаем заглавными первые буквы предложения

temp_list = exe_text.split(".")


for i in range(0, len(temp_list)):
    temp_list[i] = temp_list[i].lstrip().capitalize()

exe_text = ""
exe_text = ". ".join(temp_list)

print(exe_text)