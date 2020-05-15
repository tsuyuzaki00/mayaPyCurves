import pymel.core as pm

def curveHexagon(name):
    height = 2
    a1 = (0,-1,0)
    a2 = (0,-0.5,0.87)
    a3 = (0,0.5,0.87)
    a4 = (0,1,0)
    a5 = (0,0.5,-0.87)
    a6 = (0,-0.5,-0.87)
    b1 = (height,-1,0)
    b2 = (height,-0.5,0.87)
    b3 = (height,0.5,0.87)
    b4 = (height,1,0)
    b5 = (height,0.5,-0.87)
    b6 = (height,-0.5,-0.87)

    tmpCurve = pm.curve( d=1,p=[a1,a2,a3,a4,a5,a6,a1,b1,b2,a2,b2,b3,a3,b3,b4,a4,b4,b5,a5,b5,b6,a6,b6,b1], n= name )
    return name