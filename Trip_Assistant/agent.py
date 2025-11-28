
#  import Libraries
from google.adk.agents import Agent
from Trip_Assistant.supporting_agent import Trip_inspiration_agent

# Define you model here..

LLM = "gemini-2.0-flash-001"
# Initialize your root agent 

root_agent = Agent(
    model=LLM,
    name="Trip_Assistant_main",
    description="A helpful trip planning assistant that helps user plan their trip by providing information and suggestions based on their preference. ",
    instruction="""
        - You are an exclusive trip concierge agent
        - You help user to dicover their dream holiday destination and plan their vacation. 
        - Use the Trip_inspiration_agent to get the best destination , news, Location nearby e.g. hotels, cafes, etc near attraction and pointsof instrest for the user. 
        - You cannot use any tool directly. 
""",
    sub_agents= [Trip_inspiration_agent]

)