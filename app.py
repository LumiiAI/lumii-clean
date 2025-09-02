import streamlit as st
from lumii_core_logic_v2 import LumiiState, generate_response_with_memory_safety
import base64
import os

from datetime import datetime
from zoneinfo import ZoneInfo  # built-in in Python 3.9+

DAILY_LIMIT = 20
TZ = ZoneInfo("Europe/Ljubljana")
FEEDBACK_FORM_URL = "https://forms.gle/XudYBTGsweCaKhc96"  # ← replace with your Google Form


# Require users to re-accept if we change the disclaimer meaningfully
DISCLAIMER_VERSION = "2025-09-01-v1"

@st.cache_data
def _logo_b64(path="logo.png") -> str:
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception:
        return ""  # falls back to no image if file missing

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

# --- Core logic state (for Lumii) ---
if "lumii_state" not in st.session_state:
    st.session_state["lumii_state"] = LumiiState()

# local handle
state = st.session_state["lumii_state"]

# make sure messages list is synced between UI and logic
state.setdefault("messages", st.session_state["messages"])
state["messages"] = st.session_state["messages"]

# ── Daily quota init/rollover ────────────────────────────────────────────────
today = datetime.now(TZ).date().isoformat()
dq = st.session_state.get("daily_quota") or {"date": today, "used": 0}
if dq.get("date") != today:
    dq = {"date": today, "used": 0}
st.session_state["daily_quota"] = dq
remaining = max(0, DAILY_LIMIT - dq["used"])

# ───────────────────────── Full Disclaimer (pre-chat) ─────────
def show_disclaimer():
    # Hero (logo + text inside the same gradient box)
    _b64 = _logo_b64("logo.png")
    st.markdown(f"""
    <style>
      /* stack on small screens */
      @media (max-width: 700px) {{
        .lumii-hero-flex {{ flex-direction: column; text-align: center; }}
        .lumii-hero-flex img {{ width: 120px !important; margin-bottom: .5rem; }}
      }}
    </style>
    <div style="
         background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
         border-radius: 18px; margin-bottom: 2rem; color: white;
         padding: 1.75rem 1.5rem;">
      <div class="lumii-hero-flex" style="
           display: flex; align-items: center; gap: 18px;">
        {"<img src='data:image/png;base64," + _b64 + "' alt='Lumii Logo' style='width:160px; border-radius:16px; filter:drop-shadow(0 4px 10px rgba(0,0,0,.15));'>" if _b64 else ""}
        <div>
          <h1 style="font-size: 2.4rem; margin:.25rem 0 .4rem;">Welcome to My Friend Lumii!</h1>
          <p style="font-size:1.15rem; margin:0; opacity:.95;">Your Safe AI Learning Companion</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True
)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Beta + Safety (boxed, theme-safe) ---
    with st.container(border=True):
        st.subheader("🚀 Beta Testing")
        st.write("You're among our first 100 beta families! Help us improve with your feedback.")

    with st.container(border=True):
        st.subheader("🛡️ Safety First")
        st.write("Multiple layers of protection keep you safe. Your wellbeing is #1.")

    # --- Subjects (boxed section with a simple grid) ---
    with st.container(border=True):
        st.markdown("## 📚 Subjects I Can Help With")

        row1 = st.columns(3)
        with row1[0]:
            st.markdown("**🧮 Mathematics**  \nAlgebra, Geometry, Calculus")
        with row1[1]:
            st.markdown("**⚡ Physics**  \nMotion, Energy, Electricity")
        with row1[2]:
            st.markdown("**🧪 Chemistry**  \nReactions, Periodic Table")

        row2 = st.columns(3)
        with row2[0]:
            st.markdown("**🌍 Geography**  \nMaps, Countries")
        with row2[1]:
            st.markdown("**🏛️ History**  \nEvents, Timelines")
        with row2[2]:
            st.markdown("**📖 Study Skills**  \nOrganization, Test Prep")


    # --- Disclaimer (dark-mode safe) ---
    with st.expander("📜 Disclaimer — click to read and agree", expanded=False):
        st.markdown("## 📜 Disclaimer")
        st.markdown("""
        Beta Testing Disclaimer
Important Notice: Beta Software

This is beta software under active development. By using MyFriendLumii K-12 Learning Companion, you acknowledge and agree to the following terms:
Educational Use Limitations

This tool is designed to supplement, not replace traditional teaching methods and human instruction
All educational content should be verified by qualified educators before relying on it for learning outcomes
The AI may provide incomplete, inaccurate, or inappropriate responses - always use with adult supervision for K-12 students
Not suitable for high-stakes educational decisions such as grading, placement, or assessment

Beta Software Risks
- Service interruptions and unexpected downtime may occur
- Data loss is possible - do not rely on the service to store critical information
- Features may change or be removed without notice as we improve the platform
- Response quality and accuracy will vary as we refine our algorithms

Privacy and Data Protection
- Student interactions may be logged and analyzed to improve our service
- We follow applicable  privacy laws 
- No personal identifying information should be shared in conversations
- Parents and educators should review all interactions involving minors

No Warranties
- MyFriendLumii provides this beta service "AS IS" without any warranties, express or implied
- We make no guarantees about educational outcomes, content accuracy, or service availability
- Use at your own risk and discretion

Your Participation
By participating in our beta program, you agree to:
- Provide constructive feedback about bugs, issues, and improvements
- Use the service responsibly and in accordance with educational best practices
- Supervise student interactions and ensure age-appropriate usage
- Report any concerning behavior or inappropriate content immediately after using the app via dedicated form.

Contact
For questions, concerns, or to report issues: 
Last Updated: 
This disclaimer may be updated as our beta program evolves. Continued use constitutes acceptance of any changes.

THE BETA SOFTWARE PROGRAM PRODUCT LICENSED HERE UNDER IS STILL IN ITS TESTING PHASE AND IS PROVIDED ON AN “AS IS” AND “AS AVAILABLE” BASIS AND IS BELIEVED TO CONTAIN DEFECTS.
A PRIMARY PURPOSE OF THIS BETA TESTING LICENCE IS TO OBTAIN FEEDBACK ON SOFTWARE PERFORMANCE AND THE IDENTIFICATION OF DEFECTS.
LICENSEE IS ADVISED TO SAFEGUARD IMPORTANT DATA, TO USE CAUTION AND NOT TO RELY IN ANY WAY ON THE CORRECT FUNCTIONING OR PERFORMANCE OF THE BETA SOFTWARE PROGRAM PRODUCT AND/OR ACCOMPANYING MATERIALS OR DOCUMENTATION.
        """)

        agree_check = st.checkbox("I have read and understood the disclaimer", key="agree_ck")

        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            st.markdown("<div style='margin-top:.5rem'></div>", unsafe_allow_html=True)
            if st.button("✅ I Agree & Start Learning", use_container_width=True, disabled=not agree_check, key="agree_btn"):
                st.session_state["agreed_version"] = DISCLAIMER_VERSION
                st.rerun()

    # IMPORTANT: stop the rest of the app from rendering until agreed
    st.stop()


if st.session_state.get("agreed_version") != DISCLAIMER_VERSION:
    show_disclaimer()
    st.stop()

# ───────────────────────── Clean Chat UI ──────────────────────

# Title (logo + title using same base64/flex approach as disclaimer)
_b64 = _logo_b64("logo.png")
st.markdown(f"""
<style>
  /* Stack on small screens */
  @media (max-width: 700px) {{
    .lumii-chat-header {{ flex-direction: column; text-align: center; gap: 10px; }}
    .lumii-chat-header img {{ width: 90px !important; }}
  }}
</style>
<div style="display:flex; align-items:center; justify-content:center; margin:.25rem 0 .35rem;">
  <div class="lumii-chat-header" style="display:flex; align-items:center; justify-content:center; gap:14px;">
    {("<img src='data:image/png;base64," + _b64 + "' alt='Lumii Logo' "
      "style='width:110px; border-radius:16px; filter:drop-shadow(0 3px 8px rgba(0,0,0,.12));'>") if _b64 else ""}
    <h1 style="margin:.1rem 0 .2rem; line-height:1.1;">My Friend Lumii</h1>
  </div>
</div>
""", unsafe_allow_html=True)

# Status banner (own box, Option A)
api_key = st.secrets.get("GROQ_API_KEY", "")
if not api_key:
    st.error("AI Offline — no API key configured", icon="⛔")
elif st.session_state.get("memory_safe_mode"):
    st.warning("Memory Safe Mode Active", icon="⚠️")
else:
    st.success("Smart AI with Safety Active", icon="✅")


# History + greeting + disclaimer box (when empty)
if st.session_state["messages"]:
    for m in st.session_state["messages"]:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
else:
    # Greeting banner
    st.info("👋 Hi! Ask me a question to get started.")

    # Disclaimer box under the banner
    st.markdown(
        """
        <style>
        .beta-box{
            margin: 10px 0 18px;
            padding: .75rem 1rem;
            background:#fff;
            border:1px solid rgba(0,0,0,.08);
            border-left: 4px solid #f7b500; /* subtle amber accent */
            border-radius: 10px;
            color:#222;
            font-size:.95rem;
        }
        </style>
        <div class="beta-box">
            ⚠️ Beta version — may make mistakes. Please double-check important answers with a teacher or parent.
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Daily quota status (chat page only): show just above the input ---
dq = st.session_state.get("daily_quota") or {
    "date": datetime.now(TZ).date().isoformat(),
    "used": 0
}
remaining = max(0, DAILY_LIMIT - dq.get("used", 0))
st.caption(f"🔢 Daily messages left: {remaining}/{DAILY_LIMIT} (Europe/Ljubljana)")

# --- Daily quota status (chat page only): show just above the input ---
dq = st.session_state.get("daily_quota") or {
    "date": datetime.now(TZ).date().isoformat(),
    "used": 0
}
remaining = max(0, DAILY_LIMIT - dq.get("used", 0))
st.caption(f"🔢 Daily messages left: {remaining}/{DAILY_LIMIT} (Europe/Ljubljana)")

# --- Chat input (ALWAYS render this at top level, near the end) ---
user_msg = st.chat_input("Type your question here…")

if user_msg:
    # ── 0) Hard cap: block before we add to history or call the model ─────────
    if st.session_state["daily_quota"]["used"] >= DAILY_LIMIT:
        st.info(
            "You’ve reached today’s 20-message limit. "
            "Thank you for testing Lumii! 🫶 We’d love your feedback to make Lumii better."
        )
        # Friendly button to your Google Form (configure FEEDBACK_FORM_URL at top)
        st.link_button("Share feedback", FEEDBACK_FORM_URL)
        st.stop()

    # ── 1) Append user message (for UI continuity) ────────────────────────────
    st.session_state["messages"].append({"role": "user", "content": user_msg})
    state["messages"] = st.session_state["messages"]

    # ── 2) Check API key; offline helper DOES NOT consume quota ───────────────
    api_key = st.secrets.get("GROQ_API_KEY", "")
    if not api_key:
        st.info("AI is offline (no API key found). Using helper mode for now.")
        helper = (
            "I’m currently offline, but I can still help you structure this!\n\n"
            "1) Tell me what the problem is.\n"
            "2) Share what you’ve tried.\n"
            "3) I’ll guide you step-by-step."
        )
        st.session_state["messages"].append({"role": "assistant", "content": helper})
        state["messages"] = st.session_state["messages"]
        st.rerun()

    # ── 3) We will call the model → consume 1 unit from today's quota ─────────
    st.session_state["daily_quota"]["used"] += 1

    # ── 4) Normal LLM path (guards, retries, trimming inside) ─────────────────
    result = generate_response_with_memory_safety(
        state=state,
        message=user_msg,
        tool_name="lumii_main",
        api_key=api_key,
    )

    # ── 5) Extract text + optional safety flag ────────────────────────────────
    ai_text = result.get("content") or "I ran into a temporary issue. Let’s try again."
    flag = result.get("priority")  # 'crisis' | 'manipulation' | 'subject_restricted' | None

    # ── 6) Append assistant reply and keep states in sync ─────────────────────
    st.session_state["messages"].append({"role": "assistant", "content": ai_text})
    state["messages"] = st.session_state["messages"]

    # ── 7) Optional: surface a small banner if a safety path triggered ────────
    if flag in {"crisis", "manipulation", "subject_restricted"}:
        st.warning(f"Safety filter active: {flag.replace('_',' ')}")

    st.rerun()

