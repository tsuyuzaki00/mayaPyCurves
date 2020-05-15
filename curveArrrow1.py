import pymel.core as pm

def curveArrow1(name):
    a00 = (0, -1, 0)
    a01 = (0,0,1)
    a02 = (0,0,0.5)
    a03 = (0,1,0.5)
    a04 = (0,1,-0.5)
    a05 = (0,0,-0.5)
    a06 = (0,0,-1)

    tmpCurve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a00], n = name)
    return name
    