# user_index = [item for item in range(1,11)]
# print(user_index)

# # çıktısı aşağıdaki gibi
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# user_index = [num for num in range(1,11) if num % 2 == 0]
# print(user_index)

# #çıktısı aşağıdaki gibi olur
# # [2, 4, 6, 8, 10]

# short if ve short for ile 1'den 10'a kadar liste oluştur ve bunlardan sadece 2 ile tam bölünenleri 10 ile çarpıp ekrana yazsın

forTwo = [num * 10 for num in range(1,11) if num % 2 == 0]
print(forTwo)

# çıktısı aşağıdaki gibi olur
# [20, 40, 60, 80, 100]

