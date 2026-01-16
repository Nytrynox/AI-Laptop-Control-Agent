# AgentOS - Autonomous Desktop Agent

## Overview
AgentOS is a vision-first autonomous agent capable of perceiving screen content and executing complex desktop tasks. By combining Vision-Language Models (VLM) with operating system accessibility APIs, it acts as a digital co-pilot for automating cross-application workflows.

## Features
-   **Vision Perception**: Uses LLaVA to "see" and understand the graphical user interface.
-   **Semantic Planning**: Decomposes high-level instructions into executable steps using Llama 3.
-   **Cross-App Control**: Seamlessly interacts with browsers, terminals, and file explorers.
-   **Privacy Focused**: Runs entirely locally with open-source models, ensuring data security.

## Technology Stack
-   **AI Core**: Llama 3.2 (Planning), LLaVA (Vision).
-   **Inference**: Ollama.
-   **OCR**: Tesseract.
-   **Automation**: PyAutoGUI, Playwright.

## Usage Flow
1.  **Command**: User provides a natural language goal (e.g., "Summarize the latest AI news").
2.  **Plan**: HostAgent breaks the goal into a sequence of actions.
3.  **Observe**: Vision system takes a screenshot to ground the next action.
4.  **Execute**: Agent controls the mouse/keyboard to perform the task.
5.  **Verify**: System checks the outcome and replans if necessary.

## Quick Start
```bash
# Clone the repository
git clone https://github.com/Nytrynox/AI-Laptop-Control-Agent.git

# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running with required models
ollama pull llama3.2
ollama pull llava:13b

# Start the agent CLI
python -m agentos.cli
```

## License
MIT License

## Author
**Karthik Idikuda**
