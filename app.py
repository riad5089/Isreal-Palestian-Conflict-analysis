import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("Upload Dataset")
upload_file = st.sidebar.file_uploader("Choose a file", type=['csv', 'xlsx'])

if upload_file is not None:
    df=pd.read_csv(upload_file)
    no_event=len(df)

    # sidebar code
    citizenship_counts = df['citizenship'].value_counts()
    event_location_region_counts = df['event_location_region'].value_counts()
    hostilities_counts = df[df['took_part_in_the_hostilities'] == 'Yes']['citizenship'].value_counts()
    no_hostilities_counts = df[df['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()

    st.sidebar.write("No Of Event :", no_event)

    col1,col2=st.sidebar.columns(2)
    col3,col4 = st.sidebar.columns(2)

    with col1:
        st.subheader("Citizenship")
        st.write(citizenship_counts)

    with col2:
        st.subheader("Event Location Region")
        st.write(event_location_region_counts)

    with col3:
        st.subheader("hostilities")
        st.write(hostilities_counts)
    with col4:
        st.subheader('no hostilities')
        st.write(no_hostilities_counts)

    weapons_counts=df['ammunition'].value_counts()
    st.sidebar.write('Weapon Counts',weapons_counts)

    # Data analysis part
    st.title("Isreal Palestine Conflict Analysis")
    st.write('Dataset Sample',df)

    col1,col2 = st.columns(2)
    with col1:
        st.subheader("types of injuries")
        type_of_injury=df['type_of_injury'].value_counts()
        st.bar_chart(type_of_injury)

    with col2:
        st.subheader('Gender Counts')
        Gcounts=df['gender'].value_counts()
        st.bar_chart(Gcounts)
        # st.bar_chart(Gcounts)

    col1,col2=st.columns(2)
    with col1:
        st.subheader("Age Summary")
        age=df.age.describe()
        st.write(age)
    with col2:
        st.subheader("Even Location Region Count")

    #visuallize the types of injuries
    st.subheader("Types of Injuries")
    injury_counts=df['type_of_injury']
    fig,ax=plt.subplots()