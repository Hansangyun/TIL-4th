import random

greeting = '안녕하세요.'

# print(greeting)

# for 반복문으로 여러번 인사하기
# for i in range(5):
#     print(greeting)

# n = 0
# while n < 5:
#     print(greeting)
#     # n = n+1
#     n += 1


menus = ['순남시래기', '양자강', '타코벨']
# print(menus[1])

phone_book = {'순남시래기': '02-1234-5678',
              '양자강': '02-3142-5356', '타코벨': '02-646-2342'}
# print(phone_book['타코벨'])

# d = 0
# if d > 150:
#     print("매우나쁨")
# elif d > 80 and d <= 150:
#     print("나쁨")
# elif d > 30 and d <= 80:
#     print("보통")
# else:
#     print("좋음")

for i in range(5):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)