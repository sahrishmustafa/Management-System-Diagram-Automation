from pathlib import Path
from dotenv import load_dotenv
import os

# Try both possible paths
env_path1 = Path.cwd().parent / '.env'  # ../.env
env_path2 = Path.cwd() / '.env'         # ./.env

print(f"Trying path 1: {env_path1}")
load_dotenv(env_path1)
print("Key from path 1:", os.getenv("GROQ_API_KEY")[:5] + "..." if os.getenv("GROQ_API_KEY") else "NOT FOUND")

print(f"\nTrying path 2: {env_path2}")
load_dotenv(env_path2)
print("Key from path 2:", os.getenv("GROQ_API_KEY")[:5] + "..." if os.getenv("GROQ_API_KEY") else "NOT FOUND")