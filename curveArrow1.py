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
       
    def curveArrow1(self, name):
        a00 = (0, -1, 0)
        a01 = (0,0,1)
        a02 = (0,0,0.5)
        a03 = (0,1,0.5)
        a04 = (0,1,-0.5)
        a05 = (0,0,-0.5)
        a06 = (0,0,-1)

        pm.curve( d=1,p=[a00,a01,a02,a03,a04,a05,a06,a00], n = name)
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
        ctrl = self.curveArrow1(ctrlName)

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
        ctrl = self.curveArrow1(ctrlName)

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
