# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv
from openai import OpenAI
import os 


client =OpenAI(
    base_url="https://learning890ai.services.ai.azure.com/api/projects/FoundryProject/openai/v1",
    api_key=os.getenv("speech_key"),
)

# endpoint = "https://learning890ai.services.ai.azure.com/api/projects/proj-default"

# project_client = AIProjectClient(
#     endpoint=endpoint,
#     credential=DefaultAzureCredential(),
# )

my_agent = "busy-agent-lkk2gtqdwf"
my_version = "2"

# openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = client.responses.create(
    input=[{"role": "user", "content": "Tell me what you can help with."}],
    extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")