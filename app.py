import streamlit as st

# Configuração Master
st.set_page_config(page_title="MK // LETHAL MUAY THAI", layout="wide")

# CSS "EXTREMO" - Customização total de UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;700&display=swap');

    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 50%, #1a0000 0%, #050505 100%);
    }

    /* Título Futurista */
    .title-container {
        text-align: center;
        padding: 40px;
        border: 1px solid #333;
        background: rgba(255, 0, 0, 0.05);
        border-radius: 2px;
        margin-bottom: 50px;
    }

    .main-title {
        font-family: 'Orbitron', sans-serif;
        color: #ff0000;
        font-size: 65px;
        font-weight: 900;
        letter-spacing: 15px;
        text-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
    }

    /* Cards de Golpes e Pontos Vitais */
    .fight-card {
        background: #0a0a0a;
        border: 1px solid #222;
        padding: 20px;
        transition: 0.4s;
        margin-bottom: 15px;
    }

    .fight-card:hover {
        border: 1px solid #ff0000;
        background: #110000;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.2);
    }

    .vital-title {
        color: #ff0000;
        font-family: 'Orbitron', sans-serif;
        font-size: 18px;
        text-transform: uppercase;
        border-bottom: 1px solid #333;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }

    .vital-desc {
        color: #888;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
    }

    /* Esconder elementos chatos */
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header de Elite
    st.markdown("""
        <div class="title-container">
            <div class="main-title">MK // STRIKER</div>
            <p style="color: #666; letter-spacing: 3px;">ADVANCED COMBAT SYSTEM v1.0</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("<h2 style='font-family: Orbitron; color: white;'>🔴 PONTOS VITAIS</h2>", unsafe_allow_html=True)
        
        vitals = [
            ("Têmpora", "Impacto causa desorientação imediata e perda de consciência."),
            ("Queixo (The Button)", "O ponto de nocaute principal. Rotaciona o crânio e desliga o sistema."),
            ("Fígado", "Localizado abaixo das costelas à direita. Um golpe bem encaixado paralisa o corpo."),
            ("Plexo Solar", "Interrompe o diafragma. Deixa o oponente sem ar instantaneamente."),
            ("Nervo Fibular", "Lado externo da coxa. Chutes aqui desativam a base e o movimento.")
        ]

        for title, desc in vitals:
            st.markdown(f"""
                <div class="fight-card">
                    <div class="vital-title">{title}</div>
                    <div class="vital-desc">{desc}</div>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h2 style='font-family: Orbitron; color: white;'>⚔️ ARSENAL LETHAL</h2>", unsafe_allow_html=True)
        
        tab_ataque, tab_tecnica = st.tabs(["ATAQUES", "SISTEMA DE DEFESA"])

        with tab_ataque:
            # Lista de golpes com estilo
            golpes = {
                "Jab & Cross": "A base de tudo. Velocidade e precisão.",
                "Thai Roundhouse Kick": "Poder devastador usando a tíbia como uma barra de ferro.",
                "Spear Knee": "Joelhada em linha reta furando a guarda.",
                "Horizontal Elbow": "Corte preciso. Fecha o supercílio e gera sangue."
            }
            
            for g, d in golpes.items():
                with st.expander(f"➔ {g}"):
                    st.write(d)
                    st.progress(90 if "Kick" in g else 70) # Barra de poder

        with tab_tecnica:
            st.markdown("""
                ### BLOQUEIO EM X
                Usado para aparar joelhadas e chutes frontais.
                ### ESQUIVA DE PENDULO
                Mover o tronco em 'U' para passar por baixo de ganchos.
                ### CHECKING (BLOQUEIO DE CANELA)
                Girar o joelho para fora e aparar o chute com a parte dura do osso.
            """)

    # Interface de "Treino de Hoje"
    st.write("---")
    st.markdown("<h3 style='text-align: center; font-family: Orbitron;'>GERADOR DE COMBINAÇÃO MK</h3>", unsafe_allow_html=True)
    
    if st.button("GERAR COMBO DE ELITE", use_container_width=True):
        combos = [
            "JAB + DIRETO + CRUZADO + LOW KICK",
            "DIRETO + CHUTE MÉDIO + JOELHADA DIRETA",
            "JAB + COTOVELO ASCENDENTE + CLICH + JOELHADA",
            "ESQUIVA LATERAL + GANCHO NO FÍGADO + CHUTE NA CABEÇA"
        ]
        import random
        st.error(f"EXECUTE: {random.choice(combos)}")

if __name__ == "__main__":
    main()
