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
        
    def curveHexagon(self, name):
        height = 2
        a1 = (0,-1,0)
        a2 = (0,-0.5,0.87)
        a3 = (0,0.5,0.87)
        a4 = (0,1,0)
        a5 = (0,0.5,-0.87)
        a6 = (0,-0.5,-0.87)
        b1 = (height,-1,0)
        b2 = (height,-0.5,0.87)
        b3 = (height,0.5,0.87)
        b4 = (height,1,0)
        b5 = (height,0.5,-0.87)
        b6 = (height,-0.5,-0.87)

        pm.curve( d=1,p=[a1,a2,a3,a4,a5,a6,a1,b1,b2,a2,b2,b3,a3,b3,b4,a4,b4,b5,a5,b5,b6,a6,b6,b1], n= name )
        return name
    
    def doubleCheck(self):
        scene = self.getSceneName()
        agoNullName = '_'.join( ['null', 'trsName', scene, 'C', '00'] )
        agoCtrlName = '_'.join( ['ctrl', 'curveName', scene, 'C', '00'] )

        if pm.objExists(agoNullName):
            for i in range(1000):
                agoNullName = '_'.join( ['null', 'trsName', scene, 'C', str(i).zfill(2)] )
                agoCtrlName = '_'.join( ['ctrl', 'curveName', scene, 'C', str(i).zfill(2)] )
                if not pm.objExists(agoNullName or agoCtrlName):
                    trsName = agoNullName
                    ctrlName = agoCtrlName
                    break
        else :
            trsName = '_'.join( ['null', 'trsName', scene, 'C', '00'] )
            ctrlName = '_'.join( ['ctrl', 'curveName', scene, 'C', '00'] )

        return trsName,ctrlName

    def createCurve(self):
        nameCheck = self.doubleCheck()
        self.trsSetting(nameCheck[0],nameCheck[1])

    def trsSetting(self, trsName, ctrlName):
        trs = pm.createNode( 'transform', n= trsName)
        ctrl = self.curveHexagon(ctrlName)

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
        ctrl = self.curveHexagon(ctrlName)

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