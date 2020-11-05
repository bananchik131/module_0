import numpy as np
number = np.random.randint(1,101)
def game_core(number):
	'''Сначала устанавливаем любое
random число в интервале от 0 до 100,
затем отнадываем это число, срезая
каждый раз интервал поиска
на половину.
	Функция принимает загаданное число и
возвращает число попыток'''
	count = 1 #счетчик попыток
	predict_list = [] #список предполагаемых значений
	count_ls = [] #список количества попыток
	np.random.seed(1) #фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
	for predict in range(1, 101):
		predict_list.append(predict) #добавляем  в список предполагаемых значений значения
	low = 0 #минимальное значение в искомом интервале
	high = len(predict_list)-1 #максимальное значение в искомом интервале
	mid = int(np.mean(predict_list)) #середина искомого интнрвала
	while low <= high: #сокращение интервала поиска
		count +=1 #увеличиваем попытку
		mid = int((low+high)/2) #определяем новую середину интервала
		if predict_list[mid] == number: #если угадали заканчиваем считать попытки
			return count 
		if predict_list[mid] > number:  
			high = mid - 1 #поиск ведется в левой части нового интервала
		else:
			low = mid + 1 #поиск ыедется в правой части интервала 
			count_ls.append(count) #добавляем количество попыток в список попыток
			break
	score = int(np.mean(count_ls)) #подсчитываем среднее количество совершенных попыток
	print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
	return score
game_core(number)