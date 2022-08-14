import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import warnings
# import potash

st.set_page_config(page_title="Crop Recommendation", page_icon="🌿",
                   layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

val_N = 0
val_moist =0  #potash.op

header = st.container()
results = st.container()
predictions_input = st.container()
predictions_output = st.container()
crop_dataset = st.container()

def main():

    # title

    with header:
        st.title('Crop Recommendation System🌾')
        with st.expander(" ℹ️  Information", expanded=True):
            st.text("""Crop recommendation is one of the most important aspects of precision 
agriculture. Crop recommendations are based on a number of factors. 
Precision agriculture seeks to define these criteria on a site-by-site 
basis in order to address crop selection issues. While the "site-specific"
methodology has improved performance, there is still a need to monitor the
systems outcomes.Precision agriculture systems are not all created equal.
However, in agriculture, it is critical that the recommendations made are
correct and precise, as errors can result in significant material and 
capital loss.""")

    # with results:
    #     st.header('**Our Conclusions✍️**')
    #     st.caption('**These are our conclusions based on the Hardware Soil tests.**')

    #     sel_col, disp_col = st.columns(2)
    #     sel_col.metric('Nitrogen: ', val_N, delta='40 ppm',
    #                 delta_color="normal")
    #     disp_col.metric('Phosphorus: ', val_N,
    #                     delta='25 to 50 ppm', delta_color="normal")
    #     sel_col.metric('Potassium: ', val_N,
    #                 delta='40 to 80 ppm', delta_color="normal")
    #     disp_col.metric('Moisture: ', val_N,
    #                 delta='0-100%', delta_color="normal")
    #     sel_col.metric('Tempreture: ', val_N,
    #                 delta=' degree C', delta_color="normal")
        

    with predictions_input:
        st.header('**Check for Your Soil!👨‍🌾**')
        st.caption(
            '**Enter correct values for given parameters to achieve maximum accuracy.**')
        N = st.number_input('Nitrogen Content', min_value=0,
                            max_value=200, value=35, step=1, disabled=False)
        P = st.number_input('Phosphorus Content', min_value=0,
                            max_value=200, value=25, step=1, disabled=False)
        K = st.number_input('Potassium Content', min_value=0,
                            max_value=200, value=25, step=1, disabled=False)
        rainfall = st.number_input(
            'Rainfall(in mm)', min_value=0, max_value=200, value=25, step=1, disabled=False)
        temp = st.number_input('Tempreture', min_value=0,
                            max_value=200, value=25, step=1, disabled=False)
        humidity = st.number_input(
            'Humidity', min_value=0, max_value=200, value=25, step=1,   disabled=False)
        ph = st.number_input(
            'pH of soil', min_value=0.00, max_value=1.00,disabled=False)
        predict = st.button('Predict')

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        with predictions_output:
            st.header('**Our Predictions:bar_chart:**')
            st.text('Based on values entered, the best crop recommendation is...')

            if predict:

                    loaded_model = load_model('model.pkl')
                    prediction = loaded_model.predict(single_pred)
                    predictions_output.success(f"{prediction.item().title()} are recommended by the A.I for your farm.")
            #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

    

    with crop_dataset:
        st.header('Dataset Used:chart_with_upwards_trend:')
        crop_data = pd.read_csv('Data/Crop_recommendation.csv')
        st.write(crop_data.head(50))

        st.header('Nitrogen')
        N_dist = pd.DataFrame(crop_data['N'].value_counts()).head(50)
        st.bar_chart(N_dist)

        st.header('Phosphorus')
        P_dist = pd.DataFrame(crop_data['P'].value_counts()).head(50)
        st.bar_chart(P_dist)

        st.header('Potassium')
        K_dist = pd.DataFrame(crop_data['K'].value_counts()).head(50)
        st.bar_chart(K_dist)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()

