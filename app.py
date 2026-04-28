import streamlit as st
import streamlit.components.v1 as components

# Configuração da página - Nome da aba agora é MK
st.set_page_config(page_title="MK // OFFICIAL", layout="wide")

# CSS Customizado: Fundo preto, fontes brancas e detalhes em neon
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    header {visibility: hidden;}
    .main-title {
        text-align: center; 
        color: white; 
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        letter-spacing: 5px;
        font-size: 50px;
        margin-top: -50px;
    }
    .subtitle {
        text-align: center;
        color: #444;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Header da Marca MK
    st.markdown("<h1 class='main-title'>MK</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>FUTURE STREETWEAR // DROP 01</p>", unsafe_allow_html=True)

    # Visualizador 3D (Substitua o link do iframe pelo seu modelo do Spline quando tiver)
    st.markdown("""
        <div style="display: flex; justify-content: center;">
            <iframe src='https://my.spline.design/sneaker-3551571d782169600a08e1a90d40214c/' 
            frameborder='0' width='100%' height='600px'></iframe>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; color: #00ff00; font-family: monospace;'>[ INTERATIVO: GIRE O MODELO ]</p>", unsafe_allow_html=True)

    # Interface de Compra
    st.write("---")
    col1, col2, col3 = st.columns([1,1,1])
    
    with col2:
        st.markdown("<h3 style='text-align: center; color: white;'>DROP #001: MK CYBER HOODIE</h3>", unsafe_allow_html=True)
        tamanho = st.selectbox("SELECIONE O TAMANHO", ["P", "M", "G", "GG"])
        if st.button("ADICIONAR AO CARRINHO", use_container_width=True):
            st.success(f"MK HOODIE ({tamanho}) ADICIONADO.")

if __name__ == "__main__":
    main()
