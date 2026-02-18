import streamlit as st
import matplotlib.pyplot as plt
from analytics.heatmap import mines_safety_map
from rl.ppo import train_ppo
from analytics.tracking import log_session
from engine.multi_game import choose_game
from fairness.verifier import verify

def show():
    st.title("BetMind AI v2 — Advanced Platform")

    tabs = st.tabs(["Heatmap", "Deep RL", "Tracking", "MultiGame", "Fairness"])

    with tabs[0]:
        if st.button("Compute Safety Map"):
            heat = mines_safety_map()
            fig, ax = plt.subplots()
            ax.imshow(heat)
            st.pyplot(fig)

    with tabs[1]:
        if st.button("Train PPO Agent"):
            score = train_ppo()
            st.success(f"Training score {score}")

    with tabs[2]:
        if st.button("Log Demo Session"):
            log_session("sessions.csv", {"profit":1.2,"risk":0.3})
            st.success("Logged")

    with tabs[3]:
        metrics={"Crash":{"edge":0.1,"risk":0.4},
                 "Mines":{"edge":0.2,"risk":0.2}}
        best=choose_game(metrics)
        st.write("Recommended game:",best)

    with tabs[4]:
        s=st.text_input("Server")
        c=st.text_input("Client")
        n=st.number_input("Nonce",0)
        h=st.text_input("Hash")
        if st.button("Verify"):
            ok=verify(s,c,n,h)
            st.write("Valid" if ok else "Mismatch")
