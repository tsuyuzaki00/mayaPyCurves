import pymel.core as pm

def main():
    sels = pm.selected()
    
    allSel = pm.select(hi = True, ado = True)
    allCheck = pm.selected()
    pm.select(cl = True)
    
    if sels == []:
        pm.error('Please select an object')
    
    for sel in sels:
        part = sel.split("_")
        trsName = sel.replace( part[0],'null')
        ctrlName = sel.replace( part[0],'ctrl')
        
        for check in allCheck:
            if check == ctrlName or check == trsName:
                pm.error('It stopped because of the name cast')
        
        trs = pm.createNode( 'transform', n= trsName)

        ctrl = curveTwist(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, sel)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

def curveTwist(name):
    a00 = (0, -1, 0)
    a01 = (0,-0.5,0.2)
    a02 = (0,-0.7,0.7)
    a03 = (0,-0.2,0.5)
    a04 = (0,0,1)
    a05 = (0,0.2,0.5)
    a06 = (0,0.7,0.7)
    a07 = (0,0.5,0.2)
    a08 = (0,1,0)
    a09 = (0,0.5,-0.2)
    a10 = (0,0.7,-0.7)
    a11 = (0,0.2,-0.5)
    a12 = (0,0,-1)
    a13 = (0,-0.2,-0.5)
    a14 = (0,-0.7,-0.7)
    a15 = (0,-0.5,-0.2)

    tmpCurve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00], n = name)
    return name
