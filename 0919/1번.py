while(True) :
  num = int(input("몇 단을 출력할까요? : "))
  if (num < 2 or num > 9):
    print("2에서 9사이의 숫자를 입력하세요")
  else :
    break

for i in range(9) :
    res = num*(i+1)
    print(num, " * ", i+1, " = ", res)  #print("%d * %d = %d" %(num, i+1, res))
