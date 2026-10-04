# Azure Foundry LLM Practice

Small Python examples for sending prompts to an Azure AI Foundry model using the OpenAI Python SDK and LangChain.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)
- An Azure AI Foundry endpoint, a deployed model, and an API key

## Setup

From the project root, install the project dependencies:

```powershell
uv sync
```

Create `Chapter_1/.env` with the credentials and model settings for your Azure AI Foundry deployment:

```dotenv
API_KEY=your-api-key
model=your-model-or-deployment-name
base_url=https://your-resource.services.ai.azure.com/openai/v1
```

Use the endpoint and model/deployment name provided by your Azure AI Foundry resource. Keep `.env` private; it is ignored by Git. Never commit API keys. If a key has already been committed or exposed, rotate it in Azure and remove it from Git history before pushing.

## Examples

Run either example from the project root:

```powershell
uv run python Chapter_1/llm1.py
```

This example uses the OpenAI Python SDK's Responses API.

```powershell
uv run python Chapter_1/Langchainllm.py
```

This example uses LangChain's chat model interface and prints the response text from `AIMessage.content`.

Both examples load `API_KEY`, `model`, and `base_url` from `Chapter_1/.env`.

## Troubleshooting

- If you see a missing environment-variable error, check that `Chapter_1/.env` exists and that the variable names match exactly.
- If Azure returns an authentication or deployment error, verify the API key, endpoint URL, and model/deployment name in Azure AI Foundry.
- If `uv` is not recognized in PowerShell after installation, open a new terminal so it can pick up the updated PATH.
