# Azure Foundry Practice

Python examples for Azure AI Foundry models, Azure AI services, and speech recognition.

## Project Structure

- `Chapter_1(Models)/llm1.py`: calls an Azure AI Foundry model with the OpenAI Responses API.
- `Chapter_1(Models)/Langchainllm.py`: calls a model through LangChain.
- `Chapter_2(AI Services)/invoice.py`: analyzes a local document with the prebuilt invoice analyzer.
- `Chapter_2(AI Services)/ocr.py`: analyzes a document URL with the prebuilt layout analyzer.
- `Chapter_2(AI Services)/STT.py`: performs continuous speech recognition from the default microphone.
- `Chapter_3(Agents)/foundry_agent.py`: sample call to a Foundry agent.
- `Sample_Data/`: sample documents, including `Employee-Handbook.pdf`.

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)
- Azure resources and credentials for the examples you want to run

Install the dependencies declared in the project:

```powershell
uv sync
```

The invoice, OCR, and agent examples also import Azure SDK packages that are not currently declared in `pyproject.toml`. Add them before running those examples:

```powershell
uv add azure-ai-contentunderstanding azure-identity azure-ai-projects
```

## Configuration

Create a `.env` file in the repository root. `load_dotenv()` in the examples reads this file when commands are run from the project root.

```dotenv
# Azure AI Foundry model examples
API_KEY=your-api-key
model=your-model-or-deployment-name
base_url=https://your-resource.services.ai.azure.com/openai/v1

# Azure AI Content Understanding examples
ai_service=https://your-content-understanding-resource.cognitiveservices.azure.com/
file_path=../Sample_Data/Employee-Handbook.pdf
file_url=https://example.com/document.pdf

# Azure Speech example
AZURE_SPEECH_KEY=your-speech-key
AZURE_SPEECH_REGION=your-resource-region
```

Replace each value with settings from your Azure resource. `file_url` must point to a document the service can access. The invoice example expects a local invoice document; update `file_path` to its path before running it. When run from the repository root, the OCR and invoice examples write `result.json` and `result_invoice.json` to the repository root.

Keep `.env` private; it is ignored by Git. Never commit API keys. If a key has already been committed or exposed, rotate it in Azure and remove it from Git history before pushing.

## Run Examples

Run commands from the repository root:

```powershell
uv run python "Chapter_1(Models)/llm1.py"
uv run python "Chapter_1(Models)/Langchainllm.py"
uv run python "Chapter_2(AI Services)/invoice.py"
uv run python "Chapter_2(AI Services)/ocr.py"
uv run python "Chapter_2(AI Services)/STT.py"
```

The speech example listens through the default microphone until you press Enter.

The agent example currently contains a hard-coded project endpoint and agent name/version, and reads its API key from the `speech_key` environment variable. Update those values for your Foundry project before running it; it does not currently load `.env` itself.

## Troubleshooting

- For missing environment-variable errors, confirm `.env` is in the repository root and that names match exactly.
- For Azure authentication or deployment errors, verify the resource endpoint, key, region, and model or analyzer configuration.
- If `uv` is not recognized in PowerShell after installation, open a new terminal so it can pick up the updated PATH.
