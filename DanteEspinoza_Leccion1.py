import pandas as pd
import matplotlib.pyplot as plt

#Autor: Dante Espinoza

# finanzas2020 -> Ingreso/gastos mensuales

# '''
# REQUERIMIENTOS:
# Implemente un programa que lea el contenido del fichero y realice los
# siguientes cálculos:
# 1- ¿Qué mes se ha gastado más? -> SUMATORIA(-)_DE_CADA_MES->COMPARARLOS. EL MAYOR
# 2- ¿Qué mes se ha ahorrado más? -> MES EN QUE SE HA GASTADO MENOS. EL MENOR
# 3- ¿Cuál es la media de gastos al año? -> SOLO SUMO GASTOS PARA ESTO
# 4- ¿Cuál ha sido el gasto total a lo largo del año?.  -> Sumatoria de solo valores negativos 
# 5- ¿Cuáles han sido los ingresos totales a lo largo del año? -> Sumatoria de valores positivos
# 6- Opcional: Realice una gráfica de la evolución de ingresos a lo largo del año.
# '''

'''

    Función que abre el Dataset, convierte valores de muestra a int64 " COMO ME COSTO!!! "

'''
 # hacer excepciones para valores no enteros, cadenas, numeros con cosas raras como '33'

class NoDataframeException(Exception):
    def __init__(self, message):
        super().__init__(message)
    
class gastosPositivosException(Exception):
    def __init__(self, message):
        super().__init__(message)
    

def getDataFrameCleansed():
    fichero="finanzas2020.csv"
    df=[]
    try:
    
        df = pd.read_csv(fichero, sep='\t') # parth fichero.csv
        colTempMeses=[] 
        for j in range(len(df.columns)): #df.columns obtengo JSON nombres de columnas del Dataset y +
            colTempMeses.append(df.columns[j]) # Extraigo solo nombre de columnas
            if (df.dtypes[j] != "int64"): # dtypes: filtro tipo de datos de columna [i] de la muestra
                df=df.replace(regex={'\'':'',r'[A-z/]':'0'}) # limpio muestra
                df[colTempMeses[j]] = df[colTempMeses[j]].astype("int64") #Convierto a int64 muestras diferentes    
        # print(df.dtypes) print(df.to_string())
        return df
    except FileNotFoundError as er:
        print (f" Acá {er}")
        return df


##SUMO LOS GASTOS DIARIOS DE CADA MES Y EVALÚO EL MES CON MAYOR VALOR ABSOLUTO "LO QUE MÁS SE GASTO!!" 
def obtenerMesDeMAYORgasto():   
    gastoYmes=[]
    df = getDataFrameCleansed() #Obtengo el DataFrame
    listaMesesYgastos=df.where(df < 0).sum()
    for mes,gasto in listaMesesYgastos.items():
        if gasto == listaMesesYgastos.min():
            if gasto > 0: # SI SE CAMBIA EL SIGO, A menor <, Salta la Exception
                raise gastosPositivosException("Los gastos no pueden ser positivos")
            else:
                gastoYmes.append(int(gasto))
                gastoYmes.append((mes))
    return gastoYmes

##El mes de mayor ahorro es el de menos gastos
def obtenerMesDeMAYORahorro():
    ahorroMes=[]
    df = getDataFrameCleansed()
    listaMesesYgastos=df.where(df < 0).sum()
    for mes,ahorro in listaMesesYgastos.items():
        if ahorro == listaMesesYgastos.max():
            ahorroMes.append((mes))
            ahorroMes.append(int(ahorro))
    return ahorroMes

def calcularGastoTotalAnual():
    df = getDataFrameCleansed()
    listaGastosMensuales=df.where(df < 0).sum()
    gatoAnual= listaGastosMensuales.sum()
    # print(f" Gasto anual {gatoAnual}")
    return gatoAnual
    
    

def calcularMediaDeGastoPorAño(gastoAnual):
    df = getDataFrameCleansed()
    listaGastosMensuales=df.where(df < 0).sum()
    mediaDegastoAnual=int(gastoAnual/listaGastosMensuales.count())
    # print(f"media {mediaDegastoAnual *-1}")
    return mediaDegastoAnual
    

def calcularIngresoTotalAnual():
    df = getDataFrameCleansed()
    listaIngresosMensuales=df.where(df > 0).sum()
    return listaIngresosMensuales.sum()

def graficarEvolucionDeIngresoAnual():
    df = getDataFrameCleansed()
    listaIngresosMensuales=df.where(df > 0).sum()
    plt.plot(listaIngresosMensuales,label='IngresosMensuales', linewidth=2)
    plt.ylabel('Ingresos')
    plt.xlabel('Meces')
    plt.legend()
    plt.grid(True)
    listarIngresosAnuales(listaIngresosMensuales)
    plt.show()


def listarIngresosAnuales(ingresosAnuales):
    print(f"Lista de gastos anuales{[ingresosAnuales]} ")

def mostrarResultados():

    df = getDataFrameCleansed()

    if  len(df)==0:
       raise NoDataframeException("El fichero para iniciar el Dataframe no existe")
    else:

        mesGAsto = obtenerMesDeMAYORgasto()
        print(f"EL mes de mayor gasto fue  {mesGAsto[0]} con |{mesGAsto[1]}| = {mesGAsto[1] *-1} unidades monetarias. MÁXIMO GASTADO!!")
        
        mesAhorro = obtenerMesDeMAYORahorro()
        print(f"EL mes de mayor ahorro fue  {mesAhorro[0]} con |{mesAhorro[1]}| = {mesAhorro[1] *-1} unidades monetarias. MÍNIMO GASTADO!! ")

        gastoAnual = int(calcularGastoTotalAnual())
        print(f"El gasto anual fue de |{gastoAnual}| = {gastoAnual *-1} unidades monetarias. GASTO EN TODO EL AÑO!! ")
        
        mediaGastosAnual= calcularMediaDeGastoPorAño(gastoAnual)
        print(f"La media del gasto anual fue de |{mediaGastosAnual}| = {mediaGastosAnual *-1} unidades monetarias. SE GASTO EN PROMEDIO EN TODO EL AÑO!! ")

        ingresoTotalAnual=calcularIngresoTotalAnual()
        print(f"Ingreso total anual fue de {int(ingresoTotalAnual)}")

        graficarEvolucionDeIngresoAnual()
            

mostrarResultados()

