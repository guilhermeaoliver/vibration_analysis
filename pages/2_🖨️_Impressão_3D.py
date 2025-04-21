import streamlit as st

st.set_page_config(page_title="Impressão 3D", page_icon="🖨️")

st.markdown("# Impressão 3D")
st.sidebar.header("Desenho e impressão da case do protótipo")

st.subheader("Modelagem da Case")
st.markdown(
    """
    O desenho da case foi realizado utilizando o software CAD Autodesk Fusion, levando em consideração o espaço necessário para acomodar os componentes eletrônicos e a Raspberry Pi Pico W de forma funcional.
    """
)

st.image("images/case_bottom_fusion.png", caption="Parte inferior da case no Fusion 360", use_container_width=True)
st.image("images/case_top_fusion.png", caption="Parte superior da case no Fusion 360", use_container_width=True)

st.markdown(
    """
    A case foi projetada para ser impressa em 3D, em duas partes, com encaixe rápido (*snap fit*) entre elas. O software utilizado para fatiamento foi o Orca Slicer.
    """
)

st.image("images/case_bottom_orca.png", caption="Parte inferior da case no OrcaSlicer", use_container_width=True)
st.image("images/case_top_orca.png", caption="Parte superior da case no OrcaSlicer", use_container_width=True)

st.markdown(
    """
    As duas partes foram impressas em uma Flashforge Adventurer 5M Pro, com uma resolução de 0.2 mm e preenchimento de 25%.
    O tempo total de impressão foi de aproximadamente 40 minutos para cada parte.
    O material escolhido para a impressão foi o PETG Voolt nas cores preto, para a parte inferior, e verde, para a parte superior..
    """
)

st.image("images/case_open.jpg", caption="Case impressa e montada com os componentes", use_container_width=True)
st.image("images/case.jpg", caption="Versão final da montagem", use_container_width=True)
