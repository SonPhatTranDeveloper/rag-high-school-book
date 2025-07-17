from dotenv import load_dotenv

from src.workflow.agent import create_agentic_workflow

if __name__ == "__main__":
    load_dotenv()
    workflow = create_agentic_workflow()
