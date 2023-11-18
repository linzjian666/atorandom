# -*- coding: UTF-8 -*-
# @Author  : Linzjian666
# @Time    : 2023/11/18 11:45
# @Function: Generate random number within a range

import random
def 获取小数位数(number):
  decimal_str = str(number).split('.')
  if len(decimal_str) == 2 and len(decimal_str[1]) != 0:
      return len(decimal_str[1])
  else:
      return 0

def 生成随机数(before,after):
  try:
      if float(before) > float(after):
          print("起始数应小于终止数!")
      if 获取小数位数(before) == 0 and 获取小数位数(after) == 0:
          random_num = random.randint(int(before), int(after))
      else:
          decimal_places = max(获取小数位数(before), 获取小数位数(after))
          before = float(before) * 10 ** decimal_places
          after = float(after) * 10 ** decimal_places
          random_num = random.randint(int(before), int(after))
          random_num /= 10 ** decimal_places
      return random_num
  except:
    print("请输入有效的数据!")

if __name__ == "__main__":
  print("欢迎使用随机数生成器！！")
  while True:
    before = input("\r\n请输入范围起始数:")
    after = input("请输入范围终止数:")
    result = 生成随机数(before,after)
    print("\r\n生成结果:", result)
