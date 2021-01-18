class Hundred:
    def Buy_Hundred(self):
        for a in range(20):
            for b in range(33):
                c = 100 -a -b
                if 5*a +3*b + c/3 ==100:
                   print('公鸡%d只,母鸡%d只,小鸡%d只'%(a,b,c))

if __name__ == '__main__':
    Hud = Hundred()
    Chic = Hud.Buy_Hundred()
