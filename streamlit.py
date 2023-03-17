import streamlit as st
import pandas as pd
import pickle
import numpy as np


pickled_model = pickle.load(open('modeltfm.pkl', 'rb'))


def predict(pickled_model, input_df):
    predictions_df = pickled_model.predict(estimator=pickled_model.predict, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('hrana.png')
    image_hranalitycs = Image.open('hrana.jpg')

    st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "Como te gustaria predecir?",
    ("Online", "Batch"))

    st.sidebar.info('Esta aplicacion es creada para predecir al personal que será promovido')
    st.sidebar.success('https://www.pycaret.org')
    
    st.sidebar.image(image_hranalitycs)

    st.title("Promoción efectiva app")

    if add_selectbox == 'Online':
        
        Departament = st.selectbox('departament', ['Analytics', 'Finance','HR', 'Legal', 'Operations', 'Procurement', 'R&D'])
        Edad = st.number_input('age', min_value=1, max_value=100, value=25)
        sexo = st.selectbox('gender', ['male', 'female'])
        educacion = st.selectbox('education', ['Bachelors', 'Below Secundary','Masters y Above'])
        reclutamiento = st.selectbox('recruitment_channel', ['referido', 'red','otro medio'])
        numerodeentrenamientos = st.selectbox('no_of_trainings', [0,1,2,3,4,5])
        Entrenamientos_previos = st.selectbox('previous_year_rating', [0,1,2,3,4,5])
        servicio = st.number_input('Servicio', min_value=1, max_value=37, value=25)
        if st.checkbox('Kipsaprobado'):
            KIPs_met = 'yes'
        else:
            KIPs_met = 'no'
        
        if st.checkbox('Ganópremio'):
            awards_won = 'yes'
        else:
            awards_won = 'no'
                   
        Avg_training_score = st.number_input('avg_training_score', min_value=1, max_value=100, value=25)
    
        
        region = st.number_input('region', min_value=1, max_value=34, value=25)

        output=""

        input_dict = {'departament' : Departament ,'region' : region , 'education' : educacion, 'gender' : sexo, 'recruitment_chanel' : reclutamiento, 'no_of_trainings' : numerodeentrenamientos, 'age' : Edad, 'previous_year_raiting': Entrenamientos_previos, 'length_of_service': servicio, 'KPIs_met>80%': KIPs_met, 'awards_won?' : awards_won , 'avg_training_score' : Avg_training_score}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=pickled_model.predict, input_df=input_df)
            output = '$' + str(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = pickled_model.predict(estimator=pickled_model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()
