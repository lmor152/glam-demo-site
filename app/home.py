import streamlit as st
from wrapper import Wrapper

st.set_page_config(
    page_title="GLAM Demo",
    page_icon="🗺️",
    layout="wide",
)

intro = """
I created GLAM (Geocoding via LINZ Address Matching) to help with geocoding New Zealand addresses.

GLAM is a tool for ***free, offline*** geocoding. It works by matching addresses to Land Information New Zealand data, so it only works with residential addresses. 

GLAM includes multiple methods for parsing and matching messy unstructured addresses. Find out more here: https://github.com/lmor152/glam 
"""

with st.sidebar:
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.image("glam.svg")
    st.divider()
    st.write(intro)

    st.markdown("**GLAM Settings**")
    st.write(
        "At this time, this demo site only supports the RNN-based parser, and the TF-IDF matcher."
    )

    st.divider()

st.title("GLAM Demo")

st.markdown(
    """
GLAM is designed to handle messy addresses, this includes building names, levels, abbreviations, and typos. 

Test it out by entering an address, and seeing how it parses the address components and finds the best match in the LINZ database.
"""
)

address = st.text_input(
    "Enter an address to test:", "Level three, KPMG, 18 viaduct harbour ave, 1010"
)

c1, c2 = st.columns(2)

with c1:
    st.write("Your address was parsed into:")
    st.table(Wrapper.parse_address(address))

with c2:
    match, conf = Wrapper.match_address(address)
    st.write(f"Best match found (confidence = {conf * 100:.2f}%):")
    st.table(match)

search = st.text_input(
    "You can ***exact*** search against the LINZ database to find your address here too:",
    "18 Viaduct Harbour Avenue, Auckland",
)
st.dataframe(Wrapper.search_address(search))
