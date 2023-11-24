import streamlit as st
import pandas as pd
import pickle 
from pickle import dump
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from sklearn.ensemble import RandomForestClassifier



def run():
    #Import Images
    from PIL import Image
    imagen1 = Image.open('./images/hrana.png')
    imagen2 = Image.open('./images/hr2.jpg')
    imagen2 = imagen2.resize((650,200))

    st.image(imagen2,use_column_width=False)

 
    #Main Menu
    st.sidebar.image(imagen1)
    with st.sidebar:
        add_selectbox = option_menu("Select an Option",["Realizar la predicción","Analyze The Data","Ir a gráficos", ],
             icons=['house', 'search',"house"], menu_icon="menu-down", default_index=1)                       
    
    st.sidebar.info('Apreciado usuario, puede saber si un empleado será promovido, o hacer graficos')
        
    

    st.title("Predictor of Employee Elegible to Promotion")
    
    #Input the information of the employee or variables
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
        
      #Create a List with the variables 
        input_dict = [department1 , region , educacion,  sexo, reclutamiento,  numerodeentrenamientos,  Edad,  Entrenamientos_previos,  servicio,  KIPs_met,  awards_won ,  Avg_training_score]
        
        
       #Make the prediction
        if st.button("Predecir"):
            #Import model file .PKL, 
            nombreArchivo = 'modelpredictionppe.pkl'
            modeloCargado = pickle.load(open('modelpredictionppe.pkl', 'rb'))
            prediccion = modeloCargado.predict([input_dict])
            if  prediccion == 0:
                st.write('El empleado no será promovido')
            else:
                 st.write('El empleado será promovido')
            st.write('llamar al empleado para comunicarselo')     
                 
              
    
    
    if add_selectbox == 'Analyze The Data':
        import pandas as pd
        from ydata_profiling import ProfileReport
        import matplotlib 
        import matplotlib.backends.backend_tkagg
        from streamlit_pandas_profiling import st_profile_report 
        
        
        df = pd.read_csv("hrdata.csv")
        df.education = df.education.fillna("Bachelor's")
        df.previous_year_rating = df.previous_year_rating.fillna(3.0)
        df= df.rename(columns={'employee_id':'Emp_ID', 'department':'Department','region':'No_of_Region','education':'Level_of_education','gender':'Gender','recruitment_channel':'Recruitment_channel','no_of_trainings' :'No_of_other_trainings_completed','age':'Age','previous_year_rating':'Performance_Score', 'length_of_service':'Length_of_service','KPIs_met >80%':'High_KPIS','awards_won?':'Awards_won','avg_training_score':'Average_score_evaluations' })
        
        st.write("## Analyze the Data:") 
        profile = ProfileReport(df,  title="Profiling Report")
        st_profile_report(profile) 
        
        
       
if __name__ == '__main__':
    run() 
      