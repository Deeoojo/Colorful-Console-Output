def color_change(color, word):
  if color == "red":
    print("\033[31m", word)
  elif color == "yellow":
    print("\033[33m", word)
  elif color == "purple":
    print("\033[35m", word)
  else:
    print("\033[0m", word)
title = "Music app"
responset = f'{title:>25}'
color_change("yellow", responset,)
symbol = "🔥▶️"
txt = "Radio Gaga"
rank = "Queen"
print(symbol, end="")
responsetxt = f'{txt:>5}'
color_change("white", responsetxt)
responsetitle = f'{rank:>8}'
color_change("purple", responsetitle)
time1 = "Prev"
print("\033[0m", time1, end="\v")
print("\033[33m", "Next", end="\v")
color_change("red", "pause")
print()
print()
print("\033[0m","Interface 2")
title2 = "Welcome to"
restitle = f'{title2:>25}'
print(restitle)
title3 = """--   Armbook   --"""
restitle3 = f'{title3:>27}'
color_change("red", restitle3)
word = "Definetly not a rip off of"
resword = f'{word:>46}'
color_change("yellow", resword)
word2 = "a certain other social"
resword2 = f'{word2:>46}'
color_change("yellow", resword2)
word3 = "networking site"
resword3 = f'{word3:>46}'
color_change("yellow", resword3)
aword = "Honest."
raword = f'{aword:>25}'
color_change("red", raword)
login1 = "Username:"
login2 = "Password:"
rlogin1 = f'{login1:>25}'
rlogin2 = f'{login2:>25}'
color_change("white", rlogin1)
color_change("white", rlogin2)
