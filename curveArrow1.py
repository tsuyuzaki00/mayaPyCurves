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

        ctrl = curveArrow1(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, sel)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

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
    