import urllib
import re
from bs4 import BeautifulSoup
import streamlit as st

st.set_page_config(page_title="My Website", page_icon=":tada", layout="wide")
st.subheader("Sensor 4")

st.write("Sensor 4 in the basememt tunnel, close to access control has detetected humidity levels lower than the threshold of 0%")
