# baiOS
Basic AI Operating System

# Motivation
Middleware for the ai minded development, an extendible platform you can bootstrap on the edge.
Mimicking how a machine boots up, this is a BIOS/hypervisor for your ai minded engineering.

BAIOS will initialize model(s) connectio(s), tools, mcp servers etc., then hand over to your ai kernel. 

# Requirements

Example boot order:
1. POWERON: we are bootstrapping a single thread python main process with configuration
1. INIT: we initiate "hardware" e.g. run ollama gemma3:latest model, start databases for memory etc.
1. POST: see if all hardware has come up, wait for all to load
1. BOOT: boot options inclde ollama, openai, agent (see below) etc.

# Design Considerations
For example use Google ADK for the actual "hypervisor". You have to implement/load an agent for execution.
The "user process" will be the agent(s) executing.

# Architecture
use Mermaid here

# Future plans
Consider a future configuration cli console app for "bios-menu" to configure the setup.
