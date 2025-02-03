try:
    v0 = int(input("V0"))
    v = int(input("V"))
    t = int(input("t"))
    if t<=0:
      raise zeroT("Error")
except TypeError:
    print("Error")


def Boost(v,v0,t):
    a = (v-v0)/t
    return a


def BoostS(Boost):
    def Wrapper(v,v0,t):
        a = Boost(v,v0,t)
        S = v0*t+a*t**2/2
        return S
    return Wrapper

a = Boost(v0,v,t)
print(a)

@BoostS
def Boost(v,v0,t):
    a = (v-v0)/t
    return a

s = Boost(v0,v,t)
print(s)


