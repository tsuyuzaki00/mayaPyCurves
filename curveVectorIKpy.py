import pymel.core as pm

def curveVectorIK(name):
    height = 1.4
    a1 = (0,height,0)
    b1 = (1,0,1)
    b2 = (1,0,-1)
    b3 = (-1,0,-1)
    b4 = (-1,0,1)
    c1 = (0,-height,0)
    tmpCurve = pm.curve( d=1,p=[b1,b2,b3,b4,b1,a1,b3,c1,b1,b2,a1,b4,c1,b2], n = name )
    return name