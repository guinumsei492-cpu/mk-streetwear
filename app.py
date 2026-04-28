import streamlit as st

# Configuração de Interface Técnica
st.set_page_config(page_title="MK // COMBAT MECHANICS", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syncopate:wght@700&display=swap');

    .stApp {
        background-color: #050505;
        color: #e0e0e0;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Cabeçalho Estilo Militar */
    .header-box {
        border-left: 10px solid #ff0000;
        padding-left: 20px;
        margin-bottom: 40px;
        background: linear-gradient(90deg, #1a0000 0%, transparent 100%);
    }

    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 45px;
        color: #ffffff;
        letter-spacing: 2px;
        margin: 0;
    }

    /* Cards de Execução */
    .step-card {
        background: #0a0a0a;
        border: 1px solid #1a1a1a;
        padding: 25px;
        margin-bottom: 20px;
        border-radius: 4px;
    }

    .step-number {
        color: #ff0000;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 10px;
        display: block;
    }

    .technique-name {
        font-size: 24px;
        color: #fff;
        font-weight: bold;
        border-bottom: 1px solid #ff0000;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }

    .execution-list {
        list-style-type: none;
        padding-left: 0;
    }

    .execution-list li {
        margin-bottom: 10px;
        padding-left: 15px;
        border-left: 2px solid #333;
    }

    /* Ponto Vital - Destaque */
    .vital-highlight {
        color: #ff0000;
        font-weight: bold;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
        <div class="header-box">
            <p style="color: #ff0000; margin-bottom: 5px;">CLASSIFIED // INSTRUCTIONAL MANUAL</p>
            <h1 class="main-title">MK MECHANICAL STRIKE</h1>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("### [ EXECUÇÃO DE ARSENAL ]")
        
        # Técnica 1: Roundhouse Kick (Chute Circular)
        with st.container():
            st.markdown("""
                <div class="step-card">
                    <span class="step-number">TECH #01</span>
                    <div class="technique-name">THAI ROUNDHOUSE KICK</div>
                    <ul class="execution-list">
                        <li><b>O PASSO:</b> Dê um passo diagonal (45°) para fora com a perna da frente, abrindo o quadril.</li>
                        <li><b>O EIXO:</b> Gire sobre a ponta do pé de apoio. O calcanhar deve apontar para o alvo no momento do impacto.</li>
                        <li><b>A TRAJETÓRIA:</b> Não chute para cima; chute ATRAVÉS do alvo, como se fosse cortar o oponente ao meio.</li>
                        <li><b>O IMPACTO:</b> Conecte com a parte inferior da <span class="vital-highlight">TÍBIA (CANELA)</span>, nunca com o pé.</li>
                        <li><b>O BRAÇO:</b> Jogue o braço do mesmo lado do chute para baixo e para trás para gerar torque e equilíbrio.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

        # Técnica 2: Spear Knee (Joelhada)
        with st.container():
            st.markdown("""
                <div class="step-card">
                    <span class="step-number">TECH #02</span>
                    <div class="technique-name">SPEAR KNEE (KAO TAWN)</div>
                    <ul class="execution-list">
                        <li><b>A POSTURA:</b> Projete o quadril para frente enquanto sobe o joelho.</li>
                        <li><b>O PÉ:</b> Mantenha os dedos do pé que golpeia apontados para baixo para tencionar a musculatura da perna.</li>
                        <li><b>O CONTATO:</b> Use a ponta do joelho para perfurar o <span class="vital-highlight">PLEXO SOLAR</span> ou o <span class="vital-highlight">FÍGADO</span>.</li>
                        <li><b>A DEFESA:</b> Mantenha o queixo colado no ombro oposto e a guarda alta durante a projeção.</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("### [ ANATOMIA DO DANO ]")
        
        st.markdown("""
            <div class="step-card">
                <div class="vital-title" style="color:#ff0000; font-weight:bold;">ALVOS DE ALTA PRIORIDADE</div>
                <hr style="border-color:#333">
                <p><b>1. NERVO MANDIBULAR:</b> Localizado no queixo. O impacto causa uma oscilação cerebral (Nocaute).</p>
                <p><b>2. ARTÉRIA CARÓTIDA:</b> Lateral do pescoço. Chutes altos aqui interrompem o fluxo sanguíneo cerebral.</p>
                <p><b>3. NERVO CIÁTICO:</b> Alvo principal dos Low Kicks. Localizado no meio da lateral da coxa.</p>
                <p><b>4. COSTELAS FLUTUANTES:</b> Alvo de chutes médios e joelhadas. Facilmente fraturáveis, interrompendo a respiração.</p>
            </div>
        """, unsafe_allow_html=True)

        # Pequeno "Easter Egg" de Dev
        st.write("---")
        if st.checkbox("MOSTRAR CÓDIGO DE CONDUTA"):
            st.code("""
            if oponente_abriu_guarda:
                executar(Knee_Spear)
            elif oponente_recuou:
                executar(Low_Kick)
            else:
                manter(Distancia_Segura)
            """, language="python")

    # Rodapé Técnico
    st.markdown("<p style='text-align: center; color: #333; font-size: 10px;'>MK COMBAT SYSTEMS // ENCRYPTION ENABLED</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
