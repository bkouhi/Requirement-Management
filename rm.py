import os
os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

from crewai import Agent
from crewai_tools import SerperDevTool, BrowserbaseTool, ExaSearchTool
search_tool = SerperDevTool()
browser_tool = BrowserbaseTool()
exa_search_tool = ExaSearchTool()

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
  role='Senior Researcher',
  goal='Uncover groundbreaking technologies in {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could change"
    "the world."
  ),
  tools=[search_tool, browser_tool],
)

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[exa_search_tool],
  allow_delegation=False
)

# Setting a specific manager agent
manager = Agent(
  role='Manager',
  goal='Ensure the smooth operation and coordination of the team',
  verbose=True,
  backstory=(
    "As a seasoned project manager, you excel in organizing"
    "tasks, managing timelines, and ensuring the team stays on track."
  )
)