import os
import openai
import datetime
import random
from github import Github

# 🔐 API Keys from GitHub Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GH_TOKEN = os.getenv("GH_TOKEN_CUSTOM")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")

openai.api_key = OPENAI_API_KEY
github = Github(GH_TOKEN)
repo = github.get_repo(REPO_NAME)

# 🚀 Dopamine Trigger Prompts (Only for Addictive Tools)
dopamine_styles = [
    "insanely addictive tool that gives instant results and makes people come back daily",
    "satisfying animation-based interactive tool that gives pleasure in clicking and dragging",
    "dopamine-releasing, fast-response tool with sound/vibration feedback",
    "AI toy that gives unpredictable but interesting output every time",
    "a mysterious tool that reveals different answers every time, like fortune telling",
    "funny insult generator that feels like a game, people can’t stop clicking",
    "tool that makes user feel like they hacked the matrix",
    "visually hypnotic tool that responds to input in surprising ways",
    "AI-powered decision maker that always gives hilarious or shocking answers",
    "daily emotional check tool with weird AI mood output"
]

def generate_tool_code(style):
    prompt = f"""
    Create an ultra-viral, dopamine-triggering HTML+JS web tool based on the style: "{style}".
    Requirements:
    - Fully single-page tool (HTML+JS in one)
    - Insanely unique logic (don't reuse from past tools)
    - Add Google AdSense comment <!-- ADSENSE_HERE -->
    - Add JS function lockToolAfterLimit() to disable tool after 5 uses
    - Must feel satisfying, addictive or mysterious to use
    - Output ONLY full HTML with inline JS and CSS
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def extract_title_from_code(code):
    start = code.find("<title>")
    end = code.find("</title>")
    if start != -1 and end != -1:
        return code[start+7:end].strip().replace(" ", "_").replace("/", "-")
    else:
        return "dopamine_tool"

def push_to_github(code, tool_name):
    path = f"tools/{tool_name}.html"
    repo.create_file(path, f"Add tool: {tool_name}", code)

if __name__ == "__main__":
    try:
        print("🧠 Creating dopamine-driven AI assets...")

        for i in range(15):
            style = random.choice(dopamine_styles)
            tool_code = generate_tool_code(style)
            title = extract_title_from_code(tool_code)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            tool_filename = f"{title}_{timestamp}_{i+1}"
            push_to_github(tool_code, tool_filename)
            print(f"✅ Tool created: {tool_filename}.html")

        print("🎯 All 15 AI dopamine tools created & pushed!")

    except Exception as e:
        print(f"❌ Error: {e}")