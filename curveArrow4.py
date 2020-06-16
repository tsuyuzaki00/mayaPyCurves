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

        ctrl = curveArrow4(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, sel)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

def curveArrow4(name):
    a00 = (0,-1,-1)
    a01 = (0,-3,-1)
    a02 = (0,-3,-2)
    a03 = (0,-5,0)
    a04 = (0,-3,2)
    a05 = (0,-3,1)
    a06 = (0,-1,1)
    a07 = (0,-1,3)
    a08 = (0,-2,3)
    a09 = (0,0,5)
    a10 = (0,2,3)
    a11 = (0,1,3)
    a12 = (0,1,1)
    a13 = (0,3,1)
    a14 = (0,3,2)
    a15 = (0,5,0)
    a16 = (0,3,-2)
    a17 = (0,3,-1)
    a18 = (0,1,-1)
    a19 = (0,1,-3)
    a20 = (0,2,-3)
    a21 = (0,0,-5)
    a22 = (0,-2,-3)
    a23 = (0,-1,-3)
    a24 = (0,-1,-1)

    tmpCurve = pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a00], n = name)
    return name
