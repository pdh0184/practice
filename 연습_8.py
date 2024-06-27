import re
import time

psh = input('입력하세요')
sh = re.findall("수현", psh)

if sh == ["수현"]:
    time.sleep(1)
    print(chr(48148)+chr(48372))
    time.sleep(1)
    print(chr(48645)+chr(49888))
    time.sleep(1)
    print(chr(47672)+chr(51200)+chr(47532))