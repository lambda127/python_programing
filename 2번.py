import random

ans = random.randrange(1,101)

while True :
  sol = int(input("숫자를 예측해보세요 (1~100) >> "))

  if sol > ans:
      print("숫자가 낮습니다.")

  elif sol < ans:
      print("숫자가 높습니다.")

  else:
    print("정답입니다!!")
    break;
