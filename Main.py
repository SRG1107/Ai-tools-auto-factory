import openai
import datetime
from github import Github
import os

openai.api_key = os.environ["openai.api_key"]

def generate_tool_code():
    prompt = f"""
    You are a super-intelligent AI who builds viral web tools.
    Create a useful, unique, 1-page HTML/JS web tool with:
    - Clean UI
    - Google AdSense embed (dummy code)
    - Lock tool after 5 uses
    Output full HTML+JS in <html> format.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def push_to_github(repl_name, code):
    g = Github(os.environ["GITHUB_TOKEN"])
    repo = g.get_user().get_repo("Ai-tools-auto-factory")
    filename = f"tools/{repl_name}.html"
    repo.create_file(filename, "Add AI tool", code)

repl_name = f"tool_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}"
code = generate_tool_code()
push_to_github(repl_name, code)
