import pymel.core as pm

class CreateCurve():
    def __init__(self, sel):
        self.sel = sel

    def getSceneName(self):
        sceneName = pm.sceneName().basename()
        part = sceneName.split("_")
        
        if part[0].endswith('.ma') or part[0].endswith('.mb'):
            scene = part[0][:-3]
        elif part[0] == '':
            scene = 'scene'
        else:
            scene = part[0]

        return scene
       
    def curveArrow2(self, name):
        a00 = (10, 0, 0)
        a01 = (4,0,6)
        a02 = (4,0,2)
        a03 = (2,0,2)
        a04 = (0,0,2)
        a05 = (-2,0,2)
        a06 = (-4,0,2)
        a07 = (-4,0,6)
        a08 = (-10,0,0)
        a09 = (-4,0,-6)
        a10 = (-4,0,-2)
        a11 = (-2,0,-2)
        a12 = (0,0,-2)
        a13 = (2,0,-2)
        a14 = (4,0,-2)
        a15 = (4,0,-6)

        pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00], n = name)
        return name
    
    def doubleCheck(self):
        scene = self.getSceneName()
        agoNullName = '_'.join( ['C', 'trsName', 'null', scene, '00'] )
        agoCtrlName = '_'.join( ['C', 'curveName', 'ctrl', scene, '00'] )

        if pm.objExists(agoNullName):
            for i in range(1000):
                agoNullName = '_'.join( ['C', 'trsName', 'null', scene, str(i).zfill(2)] )
                agoCtrlName = '_'.join( ['C', 'curveName', 'ctrl', scene, str(i).zfill(2)] )
                if not pm.objExists(agoNullName or agoCtrlName):
                    trsName = agoNullName
                    ctrlName = agoCtrlName
                    break
        else :
            trsName = '_'.join( ['C', 'trsName', 'null', scene, '00'] )
            ctrlName = '_'.join( ['C', 'curveName', 'ctrl', scene, '00'] )

        return trsName,ctrlName

    def createCurve(self):
        nameCheck = self.doubleCheck()
        self.trsSetting(nameCheck[0],nameCheck[1])

    def trsSetting(self, trsName, ctrlName):
        trs = pm.createNode( 'transform', n= trsName)
        ctrl = self.curveArrow2(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, self.sel)

        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)

    def worldSetting(self):
        nameCheck = self.doubleCheck()
        trsName = nameCheck[0]
        ctrlName = nameCheck[1]
        trs = pm.createNode('transform', n = trsName)
        ctrl = self.curveArrow2(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs ,w = True)

def main():
    sels = pm.selected()
    if sels == []:
        createCurve = CreateCurve(None)
        createCurve.worldSetting()
    else:
        for sel in sels:
            create = CreateCurve(sel)
            create.createCurve()
main()