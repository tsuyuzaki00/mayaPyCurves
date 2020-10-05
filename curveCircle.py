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
        
    def curveCircle(self, name):
        pm.circle( nr = (1, 0, 0), c = (0, 0, 0), sw = 360, r = 2, ch = False, n = name)
        return name
    
    def doubleCheck(self):
        scene = self.getSceneName()
        agoNullName = '_'.join( ['C', 'objName', 'null', scene, '00'] )
        agoCtrlName = '_'.join( ['C', 'objName', 'ctrl', scene, '00'] )

        if pm.objExists(agoNullName):
            for i in range(1000):
                agoNullName = '_'.join( ['C', 'objName', 'null', scene, str(i).zfill(2)] )
                agoCtrlName = '_'.join( ['C', 'objName', 'ctrl', scene, str(i).zfill(2)] )
                if not pm.objExists(agoNullName or agoCtrlName):
                    trsName = agoNullName
                    ctrlName = agoCtrlName
                    break
        else :
            trsName = '_'.join( ['C', 'objName', 'null', scene, '00'] )
            ctrlName = '_'.join( ['C', 'objName', 'ctrl', scene, '00'] )

        return trsName,ctrlName

    def createCurve(self):
        nameCheck = self.doubleCheck()
        self.trsSetting(nameCheck[0],nameCheck[1])

    def trsSetting(self, trsName, ctrlName):
        trs = pm.createNode( 'transform', n= trsName)
        ctrl = self.curveCircle(ctrlName)

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
        ctrl = self.curveCircle(ctrlName)

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