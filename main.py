import random
def 生成整数():
  while True:
    try:
      a = int(input("请输入范围前置数："))
      b = int(input("请输入范围后置数："))
      if a == b:
        print("前置数不能等于后置数！")
      else: 
        break
    except:
      print("请输入正确的整数！")
      continue 
  c = random.randint(a,b)
  print("生成结果:" , c)

def 生成小数():
  while True:
    try:
      a = float(input("请输入范围前置数："))
      b = float(input("请输入范围后置数："))
      if a == b:
        print("前置数不能等于后置数！")
      else: 
        break
    except:
      print("请输入正确的小数！")
    continue 
  c = random.randint(a,b)
  print("生成结果:" , c)

if __name__ == "__main__":
  mode = input("欢迎使用随机数生成器！！\r\n工作模式：\r\n1.整数模式\r\n2.小数模式\r\n请选择(1/2):")
  while True:
    if mode =="1":
      生成整数()
    elif mode =="2":
      生成小数()
    else :
      print ("请输入正确的工作模式！")
      continue