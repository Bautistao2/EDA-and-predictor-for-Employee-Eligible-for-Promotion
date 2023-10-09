from msilib.schema import Component
import streamlit as st
import pandas as pd
import pickle 
import pickle
from pickle import dump
import pygwalker as pyg
import streamlit.components.v1 as components
from sklearn.ensemble import RandomForestClassifier



def run():
    #IMPORTO IMAGENES QUE SERAN VISIBLES EN EL APP
    from PIL import Image
    imagen1 = Image.open('./images/hrana.png')
    imagen2 = Image.open('./images/hr2.jpg')
    imagen2 = imagen2.resize((650,200))

    st.image(imagen2,use_column_width=False)

    #AÑADO UN SELETBOX PARA QUE EL USUARIO ELIGA ENTRE GRAFICAR O HACER LA PREDICCION
    add_selectbox = st.sidebar.selectbox(
    "Escoge una opción",
    ("Realizar la predicción", "Ir a gráficos"))

    st.sidebar.info('Apreciado usuario, puede saber si un empleado será promovido, o hacer graficos')
        
    st.sidebar.image(imagen1)

    st.title("PEAPP, Promoción Efectiva para sus empleados")
    
    #SI EL USUARIO ELIGE REALIZAR LA PREDICCION, AQUÍ SE RECOGEN LAS VARIABLES
    if add_selectbox == 'Realizar la predicción':
        
        st.write('A continuación deberá ingresar la información de su empleado')
        department1 = st.slider('Seleccione el departamento en donde trabaja, 0.Analitics, 1.Finanzas, 2.HR, 3.Legal, 4.Operaciones, 5.Compra, 6.RyD, 7.VentasYMarketing, 8.tecnología', 0,8,1)
        Edad = st.number_input('Ingrese la edad', min_value=1, max_value=100, value=25)
        st.write('Seleccione el sexo del empleado')
        mujer =  st.checkbox ("Mujer")
        hombre =  st.checkbox ("Hombre")
        if mujer :
            sexo = 0
        else :
            sexo = 1     
                   
        educacion = st.slider('El nivel de educacion. 0.Bachiller, 1.Especialista, 2.Magister', 0,2,1)
        reclutamiento = st.slider('El medio del reclutamiento fue: 2.Sourcing, 1.Referido, 0.Otro', 0,2,1)
        numerodeentrenamientos = st.selectbox('No de intentos de promoción', [0,1,2,3,4,5])
        Entrenamientos_previos = st.selectbox('Calificación del empleado en el ultimo año', [0,1,2,3,4,5])
        servicio = st.number_input('Años que lleva en la empresa', min_value=1, max_value=37, value=25)
        
        if st.checkbox('Posee KPIS>80%? '):
            KIPs_met = 0
               
        else:
            KIPs_met = 1
                
        
        if st.checkbox('Ha ganado algún premio en el último año?'):
            awards_won = 0
        else:
            awards_won = 1
            
                   
        Avg_training_score = st.number_input('Puntuación media de las evaluaciones de formación actuales', min_value=1, max_value=100, value=25)
    
        
        region = st.number_input('Region en donde está el empleado', min_value=1, max_value=35, value=25)

        output=""
        
      #CREO UNA LISTA CON TODAS LAS VARIABLES O INFO RECOGIDAS  ANTERIORMENTE POR EL USUARIO , DEL EMPLEADO
        input_dict = [department1 , region , educacion,  sexo, reclutamiento,  numerodeentrenamientos,  Edad,  Entrenamientos_previos,  servicio,  KIPs_met,  awards_won ,  Avg_training_score]
        
        
       #REALIZO LA PREDICCIÓN
        if st.button("Predecir"):
            #LLAMO AL ARCHIVO .PKL, 
            nombreArchivo = 'modelpredictionppe.pkl'
            modeloCargado = pickle.load(open('modelpredictionppe.pkl', 'rb'))
            prediccion = modeloCargado.predict([input_dict])
            if  prediccion == 0:
                st.write('El empleado no será promovido')
            else:
                 st.write('El empleado será promovido')
            st.write('llamar al empleado para comunicarselo')     
                 
              
    #SI EL USUARIO HA ESCOGIDO LA OPCION DE IR A GRAFICOS, SE AÑADE LA LIBRERIA QUE PERMITE REALIZAR GRAFICOS
    #CON LA INFO DEL DATASET
    if add_selectbox == 'Ir a gráficos':
       #VISUALIZO EL DATASET, PRIMERO, LUEGO REALIZO GRAFICOS 
       df = pd.read_csv("hrdatatest.csv")
       st.dataframe(df, height=300)
       pyg_html = pyg.walk(df, return_html=True)
       components.html(pyg_html, height=1000, scrolling=True)
       
        
        
if __name__ == '__main__':
    run() 
      