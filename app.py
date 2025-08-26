import streamlit as st

st.set_page_config(page_title="My Friend Lumii", page_icon="🎓", layout="centered")

# ---------- Light UI polish ----------
st.markdown("""
<style>
:root { --maxw: 1100px; --muted:#5b6270; --radius:18px; }
.main > div { max-width: var(--maxw); margin: 0 auto; }
h1,h2,h3 { margin: .25rem 0 .75rem; }
.subtitle { color: var(--muted); margin-top: .25rem; }
.card { background:#fff; border:1px solid rgba(0,0,0,.06); border-radius:14px; padding:16px;
        box-shadow:0 1px 4px rgba(0,0,0,.06); }
.center { text-align:center; }
</style>
""", unsafe_allow_html=True)

# ---------- DISCLAIMER (modern, polished) ----------
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

# session default for the gate
if "agreed_to_terms" not in st.session_state:
    st.session_state.agreed_to_terms = False

# gate
if not st.session_state.agreed_to_terms:
    show_disclaimer()

# ---------- MAIN UI (shell) ----------
st.markdown('<h1 class="main-header">🎓 My Friend Lumii</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your safe AI Math, Physics, Chemistry, Geography & History tutor! 🛡️💙</p>', unsafe_allow_html=True)

# Welcome card
st.markdown("""
<div class="card" style="margin:10px 0;">
  🛡️ <b>Safety first</b> — always protective<br>
  📚 <b>Focus</b> — Math • Physics • Chemistry • Geography • History<br>
  💡 <b>Help</b> — clear explanations, study tips, confusion support<br>
  🤝 <b>Respect</b> — kind guidance
</div>
""", unsafe_allow_html=True)

# Help section
st.subheader("💙 If You Need Help")
st.markdown("**Talk to a trusted adult right now** — a parent/caregiver, teacher, or school counselor.")

# API status (placeholder — replace with your real block later)
st.subheader("🤖 AI Status")
try:
    # Example read from Streamlit secrets; replace with your logic
    api_key = st.secrets.get("GROQ_API_KEY")
    if st.session_state.get("memory_safe_mode", False):
        st.warning("⚠️ Memory Safe Mode Active")
    else:
        st.success("✅ Smart AI with Safety Active")
    st.caption("Full safety protocols enabled")
except Exception:
    st.error("❌ API Configuration Missing")

# Chat placeholder (replace with your chat logic later)
st.subheader("💬 Chat")
st.info("Chat placeholder — paste your existing chat/agent logic here.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#667; margin: 1rem 0;'>
  <p><strong>My Friend Lumii</strong> – Safe AI tutor for Math, Physics, Chemistry, Geography & History</p>
  <p>🛡️ Safety first • 🤝 Respectful learning • 💡 Clear explanations</p>
</div>
""", unsafe_allow_html=True)
