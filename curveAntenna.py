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

        ctrl = curveAntenna(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, sel)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

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