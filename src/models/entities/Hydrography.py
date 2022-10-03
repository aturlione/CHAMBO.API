import datetime

class DateFormat():

    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')

class SubCatchment():  

    def __init__(self,id,Nombre=None,Area_km2=None,par_a=None, par_tau=None, par_p0=None, par_lan=None, par_fcp=None, par_ks=None, par_tc1=None, par_tc2=None, Qthr_1=None, Qthr_2=None, Qthr_3=None) -> None:
        self.id=id
        self.Nombre=Nombre
        self.Area_km2=Area_km2
        self.par_a=par_a
        self.par_tau=par_tau
        self.par_p0=par_p0
        self.par_lan=par_lan
        self.par_fcp=par_fcp
        self.par_ks=par_ks
        self.par_tc1=par_tc1
        self.par_tc2=par_tc2
        self.Qthr_1=Qthr_1
        self.Qthr_2=Qthr_2
        self.Qthr_3=Qthr_3
    def to_JSON(self):
        return{
            'id':self.id,
            'Nombre':self.Nombre,
            'Area_km2':self.Area_km2,
            'par_a':self.par_a,
            'par_tau':self.par_tau,
            'par_p0':self.par_p0,
            'par_lan':self.par_lan,
            'par_fcp':self.par_fcp,
            'par_ks':self.par_ks,
            'par_tc1':self.par_tc1,
            'par_tc2':self.par_tc2,
            'Qthr_1':self.Qthr_1,
            'Qthr_2':self.Qthr_2,
            'Qthr_3':self.Qthr_3
        }

class Sub_Catchment_Melca():  

    def __init__(self,id,Drena_a=None,cod_pfs=None,nombre=None, Area_km2=None, LongCauce_km=None, tuhp=None, RioPpal=None, TipoCuenca=None) -> None:
        self.id=id
        self.Drena_a=Drena_a
        self.cod_pfs=cod_pfs
        self.nombre=nombre
        self.Area_km2=Area_km2
        self.LongCauce_km=LongCauce_km
        self.tuhp=tuhp
        self.RioPpal=RioPpal
        self.TipoCuenca=TipoCuenca
    def to_JSON(self):
        return{
            'id':self.id,
            'Drena_a':self.Drena_a,
            'cod_pfs':self.cod_pfs,
            'nombre':self.nombre,
            'Area_km2':self.Area_km2,
            'LongCauce_km':self.LongCauce_km,
            'tuhp':self.tuhp,
            'RioPpal':self.RioPpal,
            'TipoCuenca':self.TipoCuenca
        }
    def to_JSON2(self):
        return{
            'subCatchmentFromId':self.id,
            'subCatchmentToId':self.Drena_a,
            'catchmentHierarchyStep':None,
            'catchmentReferenceIdentifier':None,
            'subCatchmentNavigationStep':None,
            'isOrigin':None,
        }
class Navigation():  
    def __init__(self,from_ids,Drena_a=None,catchmentHierarchyStep=None,catchmentReferenceIdentifier=None, subCatchmentNavigationStep=None, isOrigin=None) -> None:
        self.from_ids=from_ids
        self.Drena_a=Drena_a
        self.catchmentHierarchyStep=catchmentHierarchyStep
        self.catchmentReferenceIdentifier=catchmentReferenceIdentifier
        self.subCatchmentNavigationStep=subCatchmentNavigationStep
        self.isOrigin=isOrigin

    def to_JSON(self):
        return{
            'subCatchmentFromId':self.from_ids,
            'subCatchmentToId':self.Drena_a,
            'catchmentHierarchyStep':self.catchmentHierarchyStep,
            'catchmentReferenceIdentifier':self.catchmentReferenceIdentifier,
            'subCatchmentNavigationStep':self.subCatchmentNavigationStep,
            'isOrigin':self.isOrigin,
        }

class param_demandas():  

    def __init__(self,id,inic,fin,tipo,qmax,tret) -> None:
        self.id=id
        self.inic=inic
        self.fin=fin
        self.tipo=tipo
        self.qmax=qmax
        self.tret=tret
    
    def to_JSON(self):
        return{
            'id':self.id,
            'inic':self.inic,
            'fin':self.fin,
            'tipo':self.tipo,
            'winterDemand':self.qmax,
            'summerDemand':self.qmax,
            'autumnDemand':self.qmax,
            'springDemand':self.qmax,
            'annualDemand':self.qmax,
            'returnRate':self.tret
        }

class param_ret():  

    def __init__(self,id,inic,fin,tipo,qmax,tret) -> None:
        self.id=id
        self.inic=inic
        self.fin=fin
        self.tipo=tipo
        self.qmax=qmax
        self.tret=tret
    
    def to_JSON(self):
        return{
            'id':self.id,
            'inic':self.inic,
            'fin':self.fin,
            'tipo':self.tipo,
            'winterRet':self.tret*self.qmax,
            'summerRet':self.tret*self.qmax,
            'autumnRet':self.tret*self.qmax,
            'springRet':self.tret*self.qmax,
            'annualRet':self.tret*self.qmax,
        }


class param_demandas_tipos():  

    def __init__(self,id,tret,pri,ss,cf,np,dbo) -> None:
        self.id=id
        self.tret=tret
        self.pri=pri
        self.ss=ss
        self.cf=cf
        self.np=np
        self.dbo=dbo
    
    def to_JSON(self):
        return{
            'id':self.id,
            'tret':self.tret,
            'pri':self.pri,
            'ss':self.ss,
            'cf':self.cf,
            'np':self.np,
            'dbo':self.dbo
        }

class param_demandas_info():  

    def __init__(self,id,nombre,val) -> None:
        self.id=id
        self.nombre=nombre
        self.val=val
    
    def to_JSON(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'val':self.val
        }

class Well():  

    def __init__(self,id,Annual=None,Spring=None,Summer=None, Winter=None, Autumn=None,subCatchmentMELCA=None) -> None:
        self.id=id
        self.annualFlow=Annual
        self.springFlow=Spring
        self.summerFlow=Summer
        self.winterFlow=Winter
        self.autumnFlow=Autumn
        self.subCatchmentMELCA=subCatchmentMELCA
    def to_JSON(self):
        return{
            'id':self.id,
            'annualFlow':self.annualFlow,
            'springFlow':self.springFlow,
            'summerFlow':self.summerFlow,
            'winterFlow':self.winterFlow,
            'autumnFlow':self.autumnFlow,
            'subCatchmentMELCAid':self.subCatchmentMELCA
        }

class Dam():  

    def __init__(self,id,pointString=None,damId=None,name=None, alias=None, use=None,damType=None,condition=None,basinInfluence=None,damRiver=None,basinArea=None,height=None,crestLength=None,capacity=None,lastEditedDate=None,lastEditedUser=None,annualFlow=None,springFlow=None,summerFlow=None,autumnFlow=None,winterFlow=None,subcatchmentMELCAid=None) -> None:
        self.id=id
        self.pointString=pointString
        self.damId=damId
        self.name=name
        self.alias=alias
        self.use=use
        self.damType=damType
        self.condition=condition
        self.basinInfluence=basinInfluence
        self.damRiver=damRiver
        self.basinArea=basinArea
        self.height=height
        self.capacity=capacity
        self.crestLength=crestLength
        self.lastEditedDate=lastEditedDate
        self.lastEditedUser=lastEditedUser
        self.annualFlow=annualFlow
        self.springFlow=springFlow
        self.summerFlow=summerFlow
        self.winterFlow=winterFlow
        self.autumnFlow=autumnFlow
        self.subCatchmentMELCA=subcatchmentMELCAid
    def to_JSON(self):
        return{
            'id':self.id,
            'pointString':self.pointString,
            'damId':self.damId,
            'name':self.name,
            'alias':self.alias,
            'use':self.use,
            'damType':self.damType,
            'condition':self.condition,
            'basinInfluence':self.basinInfluence,
            'damRiver':self.damRiver,
            'basinArea':self.basinArea,
            'height':self.height,
            'capacity':self.capacity,
            'crestLength':self.crestLength,
            'lastEditedDate':self.lastEditedDate,
            'annualFlow':self.annualFlow,
            'springFlow':self.springFlow,
            'summerFlow':self.summerFlow,
            'winterFlow':self.winterFlow,
            'autumnFlow':self.autumnFlow,
            'subCatchmentMELCA':self.subCatchmentMELCA
        }

class Water_Source():  

    def __init__(self,id,pointString=None,physiography=None,source=None, use=None, altitude=None,observations=None,area=None,lastEditedDate=None,lastEditedUser=None) -> None:
        self.id=id
        self.pointString=pointString
        self.physiography=physiography
        self.source=source
        self.use=use
        self.altitude=altitude
        self.observations=observations
        self.area=area
        self.lastEditedDate=lastEditedDate
        self.lastEditedUser=lastEditedUser
    def to_JSON(self):
        return{
            'id':self.id,
            'pointString':self.pointString,
            'physiography':self.physiography,
            'source':self.source,
            'use':self.use,
            'altitude':self.altitude,
            'observations':self.observations,
            'area':self.area,
            'lastEditedDate':self.lastEditedDate,
            'lastEditedUser':self.lastEditedUser

        }

class ecosystems():  

    def __init__(self, id, pointString, name, alias, type, ecosystemArea, lastEditedDate, lastEditedUser,winterDemand,summerDemand,autumnDemand,springDemand,annualDemand,subcatchmentMELCAid) -> None:
        self.id=id
        self.pointString=pointString
        self.name=name
        self.alias=alias
        self.type=type
        self.ecosystemArea=ecosystemArea
        self.lastEditedDate=lastEditedDate
        self.lastEditedUser=lastEditedUser
        self.winterDemand=winterDemand
        self.summerDemand=summerDemand
        self.autumnDemand=autumnDemand
        self.springDemand=springDemand
        self.annualDemand=annualDemand
        self.subcatchmentMELCAid=subcatchmentMELCAid
        
    def to_JSON(self):
        return{
            'id':self.id,
            'pointString':self.pointString,
            'name':self.name,
            'alias':self.alias,
            'type':self.type,
            'ecosystemArea':self.ecosystemArea,
            'lastEditedDate':self.lastEditedDate,
            'lastEditedUser':self.lastEditedUser,
            'winterDemand':self.winterDemand,
            'summerDemand':self.summerDemand,
            'autumnDemand':self.autumnDemand,
            'springDemand':self.springDemand,
            'annualDemand':self.annualDemand,
            'subcatchmentMELCAid':self.subcatchmentMELCAid,

        }       


class irrigations():  

    def __init__(self, id,pointString,name,irrigationArea,winterArea,summerArea,annualArea,source,type,winterDemand,summerDemand,autumnDemand,springDemand,annualDemand,annualVolume,program,benefitedFamilies,agriculturalZone,lastEditedDate,lastEditedUser,alias,returnRate,subcatchmentMELCAid) -> None:
        self.id=id
        self.pointString=pointString
        self.name=name
        self.irrigationArea=irrigationArea
        self.winterArea=winterArea
        self.summerArea=summerArea
        self.annualArea=annualArea
        self.source=source
        self.type=type
        self.winterDemand=winterDemand
        self.summerDemand=summerDemand
        self.autumnDemand=autumnDemand
        self.springDemand=springDemand
        self.annualDemand=annualDemand
        self.annualVolume=annualVolume
        self.program=program
        self.benefitedFamilies=benefitedFamilies
        self.agriculturalZone=agriculturalZone
        self.lastEditedDate=lastEditedDate
        self.lastEditedUser=lastEditedUser
        self.alias=alias
        self.returnRate=returnRate
        self.subcatchmentMELCAid=subcatchmentMELCAid
        
    def to_JSON(self):
        return{
            'id':self.id,
            'pointString':self.pointString,
            'name':self.name,
            'irrigationArea':self.irrigationArea,
            'winterArea':self.winterArea,
            'summerArea':self.summerArea,
            'annualArea':self.annualArea,
            'source':self.source,
            'type':self.type,
            'winterDemand':self.winterDemand,
            'summerDemand':self.summerDemand,
            'autumnDemand':self.autumnDemand,
            'springDemand':self.springDemand,
            'annualDemand':self.annualDemand,
            'annualVolume':self.annualVolume,
            'program':self.program,
            'benefitedFamilies':self.benefitedFamilies,
            'agriculturalZone':self.agriculturalZone,
            'lastEditedDate':self.lastEditedDate,
            'lastEditedUser':self.lastEditedUser,
            'alias':self.alias,
            'returnRate':self.returnRate,
            'subcatchmentMELCAid':self.subcatchmentMELCAid,    

        }   

class mining_centers():  

    def __init__(self, id,pointString,name,depositSize,alteredState,mineral,alias,depositNumber,lastEditedDate,lastEditedUser, type,depositType,group,winterDemand,summerDemand,autumnDemand,springDemand,annualDemand,returnRate,subCatchmentMELCAid) -> None:
        self.id=id
        self.pointString=pointString
        self.name=name
        self.depositSize=depositSize
        self.alteredState=alteredState
        self.mineral=mineral
        self.alias=alias
        self.depositNumber=depositNumber
        self.lastEditedDate=lastEditedDate
        self.lastEditedUser=lastEditedUser
        self.type=type
        self.depositType=depositType
        self.group=group
        self.winterDemand=winterDemand
        self.summerDemand=summerDemand
        self.autumnDemand=autumnDemand
        self.springDemand=springDemand
        self.annualDemand=annualDemand
        self.returnRate=returnRate
        self.subCatchmentMELCAid=subCatchmentMELCAid

        
    def to_JSON(self):
        return{
            'id':self.id,
            'pointString':self.pointString,
            'name':self.name,
            'depositSize':self.depositSize,
            'alteredState':self.alteredState,
            'mineral':self.mineral,
            'alias':self.alias,
            'depositNumber':self.depositNumber,
            'lastEditedDate':self.lastEditedDate,
            'lastEditedUser':self.lastEditedUser,
            'type':self.type,
            'depositType':self.depositType,
            'group':self.group,
            'winterDemand':self.winterDemand,
            'summerDemand':self.summerDemand,
            'autumnDemand':self.autumnDemand,
            'springDemand':self.springDemand,
            'annualDemand':self.annualDemand,
            'returnRate':self.returnRate,
            'subCatchmentMELCAid':self.subCatchmentMELCAid,


        }  


class potable_water_demands():  

    def __init__(self, id,pointString,name,irrigationArea,winterArea,summerArea,annualArea,source,type,winterDemand,summerDemand,autumnDemand,springDemand,annualDemand,annualVolume,program,benefitedFamilies,agriculturalZone,lastEditedDate,lastEditedUser,alias,returnRate,subcatchmentMELCAid) -> None:
        self.id=id
        self.pointString=pointString
        self.name=name
        self.irrigationArea=irrigationArea
        self.winterArea=winterArea
        self.summerArea=summerArea
        self.annualArea=annualArea
        self.source=source
        self.type=type
        self.winterDemand=winterDemand
        self.summerDemand=summerDemand
        self.autumnDemand=autumnDemand
        self.springDemand=springDemand
        self.annualDemand=annualDemand
        self.annualVolume=annualVolume
        self.program=program
        self.benefitedFamilies=benefitedFamilies
        self.agriculturalZone=agriculturalZone
        self.lastEditedDate=lastEditedDate
        self.lastEditedUser=lastEditedUser
        self.alias=alias
        self.returnRate=returnRate
        self.subcatchmentMELCAid=subcatchmentMELCAid
        
    def to_JSON(self):
        return{
            'id':self.id,
            'pointString':self.pointString,
            'name':self.name,
            'irrigationArea':self.irrigationArea,
            'winterArea':self.winterArea,
            'summerArea':self.summerArea,
            'annualArea':self.annualArea,
            'source':self.source,
            'type':self.type,
            'winterDemand':self.winterDemand,
            'summerDemand':self.summerDemand,
            'autumnDemand':self.autumnDemand,
            'springDemand':self.springDemand,
            'annualDemand':self.annualDemand,
            'annualVolume':self.annualVolume,
            'program':self.program,
            'benefitedFamilies':self.benefitedFamilies,
            'agriculturalZone':self.agriculturalZone,
            'lastEditedDate':self.lastEditedDate,
            'lastEditedUser':self.lastEditedUser,
            'alias':self.alias,
            'returnRate':self.returnRate,
            'alias':self.subcatchmentMELCAid,

        }   


class Param_Chambo():  

    def __init__(self, id, fin, nombre, area, s0, tau, fcp, fce) -> None:
        self.id=id
        self.fin=fin
        self.nombre=nombre
        self.area=area
        self.s0=s0
        self.tau=tau
        self.fcp=fcp
        self.fce=fce
        
    def to_JSON(self):
        return{
            'id':self.id,
            'fin':self.fin,
            'nombre':self.nombre,
            'area':self.area,
            's0':self.s0,
            'tau':self.tau,
            'fcp':self.fcp,
            'fcp':self.fcp,
            'fce':self.fce,

        }

class Parametros_LEM():  

    def __init__(self, id, par_a, par_tau, par_p0, par_lan, par_fcp, par_ks, par_tc1, par_tc2, Qthr_1, Qthr_2, Qthr_3) -> None:
        self.id=id
        self.par_a=par_a
        self.par_tau=par_tau
        self.par_p0=par_p0
        self.par_lan=par_lan
        self.par_fcp=par_fcp
        self.par_ks=par_ks
        self.par_tc1=par_tc1
        self.par_tc2=par_tc2
        self.Qthr_1=Qthr_1
        self.Qthr_2=Qthr_2
        self.Qthr_3=Qthr_3
        
    def to_JSON(self):
        return{
            'id':self.id,
            'par_a':self.par_a,
            'par_tau':self.par_tau,
            'par_p0':self.par_p0,
            'par_lan':self.par_lan,
            'par_fcp':self.par_fcp,
            'par_ks':self.par_ks,
            'par_tc1':self.par_tc1,
            'par_tc2':self.par_tc2,
            'Qthr_1':self.Qthr_1,
            'Qthr_2':self.Qthr_2,
            'Qthr_3':self.Qthr_3

        }


class Param_Chambo():  

    def __init__(self, id, fin, nombre, area, s0, tau, fcp, fce) -> None:
        self.id=id
        self.fin=fin
        self.nombre=nombre
        self.area=area
        self.s0=s0
        self.tau=tau
        self.fcp=fcp
        self.fce=fce
        
    def to_JSON(self):
        return{
            'id':self.id,
            'fin':self.fin,
            'nombre':self.nombre,
            'area':self.area,
            's0':self.s0,
            'tau':self.tau,
            'fcp':self.fcp,
            'fcp':self.fcp,
            'fce':self.fce,

        }        

