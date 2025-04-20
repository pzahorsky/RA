import streamlit as st
import pandas as pd
import numpy as np
from data_loader import load_data 
from data_filtering import Dynamic_filtering

dynamic_filter = Dynamic_filtering()

st.title("Dynamic filtering with Pandas - regex")

uploaded_files = st.sidebar.file_uploader("Upload a CSV file", type='csv',accept_multiple_files=True)

dFs = {}

for dataFrame in uploaded_files:
    
    # Data Loader & Raw Data Viewer
    st.write(f"Uploading file: {dataFrame.name}") 
    dFs[f"{dataFrame.name}"] = load_data(dataFrame)
    st.dataframe(dFs[f"{dataFrame.name}"])

# First Level Data Filtering - Filter specific Columns
    filtered_dF_sv = dynamic_filter.sample_value_filter(dFs[f"{dataFrame.name}"])
    filtered_dF_sb = dynamic_filter.sub_board_filter(dFs[f"{dataFrame.name}"])
    filtered_dF_cp = dynamic_filter.component_filter(dFs[f"{dataFrame.name}"])

# Sidebar - Dynamic filter



if uploaded_files:
    
    if "show_component_selectbox" not in st.session_state:
        st.session_state.show_component_selectbox = False
    
    if "show_alg_selectbox" not in st.session_state:
        st.session_state.show_alg_selectbox = False

    if "show_sample_name_selectbox" not in st.session_state:
        st.session_state.show_sample_name_selectbox = False
    
    # Pop-up callbacks
    def show_component_selectbox():
        st.session_state.show_component_selectbox = True

    def show_algorithm_selectbox():
        st.session_state.show_alg_selectbox = True

    def show_sample_name_selectbox():
        st.session_state.show_sample_name_selectbox = True
    
    if np.size(dynamic_filter.sub_board_filter(dFs[f"{dataFrame.name]) == 
    sub_board_sidebar = st.sidebar.selectbox("Select Sub-Board", dynamic_filter.sub_board_filter(dFs[f"{dataFrame.name}"]),
                                             key="sub_board_selection", on_change=show_component_selectbox)
    
    # Component selectbox pop-up event
    if st.session_state.show_component_selectbox:
        comp_sidebar = st.sidebar.selectbox("Select Component", dynamic_filter.component_filter(dFs[f"{dataFrame.name}"]),
                                            key="comp_selection", on_change=show_algorithm_selectbox)
    
    # Algorithm selectbox pop-up event
    if st.session_state.show_alg_selectbox:
        alg_sidebar = st.sidebar.selectbox("Select Algorithm", dynamic_filter.algortihm_filter(dFs[f"{dataFrame.name}"]),
                                           key="sample_name_selection", on_change=show_sample_name_selectbox)

    # Sample Name selectbox pop-up event
    if st.session_state.show_sample_name_selectbox:
        sample_name_sidebar = st.sidebar.selectbox("Select Sample Name", dynamic_filter.sample_name_filter(dFs[f"{dataFrame.name}"]))

else:
    st.session_state.show_component_selectbox = False
    st.session_state.show_alg_selectbox = False
    st.session_state.show_sample_name_selectbox = False
    


    







