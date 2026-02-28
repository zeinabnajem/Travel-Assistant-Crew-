# Travelassistant Crew

Welcome to the **TravelAssistant Crew** project, powered by [crewAI](https://crewai.com).
This project demonstrates how to build a **multi-agent AI travel assistant** where specialized agents collaborate to help users:
- ✈️ Find flight options  
- 🏨 Suggest hotels  
- 🗺️ Plan personalized tours  
- 💡 Provide expert travel advice  
The system is modular, extensible, and ready to integrate with real-world APIs.

# 🧠 Multi-Agent Architecture

The TravelAssistant Crew includes four specialized agents:

### ✈️ Flight Agent
Recommends flights based on user preferences (currently using dummy data).

### 🏨 Hotel Agent
Suggests accommodations with amenities, location details, and pricing.

### 🗺️ Tour Agent
Creates personalized tour itineraries tailored to the destination.

### 💡 Advisor Agent
Provides cultural insights, travel tips, and useful recommendations.

Each agent has:
- A defined **role**
- A clear **goal**
- A detailed **backstory**
- Assigned **tasks**

All configurations are defined in YAML files.



## Installation

Ensure you have:

- Python >= 3.10 and < 3.14

```bash
pip install -r requirements.txt
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/travelassistant/config/agents.yaml` to define your agents
- Modify `src/travelassistant/config/tasks.yaml` to define your tasks
- Modify `src/travelassistant/crew.py` to add your own logic, tools and specific args
- Modify `src/travelassistant/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the TravelAssistant Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.


- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
