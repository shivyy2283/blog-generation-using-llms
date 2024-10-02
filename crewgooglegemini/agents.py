from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",  # or "gemini-1.0-pro" if that's the correct model name
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating a senior researcher agent
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=("Driven by curiosity, you're at the forefront of"
               "innovation, eager to explore and share knowledge that could change"
               "the world."),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
    max_iterations=10,  # Increase this value
    max_execution_time=300  # Time in seconds, adjust as needed
)

# Creating a writer agent
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)