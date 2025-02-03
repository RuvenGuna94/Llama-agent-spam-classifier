# Import libraries
from langchain_community.llms import ollama
from crewai import Agent, Task, Crew, Process

# Init model
model = ollama(model = "llama3")

# Create Agents for an email classifier
# Specify email to classify
email = "Inheritance from Nigerian Prince!! Click to collect USD$10M."


# First agent receives email and second agent will write a response
