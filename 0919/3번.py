tell = input("휴대전화 번호를 입력: ")
sTell = tell[0:3]

if sTell == "011" :
  print("당신은 SKT 사용자입니다.")

elif sTell == "016":
  print("당신은 KT 사용자입니다.")

elif sTell == "019":
  print("당신은 LGU 사용자입니다.")

else :
  print("통신사를 알 수 없습니다.")
