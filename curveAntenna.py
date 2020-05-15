import pymel.core as pm

def curveAntenna(name):
    a1 = (0,0,0)
    a2 = (0,3,0)
    a3 = (0,5,0)
    bxf =(1,4,0)
    bxb =(-1,4,0)
    bzf =(0,4,1)
    bzb =(0,4,-1)

    tmpCurve = pm.curve( d=1,p=[a1,a3,bxf,a2,bxb,a3,bzf,a2,bzb,a3,bxf,bxb,bzf,bzb,bxf,bzf,bzb,bxb], n=name )
    return name