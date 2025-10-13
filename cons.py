# import math

# # 1-ші нұсқа
# x, y, z = 2, 6, 7
# a1 = math.sqrt(abs(x - 1)**3 + abs(y)) / (x**2 + y**2/4)
# b1 = x * (math.atan(z) + math.e**(-y - 3))
# print("1:", a1, b1)

# # 2-ші нұсқа
# x, y, z = 5, 1, 4
# a2 = 3.5 * math.e**(-y - 1) / (1 + x * abs(y - math.tan(z)))
# b2 = abs(y - x) + (y - x)**2 / abs(y - z)
# print("2:", a2, b2)

# # 3-ші нұсқа
# x, y, z = 1, 12, 6
# a3 = (x + y) * (x**2 + 4) / (math.e**(x - y) + 2 * abs(x + y))
# b3 = (1 + math.cos(y - 2)) / (x**4 + math.sin(z)**2)
# print("3:", a3, b3)

# # 4-ші нұсқа
# x, y, z = 3, 5, 2
# a4 = (1 + y) * (x + y**2) / (abs(x - y) + (x**2 + y**2))
# b4 = 1 + math.sin(math.tan(y**2) + 3.5)
# print("4:", a4, b4)

# # 5-ші нұсқа
# x, y, z = 5, 7, 8
# a5 = (0.5 * math.tan(x + 2)) / (1 - (x**2 / (3 + abs(y))))
# b5 = 1 + math.sqrt(x**2 + 1) / (y + 2)
# print("5:", a5, b5)

# # 6-ші нұсқа
# x, y, z = 3, 4, 5
# a6 = (2 + math.sin(abs(y))) / (3 - (math.sqrt(x**2 + 1)) / (y + 2))
# b6 = math.cos(x**2 * math.atan(z))
# print("6:", a6, b6)


# # 7-ші нұсқа
# x, y, z = 5, 3, 17
# a7 = math.log(abs(y - math.sqrt(abs(x))))
# b7 = x - (z**7 / math.factorial(5))
# print("7:", a7, b7)


# # 8-ші нұсқа
# x, y, z = 7, 4, 8
# a8 = math.sin(3 * x + y + 15 * z) / math.sqrt(12 * x**3 + 6 * y**2 + z**3 + x**2)
# b8 = math.tan(7 * x**2 + math.e**(3 * y))
# print("8:", a8, b8)


# # 9-шы нұсқа
# x, y, z = 17, 16, 15
# a9 = abs(math.sin(8 * y) + 17 * x) / math.sqrt(1 - math.sin(4 * y) * math.cos(z)**2)
# b9 = math.sqrt(3 * z**2 / (3 + math.tan(3 * x) - math.sin(5 * y)))
# print("9:", a9, b9)


# # 10-шы нұсқа
# x, y, z = 6, 2, 8
# a10 = x**(2 * y) + (3 * z * (math.cos(y))**3) / (z**2 + x * y)
# b10 = abs(x - y)**2 / (3 * z + math.cos(x * z))
# print("10:", a10, b10)


# # 11-ші нұсқа
# x, y, z = 4, 3, 2
# a11 = 10 * math.log(x**2 - math.sqrt(abs(math.cos(y))))
# b11 = 2 * x**2 + (y**2 - 3 * z) / (3 * x + y)
# print("11:", a11, b11)


# # 12-ші нұсқа
# x, y, z = 4, 5, 7
# a12 = (math.cos(z**2 * x) + 5 * math.sin(3 * (x - y))) / math.log(abs(2 * z + 3))
# b12 = math.sin(math.sqrt((x**2 + 5 * y**3) / (math.sqrt(3 * z + x**2))))
# print("12:", a12, b12)


# # 13-ші нұсқа
# x, y, z = 5, 6, 7
# a13 = math.tan((x + y)**2 - math.cos(z)**2 / (math.tan(z)**2))
# b13 = math.log(x**2 + y**2 - z**2 + y)
# print("13:", a13, b13)

# # 14-ші нұсқа
# x, y, z = 8, 9, 10
# a14 = (y / math.sin(x) + y / (math.sin(2 * x) - 3 * math.cos(z))) * math.e**(5 * x)
# b14 = (5 - math.e**(-z)) / (y + x**2 * abs(z**2 - math.tan(z)))
# print("14:", a14, b14)

# # 15-ші нұсқа
# x, y, z = 9, 10, 11
# a15 = abs(y**2 + 1) + (x / (math.sin(z - math.e**x + 5)))
# b15 = (x - math.cos(z) * (y + z)) / (5 + math.log(y) - 5 * x / math.sqrt(7))
# print("15:", a15, b15)


# def inc(a,b):
#     return a + b

# print(inc(1,2))


# def numbOr(a):
#     if a % 2  == 0:
#         return "tak"
#     else:
#         return "no"
    
    
# print(numbOr(2))


# def biggerNum(a):
#     d = 0
#     for i in a:
#         if i > d:
#             d = i

#     return d

# print(biggerNum([1,2,3,4]))


# text = "Привет"
# count_letters = sum(1 for char in text if char.isalpha())
# print(f"Количество букв: {count_letters}")

# # 5. 
# N = 10
# s = 0
# for i in range(1, N+1):
#     s += i
# print("5:", s)

# # 6.
# word = "Алматы"
# print("6:", word[::-1])

# # 7.
# arr = [5, 2, 9, 1]
# print("7:", min(arr))

# # 8. 
# arr = [5, 2, 9, 1]
# arr.sort()
# print("8:", arr)

# # 9.
# a = int(input("Сан енгізіңіз: "))

# if a < 2:
#     print("Жай сан емес")
# else:
#     is_prime = True
#     for i in range(2, int(a**0.5) + 1):
#         if a % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("Жай сан")
#     else:
#         print("Жай сан емес")


# # 10.
# text = "Мен Python үйреніп жүрмін"
# print("10:", len(text.split()))

# # 11. Матрицаны транспонирлеу
# matrix = [[1,2,3],
#           [4,5,6]]
# transposed = []

# for i in range(len(matrix[0])): 
#     row = []

#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transposed.append(row)
# print("11:", transposed)

# # 2. 2-ден кем емес бүтін сан берілген. Оның 1-ден басқа ең кіші табиғи бөлгішін табу.
# n = 21
# i = 2
# while n % i != 0:
#     i += 1
# print("Ең кіші бөлгіш:", i)


# # 3. 1-10 сандарының кері мәнін шығару
# for i in range(1, 11):
#     a=2
#     print(f"{i} = {a*i}")


# # 4. Тізбектегі барлық сандардың қосындысы және саны
# s = 0       
# count = 0  
# x = int(input("x = "))

# while x != 0:        
#     s += x
#     count += 1
#     x = int(input("x = "))

# print("Барлық сандардың қосындысы:", s)
# print("Сандардың саны:", count)

# # 5. A және B саны берілген. [A, B] диапазонындағы сандардың қосындысы
# A = 5
# B = 2
# E = 0
# for i in range(A, B+1):
#     E += i
# print("Қосынды:", E)


# # 6. Теріс сандардың арифметикалық ортасы
# arr = [-5, -3, -10, 4, -2, 7]
# neg_sum = 0
# neg_count = 0
# for x in arr:
#     if x < 0:
#         neg_sum += x
#         neg_count += 1
# if neg_count > 0:
#     print("Теріс сандардың ортасы:", neg_sum / neg_count)
# else:
#     print("Теріс сан жоқ")


# # 7. [A, B] диапазонында квадраттардың қосындысы
# A = int(input("A = "))
# B = int(input("B = "))
# s = 0
# for i in range(A, B+1):
#     s += i*i
# print("Квадраттардың қосындысы:", s)


# # 8. Тізбектегі барлық жұп сандардың қосындысы
# arr = [2, 5, 8, 11, 14, 7]
# s = 0
# i = 0
# while i < len(arr):
#     if arr[i] % 2 == 0:
#         s += arr[i]
#     i += 1
# print("Жұп сандар қосындысы:", s)


# # 9. a-дан 200-ге дейінгі сандардың орташа мәні
# a = int(input("a = "))
# s = 0
# count = 0
# for i in range(a, 201):
#     s += i
#     count += 1
# print("Орташа мән:", s / count)


# # 10. Тізбектің басында қанша оң сан барын табу
# arr = [5, 3, 8, -2, 6, -4]
# count = 0
# for x in arr:
#     if x > 0:
#         count += 1
#     else:
#         break
# print("Басындағы оң сандар саны:", count)


# # 11. a-дан b-ге дейінгі сандардың қосындысы
# a = int(input("a = "))
# b = int(input("b = "))
# s = 0
# for i in range(a, b+1):
#     s += i
# print("Қосынды:", s)


# # 12. N = 2^K болғандағы K табу
# N = int(input("N = "))
# K = 0
# while 2**K < N:
#     K += 1
# if 2**K == N:
#     print("K =", K)
# else:
#     print("Мұндай K жоқ")


# # 13. a-дан 50-ге дейінгі квадраттардың қосындысы
# a = int(input("a = "))
# s = 0
# for i in range(a, 51):
#     s += i*i
# print("Квадраттардың қосындысы:", s)


# # 14. N > 1 берілген. K^2 > N болатындай ең кіші K табу
# N = int(input("N = "))
# K = 1
# while K*K <= N:
#     K += 1
# print("K =", K)


# # 15. Тізбектегі жұп және тақ сандар қосындысы
# arr = [1, 2, 3, 4, 5, 6, 7]
# sum_even = 0
# sum_odd = 0
# for x in arr:
#     if x % 2 == 0:
#         sum_even += x
#     else:
#         sum_odd += x
# print("Жұп сандар қосындысы:", sum_even)
# print("Тақ сандар қосындысы:", sum_odd)

# def a():
#     i = 0
#     b = 0
#     while i != 10:
#         i += 1

#         if i % 2 != 0:
#             b += i

#     return b

# print(a())



# # 1) Бірінші n-нен үлкен сан (1, 5, 10, 16, …)
# n = int(input("n = "))
# x, d = 1, 4
# while x <= n:
#     x += d
#     d += 1
# print("Жауап 1:", x)



# # 2) 20 студенттің орташа бағасы
# s = 0
# for i in range(20):
#     s += int(input("Баға: "))
# print("Жауап 2:", s / 20)


# 3) N табады
# A = float(input("A = "))
# s, N = 0, 0

# while s < A:
#     N += 1
#     s += 1 / N
# print("Жауап 3: N =", N)


# # 4) Тізбектей қосылған кедергі
# n = int(input("Элемент саны: "))
# s = 0
# for i in range(n):
#     s += float(input("Кедергі: "))
# print("Жауап 4:", s)


# # 5) Группаның орташа бағасы
# n = int(input("Студент саны: "))
# s = 0
# for i in range(n):
#     s += int(input("Баға: "))
# print("Жауап 5:", s / n)


# # 6) 2 санының дәрежелері (0-ден 20-ға дейін)
# i = 0
# while i <= 20:
#     print("Жауап 6:", 2**i)
#     i += 1


# # 7) Орташа халық тығыздығы
# p, a = 0, 0
# for i in range(12):
#     p += float(input("Халық (мың): "))
#     a += float(input("Аудан (км²): "))
# print("Жауап 7:", p / a)


# 8) Байдың сыйлығы > 40000 болғанда


# g, y, s = 1, 1, 0
# while s <= 40000:
#     s += g
#     g *= 2
#     y += 1
# print("Жауап 8:", y, "жасында")


# while y <= 8:
#     s += g
#     g *= 2
#     y += 1
# print("Жауап 8:", s, "aksha")



# # 9) Амёба (әр 3 сағат сайын бөлінеді)
# n = int(input("Сағат саны: "))
# a = 1
# for i in range(3, n+1, 3):
#     a *= 2
#     print("Жауап 9:", i, "сағаттан кейін =", a)


# # 10) y = –0.5x + x (1–3, қадам 0.5)
# x = 1
# while x <= 3:
#     print("Жауап 10: x =", x, "y =", -0.5*x + x)
#     x += 0.5


# # 11) Спортшының жүгірісі
# d, s = 10, 0
# for i in range(7):
#     print("Жауап 11:", i+1, "күн =", d)
#     s += d
#     d *= 1.1
# print("Жалпы =", s)

# # 12) Санның цифрларының қосындысы мен көбейтіндісі
# n = int(input("Сан енгіз: "))
# s, p = 0, 1
# while n > 0:
#     d = n % 10
#     s += d
#     p *= d
#     n //= 10
# print("Жауап 12: Қосынды =", s, "Көбейтінді =", p) 


class UserProfile:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def update(self, **kwargs):
        return UserProfile(
            kwargs.get("name", self.name),
            kwargs.get("email", self.email),
            kwargs.get("role", self.role)
        )

    def __repr__(self):
        return f"UserProfile(name='{self.name}', email='{self.email}', role='{self.role}')"


user = UserProfile("Ilyas", "ilyas@example.com", "admin")
new_user = user.update(role="editor")
print(user) 
print(new_user) 


class Vector2D():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def add(self,prop):
        return Vector2D(self.x + prop.x, self.y + prop.y)
    
    def scale(self, factor):
        return Vector2D(self.x * factor, self.y * factor)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
    

v1 = Vector2D(2, 3)
v2 = Vector2D(1, 4)
print(v1.add(v2)) 
print(v1.scale(2))


class FrozenInvoice:
    def __init__(self, price, quantity):
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @property
    def total(self):
        return self._price * self._quantity

    def __repr__(self):
        return f"FrozenInvoice(price={self.price}, quantity={self.quantity}, total={self.total})"


invoice = FrozenInvoice(500, 3)
print(invoice.price)    
print(invoice.quantity)  
print(invoice.total)     


