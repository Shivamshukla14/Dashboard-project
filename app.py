import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#Setting page config
st.set_page_config(page_title = "Dashboard",
                   page_icon = ":bar_chart:",
                   layout = "wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
#st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#Laoding dataset
df = pd.read_csv("most_runs_in_cricket.csv")

#Setting up sidebar\
st.sidebar.subheader(":large_blue_diamond: Navigate")
option = st.sidebar.radio("",options=["Home","Overview","Performance", "Compare"])

#Data for KPI
average_matches = round(df['Mat'].mean())
players = df['Player'].count()
average_sr = df['SR'].mean()
average_a = df['Ave'].mean()


#Home Layout
if option == "Home":
    st.title(":globe_with_meridians: TOP PLAYERS IN THE WORLD CRICKET ")
    st.image("cricketer.jpg",width = 850)
    l_container, m_container,r_container = st.columns(3)
    l_container.markdown("")
    m_container.subheader("About this file")
    r_container.markdown("")
    st.markdown("This dataset contain the Most Runs in International cricket in (ODI, Test , T20) and the all information about the batsman like 4's ,6's, 100's and other information of the batsman.")
    left_container, right_container = st.columns(2)
    with left_container:
        st.markdown("""
        Player:- Player Name <br><br>
        Country:- Player's country <br><br>
        Span :- Total time period <br><br>
        Mat :- Total Matches played by player <br><br>
        Inns :- Total innings <br><br>
        NO :- Total Not out <br><br>
        Runs :- Total runs <br><br>
        HS :- Highest Run in a innings <br><br>
        Ave :- Average of batting <br><br>
        BF :- Total Ball faced <br><br>
        """,True)
    
    with right_container:
        if st.checkbox("Show Data set", value = True):
            st.dataframe(df, height = 470, width = 500)

#Overview Layout
if option == "Overview":
    #KPI Sub headers
    first_h, second_h = st.columns(2)
    first_h.subheader(":beginner: Players")
    second_h.subheader(":beginner: Average")

    #KPI's
    KPI1, KPI2, KPI3, KPI4 = st.columns(4)
    KPI1.metric(label = "Count", value = int(players), delta = None)
    KPI2.metric(label = "Matches", value = str(average_matches) + "+", delta = None)
    KPI3.metric(label = "Strike Rate", value = ("%.2f" % average_sr), delta = None)
    KPI4.metric(label = "Average", value = ("%.2f" % average_a), delta = None)

    st.markdown("----")

    #Creating layout for pie chart
    input_col, pie_col = st.columns(2)
    with input_col:
        st.subheader(":beginner: Run  Machines")
        #Bar Chart
        bar_data = df[["Player","Runs"]].head(10)
        bar_data = bar_data.set_index("Player")
        bar_fig = st.bar_chart(bar_data, height=450)

    with pie_col:
        st.subheader(":beginner: Runs Scored(Country wise)")
        #Creating pie chart
        pie_data = df[["Country","Runs"]]
        pie_data.reset_index()
        fig = px.pie(pie_data, values='Runs', names='Country')
        fig.update_layout(showlegend = False,
        margin = dict(l=1,t=1,b=1,r=1),
        width = 400,
        height = 400)
        st.write(fig)

    st.markdown("----")

    left_sh, middle_sh,right_sh = st.columns(3)
    left_sh.markdown("")
    middle_sh.subheader(":beginner: Top 5 Batsman")
    right_sh.markdown("")
    #Dataframe for top 5 Batsman
    bat_5 = df[["Player","Country","Mat","SR","Ave"]].head(5)
    bat_5.columns = ["Name","Country","Matches Played","Strike Rate","Average"]   
    bat_5.index += 1 #to start index from 1
    st.table(bat_5)

#Performance Layout
if option == "Performance":
    val = st.selectbox("Select the Country: ",options = df["Country"].unique())
    #dataframe
    df_selection = df.query("Country == @val")

    #Definig KPI's values
    count_layout = df_selection["Country"].count()
    match_layout = df_selection["Mat"].sum()
    sr_layout = df_selection["SR"].mean()
    avr_layout = df_selection["Ave"].mean()

    l_cont, m_cont,r_cont = st.columns(3)
    l_cont.markdown("")
    m_cont.subheader(":beginner: Stats")
    r_cont.markdown("")

    #defining layout
    col_1, col_2, col_3, col_4 = st.columns(4)
    col_1.metric(label = "Players", value = count_layout, delta = None)
    col_2.metric(label = "Matches", value = match_layout, delta = None)
    col_3.metric(label = "Strike Rate", value = ('% .2f' % sr_layout), delta = None)
    col_4.metric(label = "Average", value = ('% .2f' % avr_layout), delta = None)

    st.markdown("----")

    #Layout for graph
    left_graph, right_graph = st.columns(2)
    #left side
    with left_graph:
        st.subheader(":beginner: Contribution")
        #horizontal bar chart
        fig_top_contributers = px.bar(
            df_selection,
            x = "Runs",
            y = "Player",
            title = "In Ascending order(Run wise)",
            orientation = "h",
            template = "plotly_white"
        )
        fig_top_contributers.update_layout(width=600, height = 450)
        st.plotly_chart(fig_top_contributers)
    #right side
    with right_graph:
        st.subheader(":beginner: Innings v/s Runs")
        fig = px.scatter(df_selection, x = "Inns", y = "Runs", size = "Runs", color = "Player", hover_name = "Player",
        log_x=True, size_max = 20,title="Contry wise")
        fig.update_layout(width = 600, height = 450)
        st.write(fig)

    st.markdown("----")

    #Top Scorers
    st.subheader(":beginner: Top Scorers")
    #table
    tc_data = df_selection[["Player","Mat","Runs","HS","SR"]].head(5)
    tc_data.columns = ["Name","Matches Played","Runs","High Score","Strike Rate"]   
    tc_data.index = [i for i in range(1,len(tc_data["Name"])+1)] #to start index from 1
    st.table(tc_data)

#Compare Layout
if option == "Compare":
    left_cn ,mid_cn ,right_cn = st.columns(3)
    left_cn.markdown("")
    mid_cn.subheader(":beginner: Comparison")
    right_cn.markdown("")

    #1st row
    left_side, right_side = st.columns(2)
    #Player 1
    with left_side:
        cols1 = st.selectbox(label = "Select Player 1",options = df["Player"].unique())
        # df_sel1 = df.query("Player == @cols1")
        df_sel1 = df[df["Player"] == cols1]
    #Player 2
    with right_side:
        cols2 = st.selectbox(label = "Select Player 2", options = df["Player"].unique(),index=1)
        df_sel2 = df.query("Player == @cols2")

    #defining KPI's for both side
    #left side
    left_match = df_sel1["Mat"]
    left_runs = df_sel1["Runs"]
    left_HS = df_sel1["HS"]
    left_SR = df_sel1["SR"]
    left_100 = df_sel1["100"]
    left_50 = df_sel1["50"]
    left_country = df_sel1["Country"].to_list()[0]
    #right side
    right_match = df_sel2["Mat"]
    right_runs = df_sel2["Runs"]
    right_HS = df_sel2["HS"]
    right_SR = df_sel2["SR"]
    right_100 = df_sel2["100"]
    right_50 = df_sel2["50"]
    Right_country = df_sel2["Country"].to_list()[0]

    #Second row
    #layout
    left_c, right_c = st.columns(2)
    left_c.markdown(left_country)
    right_c.markdown(Right_country)

    #Third row
    left_KPI1, left_KPI2, right_KPI1, right_KPI2 = st.columns(4)
    left_KPI1.metric(label = "Matches", value = left_match, delta = None)
    left_KPI2.metric(label = "Runs", value = left_runs, delta = None)
    right_KPI1.metric(label = "Matches", value = right_match, delta = None)
    right_KPI2.metric(label = "Runs", value = right_runs, delta = None)

    #Fourth row
    L_KPI1, L_KPI2, R_KPI1, R_KPI2 = st.columns(4)
    L_KPI1.metric(label = "High Score", value = left_HS, delta = None)
    L_KPI2.metric(label = "Strike Rate", value = left_SR, delta = None)
    R_KPI1.metric(label = "High Score", value = right_HS, delta = None)
    R_KPI2.metric(label = "Strike Rate", value = right_SR, delta = None)

    #Fifth row
    L1_KPI1, L1_KPI2, R1_KPI1, R1_KPI2 = st.columns(4)
    L1_KPI1.metric(label = "100s", value = left_100, delta = None)
    L1_KPI2.metric(label = "50s", value = left_50, delta = None)
    R1_KPI1.metric(label = "100s", value = right_100, delta = None)
    R1_KPI2.metric(label = "50s", value = right_50, delta = None)

    st.markdown("----")
    #Comparison Bar chart
    CB_data = df_sel1
    if cols1 != cols2:
        CB_data = pd.concat([df_sel1, df_sel2])
    fig = px.bar(CB_data, x="Player", y=["Mat", "HS", "100", "50"], barmode='group', title = "Comparison Bar Chart")
    fig.update_layout(width = 900, height = 450)
    st.plotly_chart(fig)

