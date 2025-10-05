import streamlit as st

st.set_page_config(page_title="3D Printing", page_icon="🖨️")

st.markdown("# 3D Printing")
st.sidebar.header("Enclosure design and 3D printing")

st.subheader("Enclosure Modeling")
st.markdown(
    """
    The enclosure was modeled using Autodesk Fusion 360 with enough room to accommodate the electronics and the Raspberry Pi Pico W.
    The design splits into two parts with a snap-fit connection. Slicing was done with Orca Slicer.
    """
)

st.image("images/case_bottom_fusion.png", caption="Bottom part in Fusion 360", use_container_width=True)
st.image("images/case_top_fusion.png", caption="Top part in Fusion 360", use_container_width=True)

st.image("images/case_bottom_orca.png", caption="Bottom part in OrcaSlicer", use_container_width=True)
st.image("images/case_top_orca.png", caption="Top part in OrcaSlicer", use_container_width=True)

st.markdown(
    """
    Both parts were printed on a Flashforge Adventurer 5M Pro with 0.2 mm layer height and 25% infill.
    Print time was about 40 minutes per part. PETG filament was used (black for the bottom part and green for the top part).
    """
)

st.image("images/case_open.jpg", caption="Printed and assembled enclosure with components", use_container_width=True)
st.image("images/case.jpg", caption="Final assembled version", use_container_width=True)
