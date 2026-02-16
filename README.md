📋 Strategic Intelligence PoC: Executive Narrative Generator
This application is a Contextual Intelligence Proof of Concept designed to transform raw document submissions into high-impact strategic reports. It uses a multi-agent AI system to analyze PDFs, conduct structured interviews, and synthesize findings into an executive PowerPoint presentation.

🚀 Workflow Overview
Inbox: Approve pending documents. The Architect Agent reads the PDF to generate document-specific discovery questions.

Conversation: Conduct a 10-question interview. This phase combines a structured "Fundamentals Form" with a dynamic chat loop powered by an Interviewer Agent that nudges for high-quality responses.

Designer Agent: Once the interview is complete, the system automatically builds a 5-slide PowerPoint deck.

Tracker: Monitor the status of all submissions and download the final reports.

📂 Repository Structure
app.py: Main entry point and navigation.

pages/: Contains the three main workflow stages (Inbox, Conversation, Tracker).

agents_logic.py: Core AI logic and Agent configurations.

architect_utils.py: PDF processing and initial question generation.

designer_utils.py: PowerPoint generation and narrative synthesis.

database.py: SQLite management for persistence.

style.css: Custom UI styling for the Streamlit interface.

🛠️ Setup & Local Installation
Since Docker is prohibited in this environment, follow these steps to run the application on a central server:

1. Requirements
Python 3.10+

OpenAI API Key (Configured as an environment variable)

2. Installation
Clone or download this repository to the server.

Create a virtual environment:

Bash
python -m venv venv
Activate the environment:

Windows: .\venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies:

Bash
pip install -r requirements.txt
3. Configuration (.env)
Create a .env file in the root directory and add your key:

Plaintext
OPENAI_API_KEY=sk-your-key-here
4. Launch
To make the app accessible to others on the network, run:

Bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
🛡️ Security & Privacy
Data Persistence: All data is stored in a local submissions.db file.

Compliance: The final PowerPoint includes a GenAI disclaimer stating: "The PowerPoint was made by GenAI but based in the responses provided by the user."

Narrative Integrity: The AI story generator is strictly instructed to use only facts provided during the interview without adding external data.
