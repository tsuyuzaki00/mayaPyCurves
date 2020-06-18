import pymel.core as pm

def main():

    sels = pm.selected()
    createCurve.name(sels)
    class createCurve:
        def name(self,sels):
            if sels == []:
                trsName = ''
                ctrlName = ''
                createCurve.trsSetting(trsName,ctrlName)
            else:
                for sel in sels:
                    part = sel.split("_")
                    trsName = sel.replace( '_'.join(['null',part[0],scene,'C'] ))
                    ctrlName = sel.replace( '_'.join(['ctrl',part[0],scene,'C'] ))
                    createCurve.trsSetting(trsName,ctrlName)

        def trsSetting(self,trsName,ctrlName):
            trs = pm.createNode( 'transform', n= trsName)
            ctrl = curveAntenna(ctrlName)

            pm.parent(ctrl, trs)
            pm.parent(trs, sel)
            
            pm.move( 0, 0, 0 ,ls=True)
            pm.rotate( 0, 0, 0 , os=True)
            pm.parent(trs ,w = True)

        def curveAntenna(self,name):
            a1 = (0,0,0)
            a2 = (0,3,0)
            a3 = (0,5,0)
            bxf =(1,4,0)
            bxb =(-1,4,0)
            bzf =(0,4,1)
            bzb =(0,4,-1)

            pm.curve( d=1,p=[a1,a3,bxf,a2,bxb,a3,bzf,a2,bzb,a3,bxf,bxb,bzf,bzb,bxf,bzf,bzb,bxb], n=name )
            return name


    

    

        