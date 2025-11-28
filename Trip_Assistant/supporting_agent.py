
#  import Libraries
from google.adk.agents import Agent
from Trip_Assistant.tools import google_search_grounding,location_search_tool
from google.adk.tools.agent_tool import AgentTool

# Define you model here..

LLM = "gemini-2.0-flash-001"
# Initialize your root agent 



News_Bot = Agent(
    model=LLM,
    name="News_Bot",
    description="Shares essential travel news and happenings, backed by fresh search data.",
    instruction="""
      Generate a maximum of 10 event and news recommendations tailored to the user’s query. All information should be sourced via the google_search_grounding search tool.
""",
    tools=[google_search_grounding]
)

Location_Bot= Agent(
    model=LLM,
    name="Location_Bot",
    description="Provides location suggestions based on what the user likes.",
    instruction="""
        Provide up to 10 place recommendations relevant to the user’s query. Each entry must include the place name, its location, and full address. Use the Location_tool to obtain coordinates and address information.
""",
    tools=[location_search_tool]
)

Trip_inspiration_agent = Agent(
    model=LLM,
    name="Trip_inspiration_agent",
    description="Provides perzsonalized travel ideas based on user preferences and may consult the News Bot and Location Bot for richer, up-to-date suggestions.",
    instruction="""
        - Understand the user’s travel preferences (budget, climate, duration, interests, travel style).
        - If information is missing, make smart assumptions.
        - Suggest curated destinations, themes, and unique experiences.
        - Keep recommendations short, creative, and practical.
        - Combine insights from both bots for richer suggestions.
        - Writing in an inspiring, friendly, and concise tone. 
        - Avoid giving too many options or generic suggestions.
        - Always tailor results if the user asks for something specific (solo travel, budget trip, adventure, etc.).
        - Ensure all suggestions are safe, culturally respectful, and relevant.
        - Provide 2–3 strong recommendations with short reasoning.
        - You will two two tools  `Location_Bot(inspiration query)' and News_Bot(inspiration query)` when appropirate:
        - Use `news_bot` to provide key events and news recommendations based on the user's query.
        - Use `places_bot` to provide a list of locations or nearby places to famous locations when user asks for it, for example "find hotels near eiffel tower", should return nearby hotels given some user preferences.
""",
    tools= [AgentTool(agent=News_Bot), AgentTool(agent=Location_Bot)]
)
