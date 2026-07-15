from agent import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)

def run_research_pipeline(topic: str):

    state = {}

    # -----------------------------
    # STEP 1 : SEARCH
    # -----------------------------
    print("\n" + "=" * 60)
    print("STEP 1 - Search Agent")
    print("=" * 60)

    search_agent = build_search_agent()

    search_results = search_agent.invoke(topic)

    state["search_results"] = search_results

    print(search_results)


    # -----------------------------
    # STEP 2 : READER
    # -----------------------------
    print("\n" + "=" * 60)
    print("STEP 2 - Reader Agent")
    print("=" * 60)

    reader_agent = build_reader_agent()

    scraped_content = reader_agent.invoke(search_results)

    state["scraped_content"] = scraped_content

    print(scraped_content)


    # -----------------------------
    # STEP 3 : WRITER
    # -----------------------------
    print("\n" + "=" * 60)
    print("STEP 3 - Writer")
    print("=" * 60)

    research = f"""
SEARCH RESULTS

{state["search_results"]}


SCRAPED CONTENT

{state["scraped_content"]}
"""

    report = writer_chain.invoke({
        "topic": topic,
        "research": research,
    })

    state["report"] = report

    print(report)


    # -----------------------------
    # STEP 4 : CRITIC
    # -----------------------------
    print("\n" + "=" * 60)
    print("STEP 4 - Critic")
    print("=" * 60)

    feedback = critic_chain.invoke({
        "report": report
    })

    state["feedback"] = feedback

    print(feedback)

    return state


if __name__ == "__main__":

    topic = input("\nEnter Research Topic : ")

    run_research_pipeline(topic)