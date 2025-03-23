import math
import Null
import Zero
import MineCraft
class abcdef():
    def Hexadecimal(a,b,c,d,e,f):
      a = "00001011"
      b = "00001100"
      c = "00001101"
      d = "00001110"
      e = "00001111"
      f = "00010000"
    def time(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12):
        return [
            a * math.sin(x + t1) + b * math.cos(x - t1) + c * math.sin(y + t2) + d * math.cos(y - t2) + e * math.sin(z + t3) + f * math.cos(z - t3),       #t123
            a * math.sin(x + t1) + b * math.cos(x - t1) + c * math.sin(y + t2) + d * math.cos(y - t2) + e * math.sin(z + t3) + f * math.cos(z - t3),       #t123
            a * math.asin(x + t4) + b * math.acos(x - t4) + c * math.asin(y + t5) + d * math.acos(y - t5) + e * math.asin(z + t6) + f * math.acos(z - t6), #t456
            a * math.sinh(x + t7) + b * math.cosh(x - t7) + c * math.sinh(y + t8) + d * math.cosh(y - t8) + e * math.sinh(z + t9) + f * math.cosh(z - t9), #t789
            a * math.tan(x + t10) + b * math.atan(x - t10) + c * math.tan(y + t11) + d * math.atan(y - t11) + e * math.tan(z + t12) + f * math.atan(z - t12) #t101112
            ]
