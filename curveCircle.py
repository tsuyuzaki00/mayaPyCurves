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

        ctrl = curveCircle(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, sel)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

def curveCircle(name):
    pm.circle( nr=(1, 0, 0), c=(0, 0, 0), sw=360, r=2, n = name)
    return name    