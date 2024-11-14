# Core Packages
import streamlit as st 

# EDA Packages
import pandas as pd 
import numpy as np 

# Data Visualization Packages
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 

def main():
    """Automated ML App with Streamlit"""

    activities = ["EDA", "Plots"]	
    choice = st.sidebar.selectbox("Select Activities", activities)

    if choice == 'EDA':
        st.subheader("Exploratory Data Analysis")

        data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("Show Shape"):
                st.write(df.shape)

            if st.checkbox("Show Columns"):
                all_columns = df.columns.to_list()
                st.write(all_columns)

            if st.checkbox("Summary"):
                st.write(df.describe())

            if st.checkbox("Show Selected Columns"):
                selected_columns = st.multiselect("Select Columns", all_columns)
                new_df = df[selected_columns]
                st.dataframe(new_df)

            if st.checkbox("Show Value Counts"):
                st.write(df.iloc[:, -1].value_counts())

            if st.checkbox("Correlation Plot (Matplotlib)"):
                fig, ax = plt.subplots()
                cax = ax.matshow(df.corr())
                fig.colorbar(cax)
                st.pyplot(fig)

            if st.checkbox("Correlation Plot (Seaborn)"):
                fig, ax = plt.subplots()
                sns.heatmap(df.corr(), annot=True, ax=ax)
                st.pyplot(fig)

            if st.checkbox("Pie Plot"):
                all_columns = df.columns.to_list()
                column_to_plot = st.selectbox("Select 1 Column", all_columns)
                fig, ax = plt.subplots()
                df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
                st.pyplot(fig)

    elif choice == 'Plots':
        st.subheader("Data Visualization")
        data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("Show Value Counts"):
                fig, ax = plt.subplots()
                df.iloc[:, -1].value_counts().plot(kind='bar', ax=ax)
                st.pyplot(fig)
		
            # Customizable Plot
            all_columns_names = df.columns.tolist()
            type_of_plot = st.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde"])
            selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)

            if st.button("Generate Plot"):
                st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

                # Plot By Streamlit
                if type_of_plot == 'area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot == 'bar':
                    cust_data = df[selected_columns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot == 'line':
                    cust_data = df[selected_columns_names]
                    st.line_chart(cust_data)

                # Custom Plot
                elif type_of_plot:
                    fig, ax = plt.subplots()
                    df[selected_columns_names].plot(kind=type_of_plot, ax=ax)
                    st.pyplot(fig)

if __name__ == '__main__':
    main()
