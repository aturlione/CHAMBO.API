import json
from flask import request,jsonify
from flask_restx import Resource, fields

import os

from src.models.HydrographyModel import HydrographyModel
from src.models.entities.Hydrography import param_usos_1 #Well, Water_Source, Dam, param_demandas

def start(apiflask):
    try:
        del os.environ["DISPLAY"]
    except KeyError:
        print("No display variable found")
    ns = apiflask.namespace("Hydrographies", description="CHAMBO API")
    current_folder = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(current_folder, "config.json"))
    config = json.load(f)

    #descriptores chambo
    @ns.route("/sub-catchments", methods=["GET"])
    class SubCatchments(Resource):        
        def get(self):
            try:
                subcatchments = HydrographyModel.get_sub_catchments()
                return jsonify(subcatchments)
            except Exception as ex:           
                raise Exception(ex)

    #select descriptores chambo for a given id
    @ns.route("/sub-catchments/<id>")
    class SubCatchment(Resource):
        def get(self,id):
            try:
                subcatchment = HydrographyModel.get_sub_catchment(int(id))
                return jsonify(subcatchment)
            except Exception as ex:           
                raise Exception(ex)            

    #select upper sub-catchments
    @ns.route("/sub-catchments/<id>/upper-sub-catchments")
    class upperSubCatchment(Resource):
        def get(self,id):
            try:
                subcatchment = HydrographyModel.get_upper_sub_catchments(int(id))
                return jsonify(subcatchment)
            except Exception as ex:           
                raise Exception(ex)            


    #get navigation
    @ns.route("/sub-catchments/<id>/Navigation")
    class NavigationSubCatchment(Resource):
        def get(self,id):
            try:
                subcatchment = HydrographyModel.get_navigation(int(id))
                return jsonify(subcatchment)
            except Exception as ex:           
                raise Exception(ex)   
# #_________________________________________________________________________
# #-------------------------     demandas-   -------------------------------
# #_________________________________________________________________________
    #get all the demands
    @ns.route("/parametros-usos/demandas", methods=["GET"])
    class demadnas(Resource):
        def get(self):
            try:
                subcatchments = HydrographyModel.get_params_usos_demandas()
                return jsonify(subcatchments)
            except Exception as ex:           
                raise Exception(ex)   

    #Select one deman by id
    @ns.route("/parametros-usos/demandas/<id>")
    class demanda(Resource):
        def get(self,id):
            try:
                subcatchment = HydrographyModel.get_params_usos_demanda(id)
                return jsonify(subcatchment)
            except Exception as ex:           
                raise Exception(ex) 

    #obtain demands for a subcatchment
    @ns.route("/parametros-usos/demandas/<Sub_Catchment_id>")
    class demanda_MELCA(Resource):
        def get(self,Sub_Catchment_id):
            try:
                eco = HydrographyModel.get_usos_demands_sub_catchemnt(int(Sub_Catchment_id))
                return jsonify(eco)  
            except Exception as ex:           
                raise Exception(ex)  

    #obtain ret rates for a subcatchment
    @ns.route("/parametros-usos/returns/<Sub_Catchment_id>")
    class demanda_MELCA(Resource):
        def get(self,Sub_Catchment_id):
            try:
                eco = HydrographyModel.get_ret_demands_sub_catchemnt(int(Sub_Catchment_id))
                return jsonify(eco)   
            except Exception as ex:           
                raise Exception(ex)  

    #Add a demand
    Add_demanda_params = apiflask.model("demandas_params",
                                        {
                                            "id": fields.Integer,
                                            "inic": fields.Integer,
                                            "fin": fields.Integer,
                                            "tipo": fields.String,
                                            "qmax": fields.Float,
                                            "tret": fields.Float,
                                        },)
    #Add param usos
    @ns.route("/parametros-usos/add")
    class Adddemanda(Resource):
        @ns.expect(Add_demanda_params)
        def post(self):
            try:
                payload = request.json
                id = payload['id']
                inic = payload['inic']
                fin = payload['fin']
                tipo = payload['tipo']
                qmax = payload['qmax']
                tret = payload['tret']   

                subcatchment =  param_usos_1(id,  inic,fin,tipo, qmax, tret)
                affected_rows = HydrographyModel.add_demanda(subcatchment)
                if affected_rows == 1:
                    return jsonify({'message': "param usos added"})
            except Exception as ex:           
                raise Exception(ex)  

    #Del param usos
    dell_demanda_params = apiflask.model("dell_demanda_params",
                                        {
                                            "id": fields.String

                                        })

    @ns.route('/parametros-usos/delete', methods=['DELETE'])
    class DELdams(Resource):
        @ns.expect(dell_demanda_params)
        def delete(self):            
            try:
                id=request.json["id"]
                affected_rows = HydrographyModel.delete_demanda(id)                
                if affected_rows == 1:
                    return jsonify({'message': "param usos deleted"})
            except Exception as ex:                
                raise Exception(ex) 

# #_________________________________________________________________________
# #-------------------------     wells       -------------------------------
# #_________________________________________________________________________

#     @ns.route("/wells")
#     class wells(Resource):
#         def get(self):
#             wells = HydrographyModel.get_wells()
#             return jsonify(wells)


#     @ns.route("/wells/<Sub_Catchment_MELCA_id>")
#     class well(Resource):
#         def get(self,Sub_Catchment_MELCA_id):
#             wells = HydrographyModel.get_wells_MELCA(int(Sub_Catchment_MELCA_id))
#             return jsonify(wells)
       
#     Add_well_params = apiflask.model(
#                                     "add_well_params",
#                                     {
#                                         "id": fields.Integer,
#                                         "annualFlow": fields.Float,
#                                         "springFlow": fields.Float,
#                                         "summerFlow": fields.Float,
#                                         "winterFlow": fields.Float,
#                                         "autumnFlow": fields.Float,
#                                         "subCatchmentMELCAid": fields.Integer

#                                     })

#     @ns.route("/Hydrographies/well-add")
#     class AddSubCatchment(Resource):
#         @ns.expect(Add_well_params)
#         def post(self):            
#             payload = request.json           

#             id = payload['id']
#             Annual = payload['annualFlow']
#             Spring = payload['springFlow']
#             Summer = payload['summerFlow']
#             Winter = payload['winterFlow']
#             Autumn = payload['autumnFlow']
#             subCatchmentMELCA = payload['subCatchmentMELCAid']
            
            

#             subcatchment =  Well(id,  Annual,Spring,Summer, Winter, Autumn,subCatchmentMELCA)            
#             affected_rows = HydrographyModel.add_well(subcatchment)

#             if affected_rows == 1:
#                 return jsonify({'message': "sub catchment added"})
#             else:
#                 return jsonify({'message': "Error on insert"})

#     dell_well_params = apiflask.model(
#                                     "dell_well_params",
#                                     {
#                                         "id": fields.Integer
#                                     })

#     @ns.route('/Hydrographies/well-delete', methods=['DELETE'])
#     class DELwells(Resource):
#         @ns.expect(dell_well_params)
#         def delete(self):
            
#             try:
#                 id=request.json["id"]
#                 affected_rows = HydrographyModel.delete_well(id)
                
#                 if affected_rows == 1:
#                     return jsonify({'message': "well deleted"})
#                 else:
#                     return jsonify({'message': "No subcatchment deleted"})

#             except Exception as ex:                
#                 return jsonify({'message': str(ex)}), 500
    
#     update_well_params = apiflask.model(
#                                         "update_well_params",
#                                         {
#                                             "id": fields.Integer,
#                                             "annualFlow": fields.Float,
#                                             "springFlow": fields.Float,
#                                             "summerFlow": fields.Float,
#                                             "winterFlow": fields.Float,
#                                             "autumnFlow": fields.Float,
#                                             "subCatchmentMELCAid": fields.Integer

#                                         },
#                                     )

#     @ns.route('/Hydrographies/well-update', methods=['PUT'])
#     class UPDATEwell(Resource):
#         @ns.expect(update_well_params)
#         def put(self):
#             try:
#                 payload = request.json
#                 id = payload['id']
#                 Annual = payload['annualFlow']
#                 Spring = payload['springFlow']
#                 Summer = payload['summerFlow']
#                 Winter = payload['winterFlow']
#                 Autumn = payload['autumnFlow']
#                 subcatchid = payload['subCatchmentMELCAid']
                

#                 well = Well(id, Annual, Spring, Summer,Winter, Autumn,subcatchid)                
#                 affected_rows = HydrographyModel.update_well(well)
                
#                 if affected_rows == 1:
#                     return jsonify({'message': "well updated"})
#                 else:
#                     return jsonify({'message': "No subcatchment updated"})

#             except Exception as ex:                
#                 return jsonify({'message': str(ex)}), 500
# #_________________________________________________________________________
# #--------------------------     dams       -------------------------------
# #_________________________________________________________________________

#     @ns.route("/dams")
#     class dams(Resource):
#         def get(self):
#             dams = HydrographyModel.get_dams()
#             return jsonify(dams)


#     @ns.route("/dams/<Sub_Catchment_MELCA_id>")
#     class dam(Resource):
#         def get(self,Sub_Catchment_MELCA_id):
#             dams = HydrographyModel.get_dams_MELCA(int(Sub_Catchment_MELCA_id))
#             return jsonify(dams)
 
       
#     Add_dams_params = apiflask.model(
#                                     "Add_dams_params",
#                                     {
#                                         "id": fields.Integer,
#                                         "pointString": fields.Float,
#                                         "damId": fields.Float,
#                                         "name": fields.Float,
#                                         "alias": fields.Float,
#                                         "use": fields.Float,
#                                         "damType": fields.Integer,
#                                         "condition": fields.Integer,
#                                         "basinInfluence": fields.Integer,
#                                         "basinArea": fields.Integer,
#                                         "crestLength": fields.Integer,
#                                         "capacity": fields.Integer,
#                                         "lastEditedDate": fields.Integer,
#                                         "annualFlow": fields.Integer,
#                                         "springFlow": fields.Integer,
#                                         "summerFlow": fields.Integer,
#                                         "autumnFlow": fields.Integer,
#                                         "winterFlow": fields.Integer,
#                                         "subcatchmentMELCAid": fields.Integer

#                                     },
#                                 )

#     @ns.route("/Hydrographies/dams-add")
#     class Adddam(Resource):
#         @ns.expect(Add_dams_params)
#         def post(self):            
#             payload = request.json            

#             id = payload['id']
#             pointString = payload['pointString']
#             damId = payload['damId']
#             name = payload['name']
#             alias = payload['alias']
#             use = payload['use']
#             damType = payload['damType']
#             condition = payload['condition']
#             basinInfluence = payload['basinInfluence']
#             basinArea = payload['basinArea']
#             crestLength = payload['crestLength']
#             capacity = payload['capacity']
#             lastEditedDate = payload['lastEditedDate']
#             annualFlow = payload['annualFlow']
#             springFlow = payload['springFlow']
#             summerFlow = payload['summerFlow']
#             autumnFlow = payload['autumnFlow']
#             winterFlow = payload['winterFlow']
#             subcatchmentMELCAid = payload['subcatchmentMELCAid']         

#             subcatchment =  Dam(
#                 id,  pointString,damId,name, alias, use,damType,condition,basinInfluence,basinArea,crestLength, 
#                 capacity,lastEditedDate,annualFlow,springFlow,summerFlow,autumnFlow,winterFlow,subcatchmentMELCAid)
#             affected_rows = HydrographyModel.add_dam(subcatchment)

#             if affected_rows == 1:
#                 return jsonify({'message': "dam added"})
#             else:
#                 return jsonify({'message': "Error on insert"})

#     dell_dams_params = apiflask.model("dell_dams_params",
#                                     {
#                                         "id": fields.Integer

#                                     })

#     @ns.route('/Hydrographies/dams-delete', methods=['DELETE'])
#     class DELdams(Resource):
#         @ns.expect(dell_dams_params)
#         def delete(self):
            
#             try:
#                 id=request.json["id"]
#                 affected_rows = HydrographyModel.delete_dam(id)
                
#                 if affected_rows == 1:
#                     return jsonify({'message': "dam deleted"})
#                 else:
#                     return jsonify({'message': "No dam deleted"})

#             except Exception as ex:
                
#                 return jsonify({'message': str(ex)}), 500
    


#     @ns.route('/Hydrographies/dams-update', methods=['PUT'])
#     class UPDATEdam(Resource):
#         @ns.expect(Add_dams_params)
#         def put(self):
#             try:
#                 payload = request.json

#                 id = payload['id']
#                 pointString = payload['pointString']
#                 damId = payload['damId']
#                 name = payload['name']
#                 alias = payload['alias']
#                 use = payload['use']
#                 damType = payload['damType']
#                 condition = payload['condition']
#                 basinInfluence = payload['basinInfluence']
#                 basinArea = payload['basinArea']
#                 crestLength = payload['crestLength']
#                 capacity = payload['capacity']
#                 lastEditedDate = payload['lastEditedDate']
#                 annualFlow = payload['annualFlow']
#                 springFlow = payload['springFlow']
#                 summerFlow = payload['summerFlow']
#                 autumnFlow = payload['autumnFlow']
#                 winterFlow = payload['winterFlow']
#                 subcatchmentMELCAid = payload['subcatchmentMELCAid']
                

#                 dams = Dam(
#                     id, pointString, damId, name,alias, use,damType,
#                     condition,basinInfluence,basinArea,crestLength,capacity,
#                     lastEditedDate,annualFlow,springFlow,summerFlow,autumnFlow,
#                     winterFlow,subcatchmentMELCAid)
                
#                 affected_rows = HydrographyModel.update_dam(dams)
                
#                 if affected_rows == 1:
#                     return jsonify({'message': "dam updated"})
#                 else:
#                     return jsonify({'message': "No dam updated"})

#             except Exception as ex:                
#                 return jsonify({'message': str(ex)}), 500

# #_________________________________________________________________________
# #------------------------     ecosystems       ---------------------------
# #_________________________________________________________________________
#     @ns.route("/ecosystems")
#     class dams(Resource):
#         def get(self):
#             eco = HydrographyModel.get_ecosystems()
#             return jsonify(eco)

#     @ns.route("/ecosystems/<Sub_Catchment_MELCA_id>")
#     class dam(Resource):
#         # @ns.expect(SC_params)
#         def get(self,Sub_Catchment_MELCA_id):
#             eco = HydrographyModel.get_ecosystems_MELCA(int(Sub_Catchment_MELCA_id))
#             return jsonify(eco)   
# #_________________________________________________________________________
# #------------------------     irrigations       ---------------------------
# #_________________________________________________________________________

#     @ns.route("/irrigations")
#     class irrigations(Resource):
#         def get(self):
#             eco = HydrographyModel.get_irrigations()
#             return jsonify(eco)


#     @ns.route("/irrigations/<Sub_Catchment_MELCA_id>")
#     class irrigationMELCA(Resource):
#         # @ns.expect(SC_params)
#         def get(self,Sub_Catchment_MELCA_id):
#             eco = HydrographyModel.get_irrigations_MELCA(int(Sub_Catchment_MELCA_id))
#             return jsonify(eco)   

# #_________________________________________________________________________
# #-----------------------     mining_centers       ------------------------
# #_________________________________________________________________________
#     @ns.route("/mining_centers")
#     class mining_centers(Resource):
#         def get(self):
#             eco = HydrographyModel.get_mining_centers()
#             return jsonify(eco)

#     @ns.route("/mining_centers/<Sub_Catchment_MELCA_id>")
#     class mining_centersMELCA(Resource):
#         def get(self,Sub_Catchment_MELCA_id):
#             eco = HydrographyModel.get_mining_centers_MELCA(int(Sub_Catchment_MELCA_id))
#             return jsonify(eco)   
# #_________________________________________________________________________
# #-----------------------     potable_water_demands       -----------------
# #_________________________________________________________________________
#     @ns.route("/potable_water_demands")
#     class potable_water_demands(Resource):
#         def get(self):
#             eco = HydrographyModel.get_potable_water_demands()
#             return jsonify(eco)


#     @ns.route("/potable_water_demands/<Sub_Catchment_MELCA_id>")
#     class potable_water_demandsMELCA(Resource):
#         def get(self,Sub_Catchment_MELCA_id):
#             eco = HydrographyModel.get_potable_water_demands_MELCA(int(Sub_Catchment_MELCA_id))
#             return jsonify(eco)   
# #_________________________________________________________________________
# #---------------------     WATER SOURCES       ---------------------------
# #_________________________________________________________________________


#     @ns.route("/Hydrographies/water-sources/<id>")
#     class get_water_source(Resource):
#         def get(self,id):
#             print(int(id))
#             water_source = HydrographyModel.get_weater_source(int(id))
            
#             if water_source:
#                 return jsonify(water_source)
#             else:
#                 return jsonify({'message': "No water source with this id"})


#     update_water_sources = apiflask.model(
#             "water_source_params",
#             {
#                 "id": fields.Integer,
#                 "pointString": fields.String,
#                 "physiography": fields.String,
#                 "source": fields.String,
#                 "use": fields.String,
#                 "altitude": fields.Float,
#                 "observations": fields.Integer,
#                 "area": fields.Float,
#                 "lastEditedDate": fields.Date,
#                 "lastEditedUser": fields.Integer,

#             },
#         )

#     @ns.route('/Hydrographies/water-sources-update', methods=['PUT'])
#     class UPDATE_water_sources(Resource):
#         @ns.expect(update_water_sources)
#         def put(self):
#             try:
#                 payload = request.json
#                 id = payload['id']
#                 pointString = payload['pointString']
#                 physiography = payload['physiography']
#                 source = payload['source']
#                 use = payload['use']
#                 altitude = payload['altitude']
#                 observations = payload['observations']
#                 area = payload['area']
#                 lastEditedDate = payload['lastEditedDate']
#                 lastEditedUser = payload['lastEditedUser']
                

#                 water_sources = Water_Source(id, pointString, physiography, source,use, altitude,observations,area,lastEditedDate,lastEditedUser)                
#                 affected_rows = HydrographyModel.update_weater_source(water_sources)
                
#                 if affected_rows == 1:
#                     return jsonify({'message': "water source updated"})
#                 else:
#                     return jsonify({'message': "No water source updated"})

#             except Exception as ex:                
#                 return jsonify({'message': str(ex)}), 500

#     dell_water_sources_params = apiflask.model(
#         "well_params",
#         {
#             "id": fields.Integer

#         },
#     )

#     @ns.route('/Hydrographies/water-sources-delete', methods=['DELETE'])
#     class DELwater_sources(Resource):
#         @ns.expect(dell_water_sources_params)
#         def delete(self):
            
#             try:
#                 id=request.json["id"]
#                 affected_rows = HydrographyModel.delete_weater_source(id)
                
#                 if affected_rows == 1:
#                     return jsonify({'message': "water source deleted"})
#                 else:
#                     return jsonify({'message': "No subcatchment deleted"})

#             except Exception as ex:
                
#                 return jsonify({'message': str(ex)}), 500
# #_________________________________________________________________________
# #---------------------     PARAMETROS LEM       --------------------------
# #_________________________________________________________________________
#     @ns.route("/parametros-LEM/")
#     class get_water_source(Resource):
#         def get(self):            
#             LEM = HydrographyModel.get_prametros_LEM()            
#             if LEM:
#                 return jsonify(LEM)
#             else:
#                 return jsonify({'message': "something went wrong"})

#     @ns.route("/parametro-LEM/<id>")
#     class SubCatchment(Resource):
#         def get(self,id):
#             subcatchment = HydrographyModel.get_prametro_LEM(int(id))
#             return jsonify(subcatchment)



#     @ns.route("/tablas-LEM/historical")
#     class get_tablas_LEM(Resource):
#         def get(self):
#             station_id = '1'
#             station_name = 'Abusu'

#             response = HydrographyModel().get_historial(station_id, station_name)
#             response = response.to_json()
            
#             if response:
#                 return jsonify(response)
#             else:
#                 return jsonify({'message': "something went wrong"})            

#     @ns.route("/tablas-LEM/observado")
#     class get_tablas_LEM(Resource):
#         def get(self):
#             station_id = '1'
#             station_name = 'Abusu'

#             response = HydrographyModel().get_observado(station_id, station_name)
#             response = response.to_json()

            
#             if response:
#                 return jsonify(response)
#             else:
#                 return jsonify({'message': "something went wrong"})    

#     @ns.route("/tablas-LEM/forecast")
#     class get_tablas_LEM(Resource):
#         def get(self):
#             station_id = '1'
#             station_name = 'Abusu'

#             response = HydrographyModel().get_forecast(station_id, station_name)
#             response = response.to_json()
            
#             if response:
#                 return jsonify(response)
#             else:
#                 return jsonify({'message': "something went wrong"})  
# #_________________________________________________________________________
# #---------------------     MELCA TABLES       ----------------------------
# #_________________________________________________________________________

#     @ns.route("/parametros-MELCA/")
#     class get_tablas_CHAMBO(Resource):
#         def get(self):
            
#             chambo_param = HydrographyModel.get_chambo_param()
            
#             if chambo_param:
#                 return jsonify(chambo_param)
#             else:
#                 return jsonify({'message': "something went wrong"})

#     @ns.route("/tablas-MELCA/prec")
#     class get_prec(Resource):
#         def get(self):
#             response = HydrographyModel().get_prec_Chambo()
#             response = response.to_json()
            
#             if response:
#                 return jsonify(response)
#             else:
#                 return jsonify({'message': "something went wrong"})  

#     @ns.route("/tablas-MELCA/tmin")
#     class get_tmin(Resource):
#         def get(self):
#             response = HydrographyModel().get_tmin_Chambo()
#             response = response.to_json()
            
#             if response:
#                 return jsonify(response)
#             else:
#                 return jsonify({'message': "something went wrong"})  

#     @ns.route("/tablas-MELCA/tmax")
#     class get_tmax(Resource):
#         def get(self):

#             response = HydrographyModel().get_tmax_Chambo()
#             response = response.to_json()
           
#             if response:
#                 return jsonify(response)
#             else:
#                 return jsonify({'message': "something went wrong"})  


