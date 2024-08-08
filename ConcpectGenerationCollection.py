# import time
#
# start_time = time.time()
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# res = (x ** 100 for x in my_numbers)

# for elem in res:
#     print(elem)
# print('Еще разок')
# 1
# 1606938044258990275541962092341162602522202993782792835301376
# 1
# 7888609052210118054117285652827862296732064351090230047702789306640625
# 265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001
# 1267650600228229401496703205376
# 653318623500070906096690267158057820537143710472954871543071966369497141477376
# Еще разок

# print(res)
# <generator object <genexpr> at 0x0000026E00A1C380>

# for elem in res:
#     print(elem)

# res = [x ** 3000 for x in my_numbers]
# print(res)
# for elem in res:
#     print(elem)
#
# finish_time = time.time()
# print(f'Время в миллисек: {(finish_time - start_time) * 1000}')
# res = (x ** 3000 for x in my_numbers)
# Время в миллисек: 4.242658615112305
# res = [x ** 3000 for x in my_numbers]
# Время в миллисек: 6.291627883911133

l1 = [1, 5, 9, 29, 4]
l2 = [5, 2, 9, 1, 2]

ran = range(10, 30)
zp = zip(l1, l2)
mp = map(str, l1)

print(ran, zp, mp)
# range(10, 30) <zip object at 0x000001AFFA34F880> <map object at 0x000001AFFA39D810>
print(list(ran))
print(list(zp))
print(list(mp))
# =>
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# [(1, 5), (5, 2), (9, 9), (29, 1), (4, 2)]
# ['1', '5', '9', '29', '4']