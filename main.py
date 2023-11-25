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

    st.image(imagen2)

 
    #Main Menu
    st.sidebar.image(imagen1)
    with st.sidebar:
        add_selectbox = option_menu("Select an Option",["Realizar la predicción","Analyze The Data","Ir a gráficos", ],
             icons=['house', 'search',"house"], menu_icon="menu-down", default_index=1)                       
    
    
        
    

    st.title("Predictor of Employee Elegible to Promotion")
    
    #Input the information of the employee or variables
    if add_selectbox == 'Realizar la predicción':
        
        st.write('Next, you will need to enter the employee information')
        department1 = st.slider('Select the Department, 0.Analitics, 1.Finanzas, 2.HR, 3.Legal, 4.Operaciones, 5.Compra, 6.RyD, 7.VentasYMarketing, 8.tecnología', 0,8,1)
        Edad = st.number_input('Age', min_value=1, max_value=100, value=25)
        st.write('Gender')
        mujer =  st.checkbox ("Female")
        hombre =  st.checkbox ("Male")
        if mujer :
            sexo = 0
        else :
            sexo = 1     
                   
        educacion = st.selectbox('Level of Education',['Bachelor','Specialist','Master'])
        if educacion == 'Bachelor':
              educacion = 0
        elif educacion =='Specialist':
              educacion = 1
        elif educacion == 'Master':
              educacion = 2      
        reclutamiento = st.slider('Recruitment Source: 2.Sourcing, 1.Referred, 0.Other', 0,2,1)
        numerodeentrenamientos = st.selectbox('No of trainings completed', [0,1,2,3,4,5])
        Entrenamientos_previos = st.selectbox('Performance Score', [0,1,2,3,4,5])
        servicio = st.number_input('Lenght of Service', min_value=1, max_value=37, value=25)
        
        if st.checkbox('Have KPIS>80%? '):
            KIPs_met = 0
               
        else:
            KIPs_met = 1
                
        
        if st.checkbox('Award Won?'):
            awards_won = 0
        else:
            awards_won = 1
            
                   
        Avg_training_score = st.number_input('Average score in current training evaluations', min_value=1, max_value=100, value=25)
    
        
        region = st.number_input('Region', min_value=1, max_value=35, value=25)

        output=""
        
      #Create a List with the variables 
        input_dict = [department1 , region , educacion,  sexo, reclutamiento,  numerodeentrenamientos,  Edad,  Entrenamientos_previos,  servicio,  KIPs_met,  awards_won ,  Avg_training_score]
        
        
       #Make the prediction
        if st.button("Predictor"):
            #Import model file .PKL, 
            nombreArchivo = 'modelpredictionppe.pkl'
            modeloCargado = pickle.load(open('modelpredictionppe.pkl', 'rb'))
            prediccion = modeloCargado.predict([input_dict])
            if  prediccion == 0:
                st.write('The Employee is likely to be promoted')
            else:
                 st.write('The Employee is likely to be promoted')
                 
                 
              
    
    
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
      