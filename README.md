# Research & Blog Crew - CrewAI + Ollama

A multi-agent AI system built with **CrewAI** that automatically researches 
a topic and writes a blog post using a **local LLM (llama3.2:3b via Ollama)** 

## Agents
- **Report Generator** - Researches the topic and creates a structured report
- **Blog Writer** - Converts the report into a simple, easy-to-read blog post

## Tech Stack
- CrewAI
- Ollama (llama3.2:3b)
- Python 3.13
- uv

## Run it
1. Install Ollama and pull the model: `ollama pull llama3.2:3b`
2. Install dependencies: `uv sync`
3. Add `.env` file with `OPENAI_API_KEY=NA`
4. Run: `crewai run`

Output is saved to `blogs/blog.md`

## Output
report task output:
<img width="1879" height="935" alt="report_task_output" src="https://github.com/user-attachments/assets/9aa60319-63d3-4954-9515-b7904bc5f6da" />

Blog task output:
<img width="1900" height="956" alt="blog_task_output" src="https://github.com/user-attachments/assets/ddf9e2bb-a258-4772-b3bf-ad4d132f643a" />

crew completion:
<img width="1879" height="943" alt="crew_completed" src="https://github.com/user-attachments/assets/f8206086-e459-4f5e-bad4-4445d6f66da1" />

