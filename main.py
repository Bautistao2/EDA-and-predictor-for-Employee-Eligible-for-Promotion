
import streamlit as st
import pandas as pd
import pickle 
import pickle
from pickle import dump



  
def run():

    from PIL import Image
    imagen1 = Image.open('hrana.png')
    imagen2 = Image.open('hr2.jpg')
    imagen2 = imagen2.resize((650,200))

    st.image(imagen2,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "Cómo te gustaría ingresar la información?",
    ("En linea", "subir un archivo"))

    st.sidebar.info('Apreciado usuario, elija la manera en la que desea introducir la información del empleado, tenga en cuenta que si elige batch tendrá que subir un archivo de formato csv cuyos datos deben ser acordes a la numeración utilizada en la app al ingresar de manera manual la información del empleado (numerica).')
    st.sidebar.success('Para soporte técnico, contacte con nosotros https://www.apersonal.com')
    
    st.sidebar.image(imagen1)

    st.title("PEAPP, Promoción Efectiva para sus empleados")

    if add_selectbox == 'En linea':
        
        st.write('A continuación deberá ingresar la información de su empleado')
        department1 = st.number_input('Seleccione el departamento en donde trabaja, 0.Analitics, 1.Finanzas, 2.HR, 3.Legal, 4.Operaciones, 5.Compra, 6.RyD, 7.VentasYMarketing, 8.tecnologia', min_value=0, max_value=8, value=0)
        Edad = st.number_input('Ingrese la edad', min_value=1, max_value=100, value=25)
        sexo = st.number_input('Genero 0. Mujer, 1. Hombre', min_value=0, max_value=1, value=0)
        educacion = st.slider('El nivel de educacion. 0.Bachiller, 1.Especialista, 2.Magister', 0,2,1)
        reclutamiento = st.slider('El medio del reclutamiento fue: 2.Sourcing, 1.Referido, 0.Otro', 0,2,1)
        numerodeentrenamientos = st.selectbox('No de entreamientos posteriores', [0,1,2,3,4,5])
        Entrenamientos_previos = st.selectbox('Puntuacion del entrenamiento pasado', [0,1,2,3,4,5])
        servicio = st.number_input('Años que lleva en la empresa', min_value=1, max_value=37, value=25)
        
        if st.checkbox('Posee KIPS>80%? '):
            KIPs_met = 0
               
        else:
            KIPs_met = 1
                
        
        if st.checkbox('Ha ganado algún premio?'):
            awards_won = 0
        else:
            awards_won = 1
            
                   
        Avg_training_score = st.number_input('Promedio de puntuaciones entrenamientos pasados', min_value=1, max_value=100, value=25)
    
        
        region = st.number_input('Region en donde está el empleado', min_value=1, max_value=35, value=25)

        output=""
        
         
        input_dict = [department1 , region , educacion,  sexo, reclutamiento,  numerodeentrenamientos,  Edad,  Entrenamientos_previos,  servicio,  KIPs_met,  awards_won ,  Avg_training_score]
        
        
        

        if st.button("Predecir"):
            
            nombreArchivo = 'modelohr.pkl'
            modeloCargado = pickle.load(open('modelohr.pkl', 'rb'))
            prediccion = modeloCargado.predict([input_dict])
            if  prediccion == 0:
                st.write('El empleado no será promovido')
            else:
                 st.write('El empleado será promovido')
                 
              

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predicciones = pickle.load(open('modelohr.pkl', 'rb'))
            resultado = predicciones.predict([data])
            st.write(resultado)
        
if __name__ == '__main__':
    run() 
      