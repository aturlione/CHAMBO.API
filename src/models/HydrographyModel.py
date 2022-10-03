from .entities.Hydrography import  Well,Sub_Catchment_Melca, Water_Source, Parametros_LEM, Param_Chambo,Dam,ecosystems,irrigations,mining_centers,potable_water_demands,param_demandas,param_demandas_tipos,param_demandas_info,Navigation,param_ret
import pandas as pd
import os

import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex



class HydrographyModel():

    @classmethod
    def get_sub_catchments_MELCA(self):
        
        try:
            connection = get_connection()
            subcatchments = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM chambo ORDER BY id ASC")
                resultset = cursor.fetchall()
                
                for row in resultset:
                    subcatchment = Sub_Catchment_Melca(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8])
                    subcatchments.append(subcatchment.to_JSON())

            connection.close()
            return subcatchments
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_sub_catchment_MELCA(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM chambo WHERE id = %s", (id,))
                row = cursor.fetchone()

                subcatchment = None
                if row != None:
                    subcatchment = Sub_Catchment_Melca(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8] )
                    subcatchment = subcatchment.to_JSON()

            connection.close()
            return subcatchment
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def get_upper_sub_catchments(self,id):
        
        try:
            connection = get_connection()
            subcatchments = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM chambo WHERE "Drena_a" = %s', (id,))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    subcatchment = Sub_Catchment_Melca(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8])
                    subcatchments.append(subcatchment.to_JSON())

            connection.close()
            return subcatchments
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_navigation(self,id):
        
        try:
            connection = get_connection()
            subcatchments = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id FROM chambo WHERE "Drena_a" = %s', (id,))
                resultset = cursor.fetchall()
                resultset = [resultset[i][0] for i in range(0,len(resultset))]
                print(resultset)
                cursor.execute('SELECT "Drena_a" FROM chambo WHERE id = %s', (id,))
                resultset2 = cursor.fetchall()
                resultset2 = [resultset2[i][0] for i in range(0,len(resultset2))]
                print(resultset2)
                
                if resultset:
                    isOrigin=False
                else:
                    isOrigin=True

                subcatchment = Navigation(list(resultset), list(resultset2),isOrigin=isOrigin)
                subcatchment = subcatchment.to_JSON()
                print(subcatchment)

            connection.close()
            return subcatchment
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------     Demandas    -----------------------------------
#_________________________________________________________________________
    @classmethod
    def get_params_usos_demandas(self):
        
        try:
            connection = get_connection()
            subcatchments = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM param_usos_demandas ORDER BY "ID" ASC')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    subcatchment = param_demandas(row[0], row[1], row[2], row[3],row[4], row[5])
                    subcatchments.append(subcatchment.to_JSON())

            connection.close()
            return subcatchments
        except Exception as ex:
            raise Exception(ex)  

    @classmethod
    def get_params_usos_demanda(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM param_usos_demandas WHERE "ID" = %s', (id,))
                row = cursor.fetchone()

                subcatchment = None
                if row != None:
                    subcatchment = param_demandas(row[0], row[1], row[2], row[3],row[4], row[5])
                    subcatchment = subcatchment.to_JSON()

            connection.close()
            return subcatchment
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_usos_demands_MELCA(self,Sub_Catchment_MELCA_id):
        try:
            connection = get_connection()
            wells = []
            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM param_usos_demandas WHERE "INIC" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()
                print('------------------------------------------>',resultset)
                for row in resultset:
                    well = param_demandas(row[0], row[1], row[2], row[3],row[4],row[5])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ret_demands_MELCA(self,Sub_Catchment_MELCA_id):
        try:
            connection = get_connection()
            wells = []
            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM param_usos_demandas WHERE "FIN" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()
                print('------------------------------------------>',resultset)
                for row in resultset:
                    well = param_ret(row[0], row[1], row[2], row[3],row[4],row[5])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_demanda(self, well):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO param_usos_demandas ("ID", "INIC", "FIN", "TIPO", "QMAX", "TRET") 
                                    VALUES (%s, %s, %s, %s, %s, %s)""", (well.id, well.inic, well.fin,well.tipo ,well.qmax))
                
                affected_rows = cursor.rowcount
        
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
           
            raise Exception(ex)

    @classmethod
    def delete_demanda(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM param_usos_demandas WHERE "ID" = %s', (id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
#_________________________________________________________________________
#---------------------     WELLS       -----------------------------------
#_________________________________________________________________________
    @classmethod
    def get_wells(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM wells ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = Well(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_wells_MELCA(self,Sub_Catchment_MELCA_id):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM wells WHERE "subCatchmentMELCAid" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()

                for row in resultset:
                    well = Well(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_well(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM wells WHERE id = %s", (id,))
                row = cursor.fetchone()

                if row != None:
                    well = Well(row[0], row[1], row[2], row[3],row[4],row[5],row[6]  )
                    well = well.to_JSON()

            connection.close()
            return well
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_well(self, well):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO wells (id,  "annualFlow", "springFlow", "summerFlow", "winterFlow", "autumnFlow", "subCatchmentMELCAid") 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s)""", (well.id, well.annualFlow, well.springFlow,well.summerFlow ,well.winterFlow,well.autumnFlow ,well.subCatchmentMELCA))
                
                affected_rows = cursor.rowcount
        
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
           
            raise Exception(ex)

    @classmethod
    def update_well(self, well):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE wells SET  "annualFlow" = %s, "springFlow" = %s, "summerFlow" = %s , "winterFlow" = %s, "autumnFlow" = %s, "subCatchmentMELCAid" = %s
                               WHERE id = %s""", (  well.annualFlow, well.springFlow,well.summerFlow ,well.winterFlow,well.autumnFlow ,well.subCatchmentMELCA,well.id))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            
            raise Exception(ex)


    @classmethod
    def delete_well(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM wells WHERE id = %s", (int(id),))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
  
#_________________________________________________________________________
#---------------------     DAMS       -----------------------------------
#_________________________________________________________________________
    @classmethod
    def get_dams(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM dams ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = Dam(row[0], row[1], row[2], row[3],row[4],row[5],row[6])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_dams_MELCA(self,Sub_Catchment_MELCA_id):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM dams WHERE "subcatchmentMELCAid" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()

                for row in resultset:
                    well = Dam(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_dam(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM dams WHERE id = %s", (id,))
                row = cursor.fetchone()

                if row != None:
                    well = Dam(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21])
                    well = well.to_JSON()

            connection.close()
            return well
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_dam(self, well):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                
                cursor.execute("""INSERT INTO dams (id, , "pointString", "damId", name, alias, use, "damType", condition, "basinInfluence", "damRiver", "basinArea", height, "crestLength", capacity, "lastEditedDate", "lastEditedUser", "annualFlow", "springFlow", "summerFlow", "autumnFlow", "winterFlow", "subCatchmentMELCAid") 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (well.id, well.pointString, well.damId,well.name ,well.alias,well.use ,well.damType ,well.condition ,well.basinInfluence ,well.damRiver ,well.basinArea ,well.height ,well.crestLength,well.crestLength,well.crestLength,well.capacity,well.lastEditedDate,well.lastEditedUser,well.annualFlow,well.springFlow,well.summerFlow,well.winterFlow,well.subCatchmentMELCAid))
                
                affected_rows = cursor.rowcount
        
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
           
            raise Exception(ex)

    @classmethod
    def update_dam(self, dam):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE wells SET  "pointString" = %s, "damId" = %s, name = %s , alias = %s, use = %s, "damType" = %s, condition = %s, "basinInfluence" = %s, "damRiver" = %s, "basinArea" = %s, height = %s, "crestLength" = %s, capacity = %s, "lastEditedDate" = %s, capacity = %s, "lastEditedUser" = %s, "annualFlow" = %s,  "springFlow" = %s,  "summerFlow" = %s,  "autumnFlow" = %s,  "winterFlow" = %s,  "subCatchmentMELCAid" = %s,  "springFlow" = %s
                               WHERE id = %s""", (  dam.pointString, dam.damId,dam.name ,dam.alias,dam.use ,dam.damType ,dam.condition ,dam.basinInfluence ,dam.damRiver ,dam.basinArea ,dam.height ,dam.crestLength,dam.crestLength,dam.crestLength,dam.capacity,dam.lastEditedDate,dam.lastEditedUser,dam.annualFlow,dam.springFlow,dam.summerFlow,dam.winterFlow,dam.subCatchmentMELCAid,dam.id))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            
            raise Exception(ex)


    @classmethod
    def delete_dam(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM dams WHERE id = %s", (int(id),))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------     ecosystems       -----------------------------------
#_________________________________________________________________________
    @classmethod
    def get_ecosystems(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM ecosystems ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = ecosystems(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ecosystems_MELCA(self,Sub_Catchment_MELCA_id):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM ecosystems WHERE "subcatchmentMELCAid" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()

                for row in resultset:
                    well = ecosystems(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------     irrigations   ---------------------------------
#_________________________________________________________________________
    @classmethod
    def get_irrigations(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM irrigations ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = irrigations(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_irrigations_MELCA(self,Sub_Catchment_MELCA_id):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM irrigations WHERE "subcatchmentMELCAid" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()

                for row in resultset:
                    well = irrigations(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)


#_________________________________________________________________________
#---------------------     mining_centers---------------------------------
#_________________________________________________________________________
    @classmethod
    def get_mining_centers(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM mining_centers ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = mining_centers(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_mining_centers_MELCA(self,Sub_Catchment_MELCA_id):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM mining_centers WHERE "subCatchmentMELCAid" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()

                for row in resultset:
                    well = mining_centers(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------    potable_water_demands --------------------------
#_________________________________________________________________________
    @classmethod
    def get_potable_water_demands(self):
        
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT * FROM potable_water_demands ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    well = potable_water_demands(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_potable_water_demands_MELCA(self,Sub_Catchment_MELCA_id):
        print(Sub_Catchment_MELCA_id)
        try:
            connection = get_connection()
            wells = []

            with connection.cursor() as cursor:
               
                cursor.execute('SELECT * FROM potable_water_demands WHERE "subcatchmentMELCAid" = %s', (Sub_Catchment_MELCA_id,))
                
                resultset = cursor.fetchall()

                for row in resultset:
                    well = potable_water_demands(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22])
                    wells.append(well.to_JSON())

            connection.close()
            return wells
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------     WATER SOURCES       ----------------------------
#_________________________________________________________________________
    @classmethod
    def get_weater_source(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM water_sources WHERE id = %s", (id,))
                row = cursor.fetchone()
                if row != None:
                    water_source = Water_Source(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    water_source = water_source.to_JSON()
                    connection.close()
                    return water_source
                else:
                    connection.close()
                    return {'message':'no water sources'}

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_weater_source(self, water_source):
        
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                
                cursor.execute("""UPDATE water_sources SET  "pointString" = %s, physiography = %s, source = %s , use = %s, altitude = %s, observations = %s, area = %s, "lastEditedDate"= %s, "lastEditedUser"= %s 
                               WHERE id = %s""", (  water_source.pointString, water_source.physiography,water_source.source ,water_source.use,water_source.altitude ,water_source.observations,water_source.area,water_source.lastEditedDate,water_source.lastEditedUser,water_source.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:            
            raise Exception(ex)

    @classmethod
    def delete_weater_source(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                print('------------------------------------------------------------')
                cursor.execute("DELETE FROM water_sources WHERE id = %s", (id,))
                print('............................................................')
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------     PARAMETROS LEM       ----------------------------
#_________________________________________________________________________
    @classmethod
    def get_prametros_LEM(self):
        
        try:
            connection = get_connection()
            pars_LEM = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM "Parametros_LEM" ORDER BY id ASC')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    par_LEM = Parametros_LEM(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    pars_LEM.append(par_LEM.to_JSON())

            connection.close()
            return pars_LEM
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_prametro_LEM(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM "Parametros_LEM" WHERE id = %s', (id,))
                row = cursor.fetchone()

                
                if row != None:
                    par = Parametros_LEM(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    par = par.to_JSON()

            connection.close()
            return par
        except Exception as ex:
            raise Exception(ex)

#_________________________________________________________________________
#---------------------     LEM TABLES       ------------------------------
#_________________________________________________________________________
    @classmethod
    def get_historial(self, id, station_name):
        try:
            station_id = 'C0B{}'.format(str(id))
            base_dir = os.getcwd()
    
            df_sim_historical = pd.read_excel(os.path.join(base_dir, "LEM_TABLES","{}_{}_historical.xlsx".format(station_id, station_name)),
                                      index_col="fecha", parse_dates=True)
            
            
            return df_sim_historical
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_observado(self, id, station_name):
        try:
            station_id = 'C0B{}'.format(str(id))
            base_dir = os.getcwd()

            file_name_obs = "{}_{}_observado.xlsx".format(station_id, station_name) # Prec 	ETP 	Temp 	Caudal
            df_obs = pd.read_excel(os.path.join(base_dir, "LEM_TABLES", file_name_obs), 
                           index_col="fecha", parse_dates=True)
            
            return df_obs
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_forecast(self, id, station_name):
        try:
            station_id = 'C0B{}'.format(str(id))
            base_dir = os.getcwd()

            file_name_forecast = "{}_{}_meteorological_forecast.xlsx".format(station_id, station_name)
            df_forcing_forecast = pd.read_excel(os.path.join(base_dir, "LEM_TABLES", file_name_forecast),
                                                index_col="fecha", parse_dates=True)
            
            return df_forcing_forecast
        except Exception as ex:
            raise Exception(ex)
#_________________________________________________________________________
#---------------------     MELCA TABLES       ------------------------------
#_________________________________________________________________________
    @classmethod
    def get_chambo_param(self):
        
        try:
            connection = get_connection()
            params = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM "Param_Chambo_niv7" ORDER BY id ASC')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    subcatchment = Param_Chambo(row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7] )
                    params.append(subcatchment.to_JSON())

            connection.close()
            
            return params
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_prec_Chambo(self):
        try:
            base_dir = os.getcwd()

            file_name_series = "Series_Chambo_niv7.xlsx"
            df_forcing_series = pd.read_excel(os.path.join(base_dir, "LEM_TABLES", file_name_series),
                                                index_col="fechas", parse_dates=True, sheet_name= "prec")
            
            return df_forcing_series
        except Exception as ex:
            raise Exception(ex)
    @classmethod

    def get_tmin_Chambo(self):
        try:
            base_dir = os.getcwd()

            file_name_series = "Series_Chambo_niv7.xlsx"
            df_forcing_series = pd.read_excel(os.path.join(base_dir, "LEM_TABLES", file_name_series),
                                                index_col="fechas", parse_dates=True, sheet_name= "tmin")
            
            return df_forcing_series
        except Exception as ex:
            raise Exception(ex)

    def get_tmax_Chambo(self):
        try:
            base_dir = os.getcwd()

            file_name_series = "Series_Chambo_niv7.xlsx"
            df_forcing_series = pd.read_excel(os.path.join(base_dir, "LEM_TABLES", file_name_series),
                                                index_col="fechas", parse_dates=True, sheet_name= "tmax")
            
            return df_forcing_series
        except Exception as ex:
            raise Exception(ex)
