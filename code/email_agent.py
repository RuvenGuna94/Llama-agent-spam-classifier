# Import libraries
from langchain_community.llms import ollama
from crewai import Agent, Task, Crew, Process

# Init model
model = ollama(model = "llama3")

