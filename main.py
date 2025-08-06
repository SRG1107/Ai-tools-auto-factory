import openai
import datetime
import time
from github import Github
import random

# ✅ CONFIG SECTION
OPENAI_API_KEY = "sk-xxxxx"  # Add your OpenAI key
GH_TOKEN_SYSTEM = "ghp-xxxxx"  # Add your GitHub token
GITHUB_REPO_NAME = "srg1107/Ai-tools-auto-factory"  # Your repo

# ✅ INIT
openai.api_key = OPENAI_API_KEY
github = Github(GH_TOKEN_SYSTEM)
repo = github.get_repo(GITHUB_REPO_NAME)

# ✅ PROMPT: ULTRA VIRAL TOOL MAKER
def get_prompt():
    ideas = [
        "AI Mood Booster", "Insult Generator", "Motivational Quote Blaster",
        "Life Decision Coin Flip", "Stupid Idea Generator", "AI Roast Machine",
        "Deep Shower Thoughts", "Fake Hacker Terminal", "One-Click Excuse Maker",
        "Productivity Simulator", "Relationship Tester", "Crush Probability Meter",
        "Focus Timer", "Dream Decoder", "Emoji Translator"
    ]
    idea = random.choice(ideas)
    return f"""
    You are a top viral web tool creator. Build a 1-page dopamine-level addictive HTML+JS tool called **{idea}**.
    Rules:
    - Fully self-contained in 1 file (HTML + JS)
    - Add a title <h1> with tool name
    - UI should be funny, fast, and trigger emotional reaction
    - Add 5-use lockout using JS: function lockToolAfterLimit()
    - Add placeholder <!-- ADSENSE_HERE -->
    - No external libraries, use raw JS
    - Output only code. No explanation.
    """

# ✅ Generate code using GPT
def generate_tool_code(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ Error from GPT: {e}")
        return None

# ✅ Push to GitHub
def push_to_github(code, tool_name):
    path = f"tools/{tool_name}.html"
    try:
        repo.create_file(path, f"Add {tool_name}", code)
        print(f"✅ Pushed: {path}")
    except Exception as e:
        print(f"❌ GitHub push error: {e}")

# ✅ MAIN LOOP — 15 Tools per run
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
for i in range(1, 16):
    print(f"\n🚀 Creating Tool {i}/15")
    prompt = get_prompt()
    tool_code = generate_tool_code(prompt)
    if tool_code:
        tool_name = f"Tool_{timestamp}_{i}"
        push_to_github(tool_code, tool_name)
    time.sleep(5)  # Respect GPT rate limit