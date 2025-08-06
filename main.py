# ✅ AI Tool Generator — GitHub Pages Version (No Replit)
import os
import openai
import datetime
from github import Github

# 🔐 API Keys from GitHub Secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GH_TOKEN = os.getenv("GH_TOKEN_SYSTEM")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")  # example: "username/ai-tools-auto-factory"

# ✅ Step 1: Generate Web Tool Code from GPT-4o
def generate_tool_code():
    prompt = """
    You are a viral AI web tool creator.
    Generate a unique, useful/fun one-page HTML+JS tool with:
    - Clean UI (no CSS file, only inline)
    - AdSense placeholder comment <!-- ADSENSE_HERE -->
    - lockToolAfterLimit() JS function (locks after 5 uses)
    Return full code (HTML+JS) inside one <html> file.
    """
    openai.api_key = OPENAI_API_KEY
    res = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']

# ✅ Step 2: Save tool to GitHub as new file in /tools/
def push_to_github(tool_code, tool_name):
    g = Github(GH_TOKEN)
    repo = g.get_repo(REPO_NAME)
    path = f"tools/{tool_name}.html"
    repo.create_file(path, f"🔧 Added tool {tool_name}", tool_code)

# ✅ MAIN EXECUTION
if __name__ == "__main__":
    try:
        print("🎯 Starting AI Tool Generator...")
        tool_code = generate_tool_code()
        tool_name = "tool_" + datetime.datetime.now().strftime("%Y%m%d_%H%M")

        print("📁 Saving tool to GitHub repo...")
        push_to_github(tool_code, tool_name)

        print(f"✅ Tool created and saved: tools/{tool_name}.html")

    except Exception as e:
        print(f"❌ ERROR: {e}")
