# Llama-Agent Spam Classifier

## Overview
This project utilizes CrewAI to classify incoming emails and generate appropriate responses based on their importance. It employs a two-agent system powered by the **Llama-3.3-70B-Versatile** model via **Groq** API.

## Features
- **Email Classification:** Assigns emails one of three categories: **Important, Casual, or Spam**.
- **Automated Responses:** Generates appropriate responses based on classification.
  - **Important Emails:** Formal response.
  - **Casual Emails:** Informal response.
  - **Spam Emails:** Ignored.
- **Multi-Agent Collaboration:** Uses CrewAI framework to coordinate tasks between agents.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/RuvenGuna94/Llama-agent-spam-classifier.git
   cd Llama-agent-spam-classifier
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following line to it:
     ```plaintext
     GROQ_API_KEY=your_api_key_here
     ```

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. The agents will classify an email and generate a response accordingly.

## Code Structure
- `email_agent.py`: Core script defining agents and their tasks.
- `.env`: Stores environment variables.
- `requirements.txt`: Lists dependencies.

## Example Output
```
Agent: Email Classifier
Classification: Casual

Agent: Email Responder
Response: "Noted! Thanks for the update."
```

## Technologies Used
- **CrewAI**: Agent-based workflow framework
- **Llama 3**: Large language model from Groq
- **Python**: Primary programming language

## Future Improvements
- Extend classification to include more categories.
- Integrate with an email API (e.g., Gmail API) for real-time processing.
- Store classified emails in a database.

## License
This project is licensed under the MIT License.

## Author
[RuvenGuna94](https://github.com/RuvenGuna94)
