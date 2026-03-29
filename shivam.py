import streamlit as st
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

st.title("Bank Queue Simulation")
st.write("Enter values and click button")
st.write("===== BANK QUEUE WITH PERFORMANCE METRICS =====")

# INPUT
customers = int(st.number_input("Enter number of customers", min_value=1))
tellers = int(st.number_input("Enter number of tellers", min_value=1))

if st.button("Run Simulation"):

    st.write("Simulation Running...")

    arrival = []
    service = []
    waiting = []
    start = []
    end = []
time = 0

# Generate arrival times
for i in range(customers):
    gap = random.randint(0,2)
    time += gap
    arrival.append(time)

# Generate service times
for i in range(customers):
    service.append(random.randint(2,6))

# Teller free time tracker
teller_time = [0]*tellers

# Simulation
for i in range(customers):

    free_teller = teller_time.index(min(teller_time))

    start_time = max(arrival[i], teller_time[free_teller])
    finish_time = start_time + service[i]

    start.append(start_time)
    end.append(finish_time)

    waiting.append(start_time - arrival[i])

    teller_time[free_teller] = finish_time

# ----------------------------
# PERFORMANCE METRICS
# ----------------------------

avg_wait = sum(waiting)/customers
avg_service = sum(service)/customers

# Approx arrival rate (λ)
total_time = arrival[-1]
lambda_rate = customers / total_time

# Approx service rate (μ)
mu = 1 / avg_service

# Utilization (ρ)
rho = lambda_rate / (tellers * mu)

# Stability check
  st.write("\nServer Utilization (ρ):", round(rho,3))
if rho < 1:
   st.write("System is STABLE")
else:
      st.write("System is UNSTABLE")

# Waiting time (Wq) and system time (W)
Wq = avg_wait
W = avg_wait + avg_service

# Approx queue length (Little’s Law)
Lq = lambda_rate * Wq
L = lambda_rate * W

  st.write("\nAverage Waiting Time (Wq):", round(Wq,2))
  st.write("Average Time in System (W):", round(W,2))
  st.write("Average number in Queue (Lq):", round(Lq,2))
  st.write("Average number in System (L):", round(L,2))

# ----------------------------
# GRAPH 1 (Customer vs Waiting)
# ----------------------------
plt.plot(range(1, customers+1), waiting, marker='o')
plt.xlabel("Customer Number")
plt.ylabel("Waiting Time")
plt.title("Customer Waiting Time Graph")
plt.grid(True)
st.pyplot(plt)

# ----------------------------
# GRAPH 2 (Arrival Rate vs Waiting Time)
# ----------------------------
arrival_rates = [lambda_rate*0.5, lambda_rate*0.75, lambda_rate]
waiting_rates = [Wq*0.5, Wq*0.8, Wq]

plt.plot(arrival_rates, waiting_rates, marker='o')
plt.xlabel("Arrival Rate (λ)")
plt.ylabel("Average Waiting Time")
plt.title("Arrival Rate vs Waiting Time")
plt.grid(True)
st.pyplot(plt)



