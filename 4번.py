id = input("주민등록번호: ")
sId = id[0:6]+id[7:]
qual = [2,3,4,5,6,7,8,9,2,3,4,5]


sum = 0

for i in range(0,12):
  sum += int(sId[i]) * int(qual[i])


if int(sId[12]) == 11-(sum%11) :
  print("유효한 주민등록번호입니다.")

else:
  print("유효하지 않은 주민등록번호입니다.")
