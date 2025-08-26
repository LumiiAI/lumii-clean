import streamlit as st

# ---------------------------------------------------------------------
# Page config FIRST (before any output)
# ---------------------------------------------------------------------
st.set_page_config(page_title="My Friend Lumii", page_icon="🎓", layout="centered")

# ---------------------------------------------------------------------
# Light UI polish (your block + a few extras)
# ---------------------------------------------------------------------
st.markdown("""
<style>
:root { --maxw: 1100px; --muted:#5b6270; --radius:18px; }
.main > div { max-width: var(--maxw); margin: 0 auto; }
h1,h2,h3 { margin: .25rem 0 .75rem; }
.subtitle { color: var(--muted); margin-top: .25rem; }
.card { background:#fff; border:1px solid rgba(0,0,0,.06); border-radius:14px; padding:16px;
        box-shadow:0 1px 4px rgba(0,0,0,.06); }
.center { text-align:center; }

.badge {display:inline-flex; gap:.4rem; align-items:center; padding:.35rem .6rem;
  border:1px solid rgba(0,0,0,.08); border-radius:999px; font-size:.82rem; background:#fff;}
.kpi {background:#fff; border:1px solid rgba(0,0,0,.06); border-radius:12px; padding:.9rem;
  box-shadow:0 1px 4px rgba(0,0,0,.05); text-align:center;}
.kpi .v {font-weight:700; font-size:1.1rem;}
.kpi .l {color:#5b6270; font-size:.85rem;}
.chips button {border-radius:999px !important; padding:.35rem .75rem !important; font-size:.9rem !important;
  border:1px solid rgba(0,0,0,.1)!important; background:#fff!important;}
.chips button:hover { background:#f7fafc!important; }
.stChatInput textarea { border-radius:14px!important; }
.section-title{font-weight:700; font-size:1.1rem; margin:.25rem 0 .5rem;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# Session defaults & tiny helpers
# ---------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chat_input" not in st.session_state:
    st.session_state["chat_input"] = ""

def render_status_badge(status: str, msg: str = "") -> str:
    """Return small HTML badge based on status."""
    if status == "warning":
        return f"<span class='badge' style='background:#fff8e1;border-color:#f6c453;'>⚠️ {msg or 'Managing memory'}</span>"
    if status == "critical":
        return f"<span class='badge' style='background:#ffe5e5;border-color:#f08a8a;'>⛔ {msg or 'Temporarily unavailable'}</span>"
    return "<span class='badge' style='background:#eefbf1;border-color:#9bd1a5;'>✅ Ready</span>"

# ---------------------------------------------------------------------
# DISCLAIMER (modern, polished)
# ---------------------------------------------------------------------
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

    # Two highlights
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card center">
          <h3 style="margin-top:0;">🚀 Beta Testing</h3>
          <p style="margin:0; color:#444;">You're among our early families — your feedback matters.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card center">
          <h3 style="margin-top:0;">🛡️ Safety First</h3>
          <p style="margin:0; color:#444;">Multiple safety layers keep you protected. Your wellbeing is #1.</p>
        </div>
        """, unsafe_allow_html=True)

    # Subjects grid
    st.markdown("""
    <div style='background:#f9fafb; padding:2rem; border-radius:18px; margin:2rem 0;'>
      <h2 style='text-align:center; margin-bottom:1.25rem;'>📚 Subjects I Can Help With</h2>
      <div style='display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:1rem;'>
        <div class='card center'>🧮 <b>Mathematics</b><br><span style='font-size:.9rem;color:#555;'>Algebra, Geometry, Calculus</span></div>
        <div class='card center'>⚡ <b>Physics</b><br><span style='font-size:.9rem;color:#555;'>Motion, Energy, Electricity</span></div>
        <div class='card center'>🧪 <b>Chemistry</b><br><span style='font-size:.9rem;color:#555;'>Reactions, Periodic Table</span></div>
        <div class='card center'>🌍 <b>Geography</b><br><span style='font-size:.9rem;color:#555;'>Maps, Countries</span></div>
        <div class='card center'>🏛️ <b>History</b><br><span style='font-size:.9rem;color:#555;'>Events, Timelines</span></div>
        <div class='card center'>📖 <b>Study Skills</b><br><span style='font-size:.9rem;color:#555;'>Organization, Test Prep</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Important info
    st.markdown("""
    <div style='background:#fff8f0; padding:2rem; border-radius:18px; margin:2rem 0;'>
      <h3 style='text-align:center; margin-bottom:1.25rem;'>💡 Important Information</h3>
      <ul style='list-style:none; padding:0; max-width:680px; margin:0 auto;'>
        <li style='margin-bottom:1rem;'><b>👨‍👩‍👧‍👦 Ask Your Parents First:</b> If under 16, please get parental permission.</li>
        <li style='margin-bottom:1rem;'><b>📖 Not Covered in Beta:</b> English, Biology, Social Studies, Health/PE, Art, Music, Foreign Languages.</li>
        <li><b>🔒 Safety Promise:</b> I will never help with anything harmful. If you're having difficult thoughts, please talk to a trusted adult.</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

    # CTA + button
    st.markdown("""
    <div class='center' style='margin:2rem 0 1rem;'>
      <p style='font-size:1.05rem; color:#333; margin-bottom:1rem;'>
        <strong>Ready to start learning safely?</strong><br>
        Click below if you understand and your parents are okay with it!
      </p>
    </div>
    """, unsafe_allow_html=True)

    agree = st.button("🎓 I Agree & Start Learning with Lumii!", type="primary")
    if agree:
        st.session_state.agreed_to_terms = True
        st.rerun()

    # stop the rest of the app until agreed
    st.stop()

# Gate default & trigger
if "agreed_to_terms" not in st.session_state:
    st.session_state.agreed_to_terms = False
if not st.session_state.agreed_to_terms:
    show_disclaimer()

# ---------------------------------------------------------------------
# MAIN UI (header with live badge, KPIs, chips, chat, tips)
# ---------------------------------------------------------------------

# compute status (mock for now; plug your real function later)
status, status_msg = "normal", ""
badge_html = render_status_badge(status, status_msg)

# Header card
st.markdown(f"""
<div class="card" style="display:flex; align-items:center; justify-content:space-between;">
  <div>
    <div style="font-size:1.45rem; font-weight:800;">🎓 My Friend Lumii</div>
    <div class="subtitle">Safe, clear help for Math • Physics • Chemistry • Geography • History</div>
  </div>
  {badge_html}
</div>
""", unsafe_allow_html=True)

# KPIs (placeholders)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="kpi"><div class="v">—</div><div class="l">Conversations (today)</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="kpi"><div class="v">—</div><div class="l">Study streak</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="kpi"><div class="v">On</div><div class="l">Memory</div></div>', unsafe_allow_html=True)

# Quick-start chips (prefill chat)
st.markdown('<div class="section-title">Quick start</div>', unsafe_allow_html=True)
chip_cols = st.columns(5)
chips = [
    "Explain quadratic formula",
    "Help me balance this equation",
    "Walk me through Newton’s laws",
    "Map skills practice",
    "Study plan for a test",
]
for idx, (col, label) in enumerate(zip(chip_cols, chips)):
    with col:
        if st.button(label, key=f"chip_{idx}"):
            st.session_state["prefill"] = label
            st.rerun()

st.divider()

# Two-column layout: left chat, right tips
left, right = st.columns([2, 1])

# LEFT — Chat
with left:
    st.markdown('<div class="section-title">Chat</div>', unsafe_allow_html=True)

    # New chat button
    cA, cB = st.columns([1, 6])
    with cA:
        if st.button("🗑️ New chat", help="Clear this conversation"):
            st.session_state["messages"] = []
            st.session_state["chat_input"] = ""
            st.rerun()

    # History
    if st.session_state["messages"]:
        for m in st.session_state["messages"]:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
    else:
        st.info("Ask a question or pick a quick-start chip above to begin.")

    # Input (prefill support)
    prefill = st.session_state.pop("prefill", None)
    if prefill:
        st.session_state["chat_input"] = prefill  # must match key below

    user_msg = st.chat_input(
        placeholder="Type your question… e.g., Can you explain slope-intercept form?",
        key="chat_input",
    )

    if user_msg:
        st.session_state["messages"].append({"role": "user", "content": user_msg})

        # TODO: replace with your real assistant call
        assistant_reply = "Got it! I’ll help step-by-step. (Replace me with your model call.)"
        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

        st.session_state["chat_input"] = ""
        st.rerun()

# RIGHT — Tips (no shortcuts)
with right:
    st.markdown('<div class="section-title">Tips</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      • Ask one clear question at a time<br>
      • Share what you already tried<br>
      • Say how detailed you want the answer
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("💡 You can edit labels, tips, and colors right in the code — everything above is pure UI.")

# ---------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#667; margin: 1rem 0;'>
  <p><strong>My Friend Lumii</strong> – Safe AI tutor for Math, Physics, Chemistry, Geography & History</p>
  <p>🛡️ Safety first • 🤝 Respectful learning • 💡 Clear explanations</p>
</div>
""", unsafe_allow_html=True)
