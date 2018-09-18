from math import sin, cos, tan, radians

n = float(raw_input("Tell me a value and I'll give you the sine, cosine and tagent: > "))
sin = sin(radians(n))
cos = cos(radians(n))
tang = tan(radians(n))
print "Your sine is {:.2f}, your cosine is {:.2f} and your tangent is {:.2f}".format(sin, cos, tang)