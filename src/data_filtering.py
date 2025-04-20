import pandas as pd
import streamlit as st
import numpy as np

class Dynamic_filtering:
    def __init__(self):
        # Inicialize the class with default values
        self.df = None

    def sample_value_filter(self, df):

        sample_values = df.filter(regex=r"^Sample Value\s\d+$")

        if not sample_values.empty:
            return sample_values
        else:
            return None
        
    def sub_board_filter(self,df):

        sub_boards = df.filter(regex=r"^Sub-board\s*$")
        unique_sub_boards = sub_boards["Sub-board"].unique()
        st.write(np.size(unique_sub_boards))

        return unique_sub_boards
        
    def component_filter(self,df):

        components = df.filter(regex=r"^Component\s*$")
        unique_values = components["Component"].unique()

        return unique_values
    
    def algortihm_filter(self,df):

        algorithms = df.filter(regex=r"^Algorithm Name$")
        unique_algorithms = algorithms['Algorithm Name'].unique()
        
        return unique_algorithms
    
    def sample_name_filter(self,df):

        sample_name = df.filter(regex=r"^Sample Name$")
        unique_sample_name = sample_name['Sample Name'].unique()

        return unique_sample_name
