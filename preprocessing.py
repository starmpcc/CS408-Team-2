from typing import List
import os
import re
import hanja

DIRECTORY: str = "D:/KAIST/CS408-Team-2/Dataset"
CLASS: str = "tdmsfiletext"

# 문장 종료 조건
# 1. 문자 뒤에 마침표 또는 물음표 또는 느낌표가 오고 띄어쓰기 또는 줄바꾸기가 오는 경우
# 2. 줄바꾸기가 연속으로 두번 오는 경우. 이때 줄바꿈 사이의 띄어쓰기는 무시한다.
# 3. 문장 시작 부호(', " 등등)로 시작해서 동일한 종료 부호가 오는 경우

def main(result):
    for d in os.walk(DIRECTORY+"/KAIST_SWRC(Nolicense)"):
        files: List[str] = d[2]
        path: str = d[0]
        for fn in files:
            f = open(path + "/" + fn, mode="r", encoding="euc_kr", errors="surrogateescape")
            text1 = f.read()
            f.close()
            if not (("<{}>".format(CLASS) in text1) and ("</{}>".format(CLASS) in text1)):
                print(path + "/" + fn)
                return
            k1 = text1.find("<{}>".format(CLASS)) + len("<{}>".format(CLASS))
            text2 = text1[k1:] # cut prefix
            k2 = text2.find("</{}>".format(CLASS))
            text3 = text2[:k2] # cut postfix
            generator = (s.strip() for s in text3.split("\n")) # cut unnecessary white space
            data: str = "\n".join(generator)
            result.write(data)
    print("SUCCESS")



fresult = open(DIRECTORY+"/result.txt", mode="a", encoding="euc_kr", errors="surrogateescape")
main(fresult)
fresult.close()
