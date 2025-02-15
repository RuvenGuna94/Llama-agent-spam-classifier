# Import libraries
import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

# Init model
llm = LLM(model="groq/llama-3.3-70b-versatile")

# Create Agents for an email classifier
# Specify email to classify
email = "Meeting timing changed tomorrow from 9am to 3pm."


# First agent receives email and second agent will write a response
# Create first agent
classifier = Agent(
    role = 'email classifier',
    goal = """Accurately classify emails based on their importance, give every email on of these ratings: Important, Casual or Spam.""",
    backstory = """Your only job is to classify emails. Do not hesitate to mark 
    emails as casual if they are deemed not important. Your job is to help the user manage their inbox""",
    verbose=True,
    llm=llm, # LLM that powers the agent
    allow_delegation=False
)

# Create second agent. allow_delegation should be set to True.
responder = Agent(
    role = 'email responder',
    goal = """based on the importance of the email, write a concise and simple response.
    If the email is rated 'important', use a formal tone. If it is 'casual' use a casual tone and if it is 'spam' 
    ignore the email.""",
    backstory = """Your only job is to write short responses to emails based on their importance. The importance 
    will be provided to you by the 'classifier' agent.""",
    verbose=True,
    llm=llm, # LLM that powers the agent
    allow_delegation=True
)

# Next, we give the agents their tasks. 
# Task for Classifier agent
classify_email = Task(
    description=f"classify the following email: {email}",
    agent=classifier,
    expected_output="One of these three options: 'important', 'casual' or 'spam'."
)

# Task for Responder agent
respond_to_email = Task(
    description=f"Respond to the email: {email}",
    agent=responder,
    expected_output="A short response to the email"
)

# Define the Crew
crew = Crew(
    agents=[classifier, responder],
    tasks = [classify_email, respond_to_email],
    verbose=True,
    process=Process.sequential

)

Output = crew.kickoff()