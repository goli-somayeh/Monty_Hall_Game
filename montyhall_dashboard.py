import streamlit as st
from src.montyhall_project import simulate
import time

st.title("Monty Hall Game Simulation")
st.image("https://mathematicalmysteries.org/wp-content/uploads/2021/12/04615-0sxvwbnzvvnhuklug.png", width=400)

num_of_games = st.number_input("Please Enter Number of Games to Simulate:", min_value=1, max_value=10000, value=100)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_no_switching = 0
wins_with_switching = 0
for i in range(num_of_games):
    num_wins_without_switching , num_wins_with_switching = simulate(1)
    wins_no_switching += num_wins_without_switching
    wins_with_switching += num_wins_with_switching

    chart1.add_rows([wins_no_switching / (i + 1)])
    chart2.add_rows([wins_with_switching / (i + 1)])

    time.sleep(0.01)



