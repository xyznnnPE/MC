import math
import Null
import Zero
import MineCraft
import XYZ
class abcdef():
    def Hexadecimal(a,b,c,d,e,f):
      a = "00001011"
      b = "00001100"
      c = "00001101"
      d = "00001110"
      e = "00001111"
      f = "00010000"
    def time(a,b,c,d,e,f,x,y,z,t):
        return [
            a * math.sin(x + t) + b * math.cos(x - t) + c * math.sin(y + t) + d * math.cos(y - t) + e * math.sin(z + t) + f * math.cos(z - t),       #t123
            a * math.sin(x + t) + b * math.cos(x - t) + c * math.sin(y + t) + d * math.cos(y - t) + e * math.sin(z + t) + f * math.cos(z - t),       #t456
            a * math.asin(x + t) + b * math.acos(x - t) + c * math.asin(y + t) + d * math.acos(y - t) + e * math.asin(z + t) + f * math.acos(z - t), #t789
            a * math.tan(x + t) + b * math.atan(x - t) + c * math.tan(y + t) + d * math.atan(y - t) + e * math.tan(z + t) + f * math.atan(z - t) #t101112
            ]
