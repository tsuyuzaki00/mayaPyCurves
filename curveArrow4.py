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
       
    def curveArrow4(self, name):
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

        pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a00], n = name)
        return name
    
    def doubleCheck(self):
        scene = self.getSceneName()
        agoNullName = '_'.join( ['null', 'trsNameA', scene, 'C'] )
        agoCtrlName = '_'.join( ['ctrl', 'curveNameA', scene, 'C'] )

        if pm.objExists(agoNullName):
            for i in range(26):
                agoNullName = '_'.join( ['null', 'trsName' + chr(65+i), scene, 'C'] )
                agoCtrlName = '_'.join( ['ctrl', 'curveName' + chr(65+i), scene, 'C'] )
                if not pm.objExists(agoNullName or agoCtrlName):
                    trsName = agoNullName
                    ctrlName = agoCtrlName
                    break
        else :
            trsName = '_'.join( ['null', 'trsNameA', scene, 'C'] )
            ctrlName = '_'.join( ['ctrl', 'curveNameA', scene, 'C'] )

        return trsName,ctrlName

    def createCurve(self):
        nameCheck = self.doubleCheck()
        self.trsSetting(nameCheck[0],nameCheck[1])

    def trsSetting(self, trsName, ctrlName):
        trs = pm.createNode( 'transform', n= trsName)
        ctrl = self.curveArrow4(ctrlName)

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
        ctrl = self.curveArrow4(ctrlName)

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