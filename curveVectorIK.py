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
        
    def curveVectorIK(self, name):
        height = 1.4
        xu = (height,0,0)
        xd = (-height, 0, 0)
        yu = (0,height,0)
        yd = (0,-height,0)
        zu = (0, 0, height)
        zd = (0,0,-height)
        
        pm.curve( d=1,p=[xu,zd,xd,zu,xu,yu,xd,yd,xu,zd,yu,zu,yd,zd], n = name )
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
        ctrl = self.curveVectorIK(ctrlName)

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
        ctrl = self.curveVectorIK(ctrlName)

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