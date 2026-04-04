import streamlit as st
import random
import matplotlib.pyplot as plt

random.seed(1)

st.title("🏦 Bank Teller System Simulation")

# ----------------------------
# OVERVIEW
# ----------------------------
st.subheader("Project Overview")
st.write("""
This project simulates a bank teller queuing system.
Customers arrive randomly and require service.
Each teller serves one customer at a time.
If all tellers are busy, customers must wait.
The system calculates waiting and service time.
It helps analyze efficiency and congestion.
Graphs visualize customer waiting behavior.
Useful for real-world queue management.
""")

# ----------------------------
# INPUT
# ----------------------------
customers = st.number_input("Enter number of customers:", min_value=1, value=10)
tellers = st.number_input("Enter number of tellers:", min_value=1, value=2)

if st.button("Run Simulation"):

    arrival = []
    service = []

    time = 0

    # ARRIVAL
    for i in range(customers):
        gap = random.randint(0, 2)
        time += gap
        arrival.append(time)

    # SERVICE
    for i in range(customers):
        service.append(random.randint(2, 6))

    # SIMULATION
    waiting = []
    start = []
    end = []

    teller_time = [0] * tellers

    for i in range(customers):
        free_teller = teller_time.index(min(teller_time))

        start_time = max(arrival[i], teller_time[free_teller])
        finish_time = start_time + service[i]

        start.append(start_time)
        end.append(finish_time)

        waiting.append(start_time - arrival[i])

        teller_time[free_teller] = finish_time

    # RESULTS
    avg_wait = sum(waiting) / customers
    avg_service = sum(service) / customers
    Ws = avg_wait + avg_service

    st.subheader("Results")
    st.write(f"Average Waiting Time (Wq): {round(avg_wait, 2)}")
    st.write(f"Average Service Time: {round(avg_service, 2)}")
    st.write(f"Average Time in System (Ws): {round(Ws, 2)}")

    # GRAPH
    st.subheader("Waiting Time Graph")
    fig, ax = plt.subplots()
    ax.plot(range(1, customers+1), waiting, marker='o')
    ax.set_xlabel("Customer Number")
    ax.set_ylabel("Waiting Time")
    ax.set_title("Customer Waiting Time")
    ax.grid(True)

    st.pyplot(fig)

    # GRAPH EXPLANATION
    st.subheader("Graph Explanation")
    st.write("""
    The graph shows customer number on the X-axis and waiting time on the Y-axis.
    As the number of customers increases, waiting time may increase due to queue formation.
    An upward trend indicates congestion, while a flat trend indicates an efficient system.
    """)