import streamlit as st
from typing import Tuple

# ===============
# 0) CONFIG & GLOBALS
# ===============
st.set_page_config(page_title="My Friend Lumii", page_icon="🎓", layout="centered")

# ---- Lightweight UI polish (safe, optional) ----
_UI_CSS = """
<style>
:root{
  --radius: 14px; --radius-sm: 10px; --muted: rgba(0,0,0,.55);
}
.main > div { max-width: 1100px; margin: 0 auto; }
.lumii-card{ border-radius: var(--radius); padding: 16px; background: #fff;
  border: 1px solid rgba(0,0,0,.06); box-shadow: 0 1px 3px rgba(0,0,0,.06); }
.big-cta button{ border-radius: var(--radius-sm); padding: .85rem 1.15rem; font-weight: 700; }
.subtitle{ color: var(--muted); margin-top: .25rem; }
.footer{ text-align:center; color:#667; margin: 2rem 0 1rem; }
</style>
"""
st.markdown(_UI_CSS, unsafe_allow_html=True)

# ===============
# 1) DISCLAIMER GATE (unchanged logic)
# ===============

def _show_privacy_disclaimer() -> None:
    st.markdown("""
    <div style="text-align:center"> 
      <h1>🌟 Welcome to My Friend Lumii!</h1>
      <h2>🚀 Beta Testing Phase - Math & Science Tutor</h2>
    </div>
    """, unsafe_allow_html=True)

# Hero / Welcome banner
st.markdown("""
<div style='text-align: center; padding: 2rem; 
     background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
     border-radius: 18px; margin-bottom: 2rem; color: white;'>
  <h1 style='font-size: 2.5rem; margin-bottom: .5rem;'>🎓 Welcome to My Friend Lumii!</h1>
  <p style='font-size: 1.3rem; margin: 0; opacity: 0.95;'>Your Safe AI Learning Companion</p>
</div>
""", unsafe_allow_html=True)

# Two-column highlights
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='background: white; padding: 1.5rem; border-radius: 15px; 
         box-shadow: 0 3px 6px rgba(0,0,0,0.08); text-align:center;'>
      <h3 style='margin-top:0;'>🚀 Beta Testing</h3>
      <p style='margin:0; color:#444;'>You're among our first beta families! Your feedback makes Lumii better.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style='background: white; padding: 1.5rem; border-radius: 15px; 
         box-shadow: 0 3px 6px rgba(0,0,0,0.08); text-align:center;'>
      <h3 style='margin-top:0;'>🛡️ Safety First</h3>
      <p style='margin:0; color:#444;'>Multiple safety layers keep you protected. Your wellbeing is priority #1.</p>
    </div>
    """, unsafe_allow_html=True)

# Subjects grid
st.markdown("""
<div style='background:#f9fafb; padding:2rem; border-radius:18px; margin:2rem 0;'>
  <h2 style='text-align:center; margin-bottom:1.5rem;'>📚 Subjects I Can Help With</h2>
  <div style='display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:1rem;'>
    <div style='background:white; padding:1rem; border-radius:10px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,.06);'>
      🧮 <b>Mathematics</b><br><span style='font-size:.9rem;color:#555;'>Algebra, Geometry, Calculus</span>
    </div>
    <div style='background:white; padding:1rem; border-radius:10px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,.06);'>
      ⚡ <b>Physics</b><br><span style='font-size:.9rem;color:#555;'>Motion, Energy, Electricity</span>
    </div>
    <div style='background:white; padding:1rem; border-radius:10px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,.06);'>
      🧪 <b>Chemistry</b><br><span style='font-size:.9rem;color:#555;'>Reactions, Periodic Table</span>
    </div>
    <div style='background:white; padding:1rem; border-radius:10px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,.06);'>
      🌍 <b>Geography</b><br><span style='font-size:.9rem;color:#555;'>Maps, Countries, Features</span>
    </div>
    <div style='background:white; padding:1rem; border-radius:10px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,.06);'>
      🏛️ <b>History</b><br><span style='font-size:.9rem;color:#555;'>Events, Timelines</span>
    </div>
    <div style='background:white; padding:1rem; border-radius:10px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,.06);'>
      📖 <b>Study Skills</b><br><span style='font-size:.9rem;color:#555;'>Organization, Test Prep</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Important info
st.markdown("""
<div style='background:#fff8f0; padding:2rem; border-radius:18px; margin:2rem 0;'>
  <h3 style='text-align:center; margin-bottom:1.5rem;'>💡 Important Information</h3>
  <ul style='list-style:none; padding:0; max-width:600px; margin:0 auto; text-align:left;'>
    <li style='margin-bottom:1rem;'><b>👨‍👩‍👧‍👦 Ask Your Parents First:</b> If under 16, please get parental permission.</li>
    <li style='margin-bottom:1rem;'><b>📖 Not Covered in Beta:</b> English, Biology, Social Studies, Health/PE, Art, Music, Foreign Languages.</li>
    <li><b>🔒 Safety Promise:</b> I will never help with anything harmful. If you're having difficult thoughts, please talk to a trusted adult.</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# Call to action
st.markdown("""
<div style='text-align:center; margin:2.5rem 0;'>
  <p style='font-size:1.1rem; margin-bottom:1.5rem; color:#333;'>
    <strong>Ready to start learning safely?</strong><br>
    Click below if you understand and your parents are okay with it!
  </p>
</div>
""", unsafe_allow_html=True)

# Agree button (logic unchanged)
agree = st.button("🎓 I Agree & Start Learning with Lumii!", type="primary")
if agree:
    st.session_state.agreed_to_terms = True
    st.rerun()

st.stop()

if "agreed_to_terms" not in st.session_state:
    st.session_state.agreed_to_terms = False

if not st.session_state.agreed_to_terms:
    _show_privacy_disclaimer()

# ===============
# 2) MAIN UI SHELL (minimal presentation only)
# ===============

# -- Header
st.markdown('<h1 class="main-header">🎓 My Friend Lumii</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your safe AI Math, Physics, Chemistry, Geography & History tutor! 🛡️💙</p>', unsafe_allow_html=True)

# -- Status / memory banner (placeholder)

def check_conversation_length() -> Tuple[str, str]:
    """TEMP placeholder. Replace with your real logic later.
    Returns status in {"normal","warning","critical"}, and a message.
    """
    return "normal", "All good"

status, status_msg = check_conversation_length()
if status == "warning":
    st.warning(f"⚠️ {status_msg} – Memory management active")
elif status == "critical":
    st.error(f"🚨 {status_msg} – Automatic summarization will occur")

# -- Compact welcome card
st.markdown(
    """
<div style="
  background:#eaf2ff; border:1px solid #d6e9f9; border-radius:12px;
  padding:16px 18px; margin:8px 0 6px; font-size:16px; line-height:1.55;">
  🛡️ <b>Safety first</b> — always protective, never harmful<br>
  📚 <b>Focus</b> — Math • Physics • Chemistry • Geography • History<br>
  💡 <b>Help</b> — clear explanations, study tips, confusion support<br>
  🤝 <b>Respect</b> — kind, encouraging guidance
</div>
    """,
    unsafe_allow_html=True,
)

with st.expander("More details"):
    st.markdown(
        """
- ✅ **I can help with:** algebra, geometry, trigonometry, calculus; physics (mechanics, electricity, thermodynamics); chemistry (reactions, periodic table, molecules); geography (maps, countries, physical geography); history (timelines, events); study skills (organization, test prep)
- ❌ **Not in beta:** English/Literature, Biology/Life Science, Social Studies/Civics, Health/PE, Art/Music, Foreign languages
- 🧠 **Memory & support:** I remember our learning journey and provide encouragement
        """
    )

st.caption("💡 I remember our conversations, keep you safe, and focus only on my beta subjects.")

# -- Help section
st.subheader("💙 If You Need Help")
st.markdown("**Talk to a trusted adult right now** — a parent/caregiver, teacher, or school counselor.")

# -- API Status (placeholder)
st.subheader("🤖 AI Status")
try:
    # Replace with your real secret key / logic
    api_key = st.secrets.get("GROQ_API_KEY", None)
    if st.session_state.get("memory_safe_mode", False):
        st.warning("⚠️ Memory Safe Mode Active")
    else:
        st.success("✅ Smart AI with Safety Active")
    st.caption("Full safety protocols enabled")
except Exception:
    st.error("❌ API Configuration Missing")

# -- Chat / Logic placeholder (insert your existing app logic here later)
st.subheader("💬 Chat")
st.info("This is a placeholder chat area. Paste your existing chat/agent logic here when ready.")

# -- Footer (short)
st.markdown("---")
st.markdown("""
<div class="footer">
  <p><strong>My Friend Lumii</strong> – Safe AI tutor for Math, Physics, Chemistry, Geography & History</p>
  <p>🛡️ Safety first • 🤝 Respectful learning • 💡 Clear explanations</p>
</div>
""", unsafe_allow_html=True)
