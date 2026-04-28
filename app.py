import streamlit as st

# Configuração da página - Vibe de Academia/Luta
st.set_page_config(page_title="MK MUAY THAI // ACADEMY", page_icon="🥊", layout="wide")

# CSS para um visual "Fight Club" (Preto, Vermelho e Branco)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .main-title {
        font-family: 'Oswald', sans-serif;
        color: #ff0000;
        text-align: center;
        font-size: 60px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 0px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #111;
        border-radius: 5px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff0000 !important;
    }
    .combo-box {
        padding: 20px;
        border-left: 5px solid #ff0000;
        background-color: #111;
        margin: 10px 0px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-title">MK MUAY THAI</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>A ARTE DAS 8 ARMAS // DO ZERO AO ELITE</p>", unsafe_allow_html=True)
    st.write("---")

    # Sistema de abas para organizar "TUDO"
    tab1, tab2, tab3, tab4 = st.tabs(["🥊 FUNDAMENTOS", "🔥 COMBOS", "🛡️ DEFESA", "🏋️ TREINO"])

    with tab1:
        st.header("Os Pilares")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Base e Postura")
            st.write("- Pés na largura dos ombros\n- Calcanhar de trás levemente suspenso\n- Mãos na altura da sobrancelha")
        with col2:
            st.subheader("Golpes Retos")
            st.write("- Jab (Mão da frente)\n- Direto (Mão de trás com rotação de quadril)")
            
    with tab2:
        st.header("Combinações de Ataque")
        st.markdown('<div class="combo-box"><b>NÍVEL 01:</b> Jab + Direto + Chute Circular Baixo (Low Kick)</div>', unsafe_allow_html=True)
        st.markdown('<div class="combo-box"><b>NÍVEL 02:</b> Direto + Cruzado + Joelhada (Knee)</div>', unsafe_allow_html=True)
        st.markdown('<div class="combo-box"><b>CLINCH:</b> Controle de nuca + Cotovelada ascendente</div>', unsafe_allow_html=True)

    with tab3:
        st.header("Não seja atingido")
        st.write("### Bloqueios")
        st.info("O bloqueio do chute deve ser feito com a canela (tíbia), nunca com a coxa!")
        st.write("### Esquivas")
        st.write("- Pendulo lateral para evitar diretos\n- 'Lean back' para evitar chutes na cabeça")

    with tab4:
        st.header("Gerador de Round (MK Coach)")
        if st.button("GERAR ROUND ALEATÓRIO"):
            combos = ["30 Sg de Sombra", "50 Chutes Médios", "2 Minutos de Clinch", "10 Sprawls + Cruzados"]
            import random
            st.warning(f"Seu foco agora: {random.choice(combos)}!")

    # Rodapé Motivacional
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/100/100344.png", width=100)
    st.sidebar.title("Mantra MK")
    st.sidebar.write("*'A dor é temporária, a técnica é eterna.'*")

if __name__ == "__main__":
    main()
