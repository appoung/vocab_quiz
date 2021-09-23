words = {"사과": "apple","깃헙": "github","파이썬" : "python", "리눅스" : "linux"}
for i in words:
    user_input=input(i+"의 뜻은 무엇인가요? >>>")
    if user_input == words[i]:
        print("맞았어요! 천재세요??!!")
    else:
        print("바보세요??? 와 이것도 못맞추는 바보가 있나?ㅋㅋ")

