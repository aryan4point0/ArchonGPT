from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain
)


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # =========================
    # STEP 1 — SEARCH AGENT
    # =========================

    print("\n" + "=" * 60)
    print("STEP 1 - SEARCH AGENT IS WORKING...")
    print("=" * 60)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "input": f"Find recent, reliable and detailed information about: {topic}"
    })

    state["search_results"] = search_result["output"]

    print("\nSEARCH RESULTS:\n")
    print(state["search_results"])

    # =========================
    # STEP 2 — READER AGENT
    # =========================

    print("\n" + "=" * 60)
    print("STEP 2 - READER AGENT IS SCRAPING TOP RESOURCES...")
    print("=" * 60)

    reader_agent = build_reader_agent()

    reader_prompt = f"""
Based on the following search results about '{topic}', identify the most relevant URL.

Then scrape the webpage and extract the most useful detailed information.

SEARCH RESULTS:
{state['search_results']}
"""

    reader_result = reader_agent.invoke({
        "input": reader_prompt
    })

    state["scraped_content"] = reader_result["output"]

    print("\nSCRAPED CONTENT:\n")
    print(state["scraped_content"])

    # =========================
    # STEP 3 — WRITER CHAIN
    # =========================

    print("\n" + "=" * 60)
    print("STEP 3 - WRITER IS DRAFTING THE REPORT...")
    print("=" * 60)

    combined_research = f"""
SEARCH RESULTS:
{state['search_results']}

DETAILED SCRAPED CONTENT:
{state['scraped_content']}
"""

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": combined_research
    })

    print("\nFINAL REPORT:\n")
    print(state["report"])

    # =========================
    # STEP 4 — CRITIC CHAIN
    # =========================

    print("\n" + "=" * 60)
    print("STEP 4 - CRITIC IS REVIEWING THE REPORT...")
    print("=" * 60)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCRITIC FEEDBACK:\n")
    print(state["feedback"])

    # =========================
    # FINAL STATE
    # =========================

    return state


if __name__ == "__main__":

    topic = input("\nEnter a research topic: ")

    final_state = run_research_pipeline(topic)
 



