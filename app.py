import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="ArchonGPT",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    background-color: #060606 !important;
    color: #d4d4d4;
}
.stApp { background-color: #060606 !important; }
.main .block-container {
    max-width: 880px;
    padding: 0 2rem 5rem;
    margin: 0 auto;
}
section[data-testid="stSidebar"] { background: #0a0a0a !important; }

/* ── Top navbar ── */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem 0 1rem;
    border-bottom: 1px solid #111;
    margin-bottom: 3rem;
}
.navbar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
}
.navbar-icon {
    width: 34px; height: 34px;
    border-radius: 8px;
    background: linear-gradient(135deg, #ea580c, #f97316);
    display: flex; align-items: center; justify-content: center;
    font-size: 17px;
    box-shadow: 0 0 16px rgba(249,115,22,0.4);
}
.navbar-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.2rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #f5f5f5;
}
.navbar-name span {
    background: linear-gradient(135deg, #f97316, #fdba74);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.navbar-tag {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #2a2a2a;
    border: 1px solid #1a1a1a;
    border-radius: 100px;
    padding: 3px 10px;
}

/* ── Hero ── */
.hero-wrap {
    text-align: center;
    padding: 1rem 0 3rem;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(249,115,22,0.08);
    border: 1px solid rgba(249,115,22,0.2);
    border-radius: 100px;
    padding: 5px 16px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #c2622a;
    margin-bottom: 1.75rem;
}
.hero-badge-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #f97316;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.2} }

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -2.5px;
    margin-bottom: 1.25rem;
}
.hero-title .white { color: #f0f0f0; }
.hero-title .orange {
    background: linear-gradient(135deg, #f97316 0%, #fb923c 50%, #fdba74 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-subtitle {
    font-size: 1rem;
    color: #2d2d2d;
    line-height: 1.6;
    margin-bottom: 0.5rem;
}
.hero-pills {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 1.25rem;
}
.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #0f0f0f;
    border: 1px solid #1a1a1a;
    border-radius: 100px;
    padding: 4px 12px;
    font-size: 0.72rem;
    color: #333;
    letter-spacing: 0.3px;
}

/* ── Input card ── */
.input-card {
    background: #0a0a0a;
    border: 1px solid #161616;
    border-radius: 18px;
    padding: 1.75rem 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 0 60px rgba(249,115,22,0.04);
}

.stTextInput > div > div > input {
    background: #060606 !important;
    border: 1px solid #1c1c1c !important;
    border-radius: 10px !important;
    color: #e5e5e5 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.85rem 1.1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    caret-color: #f97316;
}
.stTextInput > div > div > input::placeholder { color: #222 !important; }
.stTextInput > div > div > input:focus {
    border-color: #ea580c !important;
    box-shadow: 0 0 0 3px rgba(234,88,12,0.1) !important;
    outline: none !important;
}
.stTextInput label {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    color: #2a2a2a !important;
}

/* ── Button ── */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #c2410c, #ea580c, #f97316) !important;
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.8px !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.82rem 2rem !important;
    margin-top: 0.85rem !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 28px rgba(234,88,12,0.35) !important;
}
.stButton > button:hover {
    box-shadow: 0 6px 36px rgba(234,88,12,0.55) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Section label ── */
.sec-label {
    font-size: 0.67rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #222;
    margin: 0 0 1rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.sec-label::after { content: ''; flex: 1; height: 1px; background: #111; }

/* ── Agent cards ── */
.agent-card {
    background: #0a0a0a;
    border: 1px solid #141414;
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
    display: flex;
    align-items: center;
    gap: 11px;
    transition: all 0.3s;
    margin-bottom: 10px;
}
.agent-card.running { border-color: #7c2d12; background: #0f0804; }
.agent-card.done    { border-color: #14532d; background: #040f07; }

.agent-icon {
    width: 34px; height: 34px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px; flex-shrink: 0;
}
.agent-card.idle    .agent-icon { background: #111; }
.agent-card.running .agent-icon { background: rgba(249,115,22,0.1); }
.agent-card.done    .agent-icon { background: rgba(74,222,128,0.07); }

.agent-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.8rem;
    font-weight: 600;
    flex: 1;
}
.agent-card.idle    .agent-name { color: #2d2d2d; }
.agent-card.running .agent-name { color: #f97316; }
.agent-card.done    .agent-name { color: #4ade80; }

.agent-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.agent-card.idle    .agent-dot { background: #1a1a1a; }
.agent-card.running .agent-dot { background: #f97316; animation: pulse 1s infinite; }
.agent-card.done    .agent-dot { background: #4ade80; }

/* ── Output panels ── */
.output-panel {
    background: #080808;
    border: 1px solid #141414;
    border-radius: 14px;
    margin-bottom: 1.25rem;
    overflow: hidden;
}
.output-panel-header {
    display: flex; align-items: center; gap: 8px;
    padding: 0.8rem 1.2rem;
    border-bottom: 1px solid #111;
    background: #0a0a0a;
}
.output-panel-dot { width: 7px; height: 7px; border-radius: 50%; }
.output-panel-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem; font-weight: 700;
    letter-spacing: 1px; text-transform: uppercase;
}
.output-panel-body {
    padding: 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem; line-height: 1.8;
    white-space: pre-wrap; word-break: break-word;
    max-height: 360px; overflow-y: auto;
}
.output-panel-body::-webkit-scrollbar { width: 3px; }
.output-panel-body::-webkit-scrollbar-thumb { background: #1c1c1c; border-radius: 4px; }

.output-panel.search .output-panel-dot   { background: #f97316; }
.output-panel.search .output-panel-title { color: #f97316; }
.output-panel.search .output-panel-body  { color: #6b3015; }

.output-panel.reader .output-panel-dot   { background: #fb923c; }
.output-panel.reader .output-panel-title { color: #fb923c; }
.output-panel.reader .output-panel-body  { color: #7a3f1a; }

/* ── Report ── */
.report-panel {
    background: #070707;
    border: 1px solid #141414;
    border-top: 2px solid #f97316;
    border-radius: 14px; overflow: hidden; margin-bottom: 1.25rem;
}
.report-panel-header {
    padding: 0.8rem 1.2rem;
    border-bottom: 1px solid #0f0f0f;
    background: #0a0a0a;
    display: flex; align-items: center; gap: 8px;
}
.report-panel-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem; font-weight: 700;
    letter-spacing: 1px; text-transform: uppercase; color: #f97316;
}
.report-panel-body {
    padding: 1.5rem 1.75rem;
    font-family: 'Inter', sans-serif;
    font-size: 0.92rem; line-height: 1.9; color: #555;
    white-space: pre-wrap; word-break: break-word;
    max-height: 520px; overflow-y: auto;
}
.report-panel-body::-webkit-scrollbar { width: 3px; }
.report-panel-body::-webkit-scrollbar-thumb { background: #1a1a1a; border-radius: 4px; }

/* ── Feedback ── */
.feedback-panel {
    background: #070707;
    border: 1px solid #141414;
    border-top: 2px solid #fb923c;
    border-radius: 14px; overflow: hidden; margin-bottom: 1.25rem;
}
.feedback-panel-header {
    padding: 0.8rem 1.2rem;
    border-bottom: 1px solid #0f0f0f;
    background: #0a0a0a;
}
.feedback-panel-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem; font-weight: 700;
    letter-spacing: 1px; text-transform: uppercase; color: #fb923c;
}
.feedback-panel-body {
    padding: 1.25rem 1.5rem;
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem; line-height: 1.85; color: #4d2c0e;
    white-space: pre-wrap; word-break: break-word;
    max-height: 360px; overflow-y: auto;
}
.feedback-panel-body::-webkit-scrollbar { width: 3px; }
.feedback-panel-body::-webkit-scrollbar-thumb { background: #1a1a1a; border-radius: 4px; }

/* ── Spinner ── */
.stSpinner > div { border-top-color: #f97316 !important; }

/* ── Alerts ── */
div[data-testid="stAlert"] {
    background: #0a0600 !important;
    border: 1px solid #7c2d12 !important;
    border-radius: 10px !important;
    color: #fb923c !important;
}

/* ── Footer ── */
.footer {
    margin-top: 5rem;
    padding-top: 1.5rem;
    border-top: 1px solid #0f0f0f;
    text-align: center;
}
.footer-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: #1a1a1a;
    letter-spacing: -0.3px;
}
.footer-logo span {
    background: linear-gradient(135deg, #7c2d12, #c2410c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.footer-sub {
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #141414;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)


# ── Navbar ────────────────────────────────────
st.markdown("""
<div class="navbar">
    <div class="navbar-logo">
        <div class="navbar-icon">⚡</div>
        <div class="navbar-name">Archon<span>GPT</span></div>
    </div>
    <div class="navbar-tag">Research Agent</div>
</div>
""", unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">
        <div class="hero-badge-dot"></div>
        AI-Powered Research
    </div>
    <div class="hero-title">
        <span class="white">Your Research,</span><br>
        <span class="orange">Supercharged.</span>
    </div>
    <div class="hero-subtitle">Enter any topic and ArchonGPT's multi-agent pipeline handles the rest.</div>
    <div class="hero-pills">
        <div class="hero-pill">🔍 Web Search</div>
        <div class="hero-pill">📖 Source Scraping</div>
        <div class="hero-pill">✍️ Report Writing</div>
        <div class="hero-pill">🧠 Quality Critique</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Input ─────────────────────────────────────
st.markdown('<div class="input-card">', unsafe_allow_html=True)
topic = st.text_input(
    "What do you want to research?",
    placeholder="e.g.  The future of nuclear fusion energy",
)
run_btn = st.button("⚡  Launch ArchonGPT")
st.markdown('</div>', unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────
AGENTS = [
    ("search", "🔍", "Search Agent"),
    ("reader", "📖", "Reader Agent"),
    ("writer", "✍️",  "Writer Chain"),
    ("critic", "🧠",  "Critic Chain"),
]

def render_agents(statuses, placeholders):
    for key, icon, name in AGENTS:
        status = statuses.get(key, "idle")
        placeholders[key].markdown(
            f'<div class="agent-card {status}">'
            f'<div class="agent-icon">{icon}</div>'
            f'<div class="agent-name">{name}</div>'
            f'<div class="agent-dot"></div>'
            f'</div>',
            unsafe_allow_html=True,
        )

def output_panel(kind, icon, title, body):
    return (
        f'<div class="output-panel {kind}">'
        f'<div class="output-panel-header">'
        f'<div class="output-panel-dot"></div>'
        f'<div class="output-panel-title">{icon}&nbsp; {title}</div>'
        f'</div>'
        f'<div class="output-panel-body">{body}</div>'
        f'</div>'
    )


# ── Pipeline ──────────────────────────────────
if run_btn:
    if not topic.strip():
        st.error("Please enter a research topic before running.")
        st.stop()

    try:
        from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
    except Exception as e:
        st.error(f"❌ Could not import agents: {e}")
        st.stop()

    st.markdown('<div class="sec-label">Pipeline Status</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    ph = {}
    with col1:
        ph["search"] = st.empty()
        ph["writer"] = st.empty()
    with col2:
        ph["reader"] = st.empty()
        ph["critic"] = st.empty()

    statuses = {k: "idle" for k, _, __ in AGENTS}
    render_agents(statuses, ph)

    out_search   = st.empty()
    out_reader   = st.empty()
    out_report   = st.empty()
    out_feedback = st.empty()

    try:
        state = {}

        # STEP 1 — SEARCH
        statuses["search"] = "running"
        render_agents(statuses, ph)
        with st.spinner("ArchonGPT is searching the web…"):
            agent = build_search_agent()
            result = agent.invoke({"input": f"Find recent, reliable and detailed information about: {topic}"})
            state["search_results"] = result["output"]
        statuses["search"] = "done"
        render_agents(statuses, ph)
        out_search.markdown(output_panel("search", "🔍", "Search Results", state["search_results"]), unsafe_allow_html=True)

        # STEP 2 — READER
        statuses["reader"] = "running"
        render_agents(statuses, ph)
        with st.spinner("ArchonGPT is scraping top sources…"):
            agent = build_reader_agent()
            prompt = (
                f"Based on the following search results about '{topic}', identify the most relevant URL.\n"
                f"Then scrape the webpage and extract the most useful detailed information.\n\n"
                f"SEARCH RESULTS:\n{state['search_results']}"
            )
            result = agent.invoke({"input": prompt})
            state["scraped_content"] = result["output"]
        statuses["reader"] = "done"
        render_agents(statuses, ph)
        out_reader.markdown(output_panel("reader", "📖", "Scraped Content", state["scraped_content"]), unsafe_allow_html=True)

        # STEP 3 — WRITER
        statuses["writer"] = "running"
        render_agents(statuses, ph)
        combined = (
            f"SEARCH RESULTS:\n{state['search_results']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
        )
        with st.spinner("ArchonGPT is drafting your report…"):
            state["report"] = writer_chain.invoke({"topic": topic, "research": combined})
        statuses["writer"] = "done"
        render_agents(statuses, ph)
        out_report.markdown(
            f'<div class="report-panel">'
            f'<div class="report-panel-header"><div class="report-panel-title">📄&nbsp; Final Report</div></div>'
            f'<div class="report-panel-body">{state["report"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # STEP 4 — CRITIC
        statuses["critic"] = "running"
        render_agents(statuses, ph)
        with st.spinner("ArchonGPT is reviewing quality…"):
            state["feedback"] = critic_chain.invoke({"report": state["report"]})
        statuses["critic"] = "done"
        render_agents(statuses, ph)
        out_feedback.markdown(
            f'<div class="feedback-panel">'
            f'<div class="feedback-panel-header"><div class="feedback-panel-title">🧠&nbsp; Critic Feedback</div></div>'
            f'<div class="feedback-panel-body">{state["feedback"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.success("✅  ArchonGPT has completed your research!")

    except Exception as e:
        st.error(f"Pipeline error: {e}")


# ── Footer ────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-logo">Archon<span>GPT</span></div>
    <div class="footer-sub">Multi-Agent Research System &nbsp;·&nbsp; Powered by LangChain</div>
</div>
""", unsafe_allow_html=True)


