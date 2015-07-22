import random

mine = []
for i in range(10):
   mine.append([])
   for j in range(10):
      a = random.randrange(5)
      if a == 0:
         mine[i].append(1)
      else:
         mine[i].append(0)

def show(a):
   for i in a:
      print(i)
      
mines = []

for i in range(len(mine)):
   mines.append([])
   for j in range(len(mine[i])):
      if mine[i][j] == 1:
         mines[i].append('*')
      else:
         a =0
         for k in [-1,0,1]:
            for l in [-1,0,1]:
               if i+k>=0 and i+k<len(mine) and j+l>=0 and j+l<len(mine[0]):
                  a = a+mine[i+k][j+l]
         mines[i].append(a)
   
visi = []

for i in range(len(mine)):
   visi.append([])
   for j in range(len(mine[i])):
      visi[i].append(' ')

def play(a,b):
   if mine[a][b] == 1:
      return "End of the game"
   else:
      visi[a][b] = mines[a][b]
      show(visi)
      
def aMine(a,b):
   visi[a][b] = '!'
   show(visi)
