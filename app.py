import streamlit as st

# ───────────────────────── Page setup ─────────────────────────
st.set_page_config(page_title="My Friend Lumii", page_icon="🎓", layout="centered")

# ───────────────────────── Light styles ───────────────────────
st.markdown("""
<style>
:root { --maxw: 1000px; --muted:#5b6270; --radius:18px; }
.main > div { max-width: var(--maxw); margin: 0 auto; }
h1,h2,h3 { margin: .25rem 0 .75rem; }
.center { text-align:center; }
.subtitle { color: var(--muted); margin-top:.25rem; }

/* Page tone + cards */
body { background:#fbfcfe; }
.card { background:#fff; border:1px solid rgba(0,0,0,.05); border-radius:14px; padding:16px;
        box-shadow:0 2px 8px rgba(0,0,0,.05); }

/* Chat input */
.stChatInput textarea { border-radius:14px!important; border:1px solid rgba(0,0,0,.12)!important; }
</style>
""", unsafe_allow_html=True)

# ───────────────────────── Session ────────────────────────────
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chat_input" not in st.session_state:
    st.session_state["chat_input"] = ""

# ───────────────────────── Disclaimer (pre-chat) ──────────────
def show_disclaimer():
    # Hero
    st.markdown("""
    <div style='text-align:center; padding: 2rem;
         background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
         border-radius: 18px; margin-bottom: 2rem; color: white;'>
      <h1 style='font-size: 2.5rem; margin-bottom:.5rem;'>🎓 Welcome to My Friend Lumii!</h1>
      <p style='font-size:1.2rem; margin:0; opacity:.95;'>Your Safe AI Learning Companion</p>
    </div>
    """, unsafe_allow_html=True)

    # Short highlights
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card center"><h3 style="margin:0 0 .35rem 0;">🚀 Beta Testing</h3>
        <p style="margin:0; color:#444;">You're among our early families — your feedback matters.</p></div>""",
                    unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card center"><h3 style="margin:0 0 .35rem 0;">🛡️ Safety First</h3>
        <p style="margin:0; color:#444;">Multiple safety layers keep you protected.</p></div>""",
                    unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div class='center' style='margin:2rem 0 1rem;'>
      <p style='font-size:1.05rem; color:#333; margin-bottom:1rem;'>
        <strong>Ready to start learning safely?</strong><br>
        Click below if you understand and your parents are okay with it!
      </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🎓 I Agree & Start Learning with Lumii!", type="primary"):
        st.session_state.agreed_to_terms = True
        st.rerun()

    st.stop()

if "agreed_to_terms" not in st.session_state:
    st.session_state.agreed_to_terms = False
if not st.session_state.agreed_to_terms:
    show_disclaimer()

# ───────────────────────── Clean Chat UI ──────────────────────
st.markdown("<h1 style='text-align:center;'>🎓 My Friend Lumii</h1>", unsafe_allow_html=True)

# History
if st.session_state["messages"]:
    for m in st.session_state["messages"]:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
else:
    st.info("👋 Hi! Ask me a question to get started.")

# Input
user_msg = st.chat_input("Type your question here…")
if user_msg:
    st.session_state["messages"].append({"role": "user", "content": user_msg})

    # Stub assistant reply (replace with real model later)
    reply = "Got it! I’ll help step by step. (Replace me with your model call.)"
    st.session_state["messages"].append({"role": "assistant", "content": reply})

    st.rerun()

# ───────────────────────── Footer disclaimer (black text) ─────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align:center; font-size:0.9rem; color:#222; margin-top:0.75rem;'>
      ⚠️ Beta version — may make mistakes. Please double-check important answers with a teacher or parent.
    </div>
    """,
    unsafe_allow_html=True,
)
