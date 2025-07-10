# Baios
Basic AI Operating System - Business Agent Integration Operating System

# Motivation
Middleware to run context engineering agentic workflows.
Most importantly it should manage and share the **context** across the agents.

# Requirements
POC implemented using BPMN and Python:
* https://bpmn.io/ (just to review bpmn xml visually)
* https://pypi.org/project/SpiffWorkflow/ (current framework)
* enterprise example: https://camunda.com/

Workflow
---

```
GamePocGenerator: Start->TaskStoryLine->End

TaskStoryLine: use openai api model o3-deep-research prompt:
We need simple common well-played game ideas. Single player preferred, but surprise me sometimes with 2+ player ones.
The game must be a known one so the rules should well understood, maybe clarify any variation of the game rules.
Name the game, describe the setting, the vibe, the atmosphere. If applicable give use a touch of the protagonist/antagonist, heroine, challenge, gear etc. Would be nice if the actual player could have a connection with the goals of the game.  
Generate a short one paragraph idea that outlines such a game! Include everything needed for a crisp requirement. Do not go into technologies or technical analysis, no integration. Focus on the core idea of a popular game.
(Each idea will be fed to ai code generators which produce poc mini games. Keep it simple. Because this is in an agentic workflow: use your powers to pass necessary specifications to image generating and source code generating agent.)
"
```

# Design Considerations
For example use Google ADK for the actual "hypervisor". You have to implement/load an agent for execution.
The "user process" will be the agent(s) executing.

# Architecture
use Mermaid here

# Future plans
1. Error handling, logging across agents
1. Implement pluggable, discoverable task toolsets (initialize model(s) connectio(s), tools, mcp servers etc.)
1. Context partitioning, context security
1. Tools filters, tool repositories 
