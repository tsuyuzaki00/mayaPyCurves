import pymel.core as pm

def curveSquare(name):
    tmpCurve = pm.curve( d=1,p=[(1,0,1),(-1,0,1),(-1,0,-1),(1,0,-1)], n = name )
    pm.closeCurve( tmpCurve )
    return name