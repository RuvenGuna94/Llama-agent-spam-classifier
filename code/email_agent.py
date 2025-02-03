# Import libraries
from langchain_community.llms import ollama
from crewai import Agent, Task, Crew, Process

# Init model
model = ollama(model = "llama3")

# Create Agents for an email classifier
# Specify email to classify
email = "Inheritance from Nigerian Prince!! Click to collect USD$10M."


# First agent receives email and second agent will write a response
# Create first agent
classifier = Agent(
    role = 'email classifier',
    goal = "Accurately classify emails based on their importance, give every email on of these ratings: Important, Casual or Spam."
    backstory = """Your only job is to classify emails. Do not hesitate to mark 
    emails as casual if they are deemed not important. Your job is to help the user manage their inbox"""
    verbose=True,
    allow_delegation=False,
    llm=model
)