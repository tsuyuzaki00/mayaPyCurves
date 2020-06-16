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

        ctrl = curveVectorIK(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, sel)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

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