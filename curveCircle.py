import pymel.core as pm

def curveCircle(name):
    pm.circle( nr=(1, 0, 0), c=(0, 0, 0), sw=360, r=2, n = name)
    return name    