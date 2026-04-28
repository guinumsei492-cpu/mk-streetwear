import streamlit as st
import streamlit.components.v1 as components

# 1. Configuração da Página (Aba do Navegador)
st.set_page_config(
    page_title="MK // OFFICIAL", 
    page_icon="🕶️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Estilo Customizado (CSS) - Foco no visual "Clean/Dark"
st.markdown("""
    <style>
    /* Fundo total preto */
    .stApp {
        background-color: #000000;
    }
    /* Esconder elementos desnecessários do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilo do Título MK */
    .mk-logo {
        font-family: 'Inter', sans-serif;
        color: white;
        text-align: center;
        font-size: 80px;
        font-weight: 900;
        letter-spacing: -5px;
        margin-top: -40px;
        margin-bottom: 10px;
    }
    
    .mk-subtitle {
        color: #555;
        text-align: center;
        font-family: 'monospace';
        letter-spacing: 2px;
        margin-bottom: 50px;
    }

    /* Estilização dos Botões */
    div.stButton > button {
        background-color: transparent;
        color: white;
        border: 1px solid white;
        border-radius: 0px;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: white;
        color: black;
        border: 1px solid white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="mk-logo">MK</div>', unsafe_allow_html=True)
    st.markdown('<div class="mk-subtitle">FUTURE STREETWEAR // COLLECTION 01</div>', unsafe_allow_html=True)

    # 3. Área do Modelo 3D (Usando Spline para performance)
    # Este link é um exemplo de um tênis 3D interativo. 
    # Depois você pode criar o seu no spline.design e trocar o link!
    render_3d = """
    <div style="display: flex; justify-content: center;">
        <iframe src='https://my.spline.design/sneaker-3551571d782169600a08e1a90d40214c/' 
        frameborder='0' width='100%' height='600px'></iframe>
    </div>
    """
    components.html(render_3d, height=600)

    st.markdown("<p style='text-align: center; color: #444; font-size: 12px;'>Gire o modelo com o mouse</p>", unsafe_allow_html=True)

    # 4. Seção de Compra
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("<h4 style='color: white; text-align: center;'>MK CYBER HOODIE v1</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #888; text-align: center;'>Preto fosco | Algodão 400g</p>", unsafe_allow_html=True)
        
        tamanho = st.select_slider(
            "Selecione o tamanho",
            options=["P", "M", "G", "GG"]
        )
        
        if st.button("ADICIONAR AO DROP"):
            st.toast(f"Item {tamanho} reservado para você.", icon="🔥")

if __name__ == "__main__":
    main()
