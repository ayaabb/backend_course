import altair as alt
import pandas as pd
import streamlit as st


def plot_barChart(values, names,week_number):  # plotting the danger index for each asteroid
    values_names = pd.DataFrame({'names': names, 'danger index': values})

    st.bar_chart(values_names.set_index('names'))
    st.title(f"Week{week_number}")
    st.pyplot()


def plot_graph(asteroids, X_key, Y_key,week_number):  # plotting the relation between two factors
    x = [ast[X_key] for ast in asteroids]
    y = [ast[Y_key] for ast in asteroids]
    df = pd.DataFrame({X_key: x, Y_key: y})

    chart = alt.Chart(df).mark_circle().encode(x=X_key, y=Y_key, tooltip=[X_key, Y_key]).interactive()
    st.title(f"Week{week_number}")
    st.write(chart)
