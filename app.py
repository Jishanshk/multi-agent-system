import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Multi-Agent Research System")
st.caption("Search → Read → Write → Critique, powered by your LangChain/LangGraph agent pipeline.")

# ---------------------------------------------------------
# Session state to keep results around between reruns
# ---------------------------------------------------------
if "state" not in st.session_state:
    st.session_state.state = None

# ---------------------------------------------------------
# Input form
# ---------------------------------------------------------
with st.form("research_form"):
    topic = st.text_input("Research Topic", placeholder="e.g. Impact of AI on renewable energy adoption")
    submitted = st.form_submit_button("Run Research", type="primary", use_container_width=True)

# ---------------------------------------------------------
# Run pipeline with live step-by-step feedback
# ---------------------------------------------------------
if submitted:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        state = {}
        progress = st.progress(0, text="Starting pipeline...")

        try:
            # STEP 1 - Search
            with st.status("Step 1 · Search Agent", expanded=True) as status:
                from agent import build_reader_agent, build_search_agent, writer_chain, critic_chain

                search_agent = build_search_agent()
                search_results = search_agent.invoke(topic)
                state["search_results"] = search_results
                st.write(search_results)
                status.update(label="Step 1 · Search Agent ✅", state="complete")
            progress.progress(25, text="Search complete...")

            # STEP 2 - Reader
            with st.status("Step 2 · Reader Agent", expanded=True) as status:
                reader_agent = build_reader_agent()
                scraped_content = reader_agent.invoke(search_results)
                state["scraped_content"] = scraped_content
                st.write(scraped_content)
                status.update(label="Step 2 · Reader Agent ✅", state="complete")
            progress.progress(50, text="Reading/scraping complete...")

            # STEP 3 - Writer
            with st.status("Step 3 · Writer", expanded=True) as status:
                research = f"""
                SEARCH RESULTS
                {state["search_results"]}

                SCRAPED CONTENT
                {state["scraped_content"]}
                """
                report = writer_chain.invoke({"topic": topic, "research": research})
                state["report"] = report
                st.markdown(report)
                status.update(label="Step 3 · Writer ✅", state="complete")
            progress.progress(75, text="Draft written...")

            # STEP 4 - Critic
            with st.status("Step 4 · Critic", expanded=True) as status:
                feedback = critic_chain.invoke({"report": report})
                state["feedback"] = feedback
                st.write(feedback)
                status.update(label="Step 4 · Critic ✅", state="complete")
            progress.progress(100, text="Done!")

            st.session_state.state = state
            st.success("Research pipeline completed successfully!")

        except Exception as e:
            st.error(f"Pipeline failed: {e}")

# ---------------------------------------------------------
# Final results view (persists across reruns)
# ---------------------------------------------------------
if st.session_state.state:
    state = st.session_state.state
    st.divider()
    st.subheader("📄 Final Report")
    st.markdown(state.get("report", "_No report generated._"))

    st.subheader("🧠 Critic Feedback")
    st.write(state.get("feedback", "_No feedback generated._"))

    st.download_button(
        "Download Report (.md)",
        data=str(state.get("report", "")),
        file_name="research_report.md",
        mime="text/markdown",
        use_container_width=True,
    )

    with st.expander("🔍 Raw Search Results"):
        st.write(state.get("search_results", ""))

    with st.expander("📚 Raw Scraped Content"):
        st.write(state.get("scraped_content", ""))