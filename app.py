st.sidebar.header("Input Pollutant Values")

PM25 = st.sidebar.number_input("PM2.5", min_value=0.0, value=50.0)
PM10 = st.sidebar.number_input("PM10", min_value=0.0, value=100.0)
NO2  = st.sidebar.number_input("NO2", min_value=0.0, value=40.0)
CO   = st.sidebar.number_input("CO", min_value=0.0, value=1.0)
SO2  = st.sidebar.number_input("SO2", min_value=0.0, value=10.0)
O3   = st.sidebar.number_input("O3", min_value=0.0, value=30.0)
