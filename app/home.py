import streamlit as st


def parse_address(address):
    split = address.split(" ")
    return {
        "street": split[0].strip(),
        "city": split[1].strip(),
        "postcode": split[2].strip(),
    }


st.set_page_config(
    page_title="GLAM Demo",
    page_icon="🗺️",
    layout="wide",
)

intro = """
I created GLAM (Geocoding Via LINZ Address Matching) to help with geocoding New Zealand addresses.

GLAM is a tool for free offline geocoding. It works by matching addresses to Land Information New Zealand data, so it only works with residential addresses. 

GLAM supports a few different algorithms for performing the matching, you can test them out below!
"""

with st.sidebar:
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.image("glam.svg")
    st.divider()
    st.write(intro)

    st.markdown("**GLAM Settings**")
    matcher = st.segmented_control(
        "Matching Algorithm:", ["Fuzzy", "Vector", "Hybrid", "TF-IDF"]
    )

    if matcher in ("Vector", "Hybrid", "Fuzzy"):
        parser = st.segmented_control("Parsing Algorithm:", ["libpostal", "RNN"])
    else:
        st.caption("Parser not required for selected matching algorithm.")
        parser = None

    st.divider()

    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        load_button = st.button("Load Geocoder")
        if load_button:
            st.balloons()

st.title("GLAM Demo")

address = st.text_input(
    "Enter an address to geocode:", "18 Viaduct Harbour Avenue, Auckland, 1010"
)

c1, c2 = st.columns(2)

with c1:
    st.write("Your address was parsed into:")
    st.table(parse_address(address))

with c2:
    st.write("Best match found:")
    st.table(parse_address(address))

st.text_input(
    "You can exact search against the LINZ database to find your address here too:",
    "18 Viaduct Harbour Avenue, Auckland, 1010",
)
st.dataframe()
