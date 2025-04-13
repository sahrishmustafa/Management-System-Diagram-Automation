import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GroqUMLGenerator:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "deepseek-r1-distill-llama-70b"
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def generate_uml(self, system_description: str) -> str:
        prompt = f"""You are a UML class diagram generator. Convert this system description into a detailed UML specification.

**Rules:**
1. ONLY output the UML specification in the EXACT format below
2. NEVER include any thinking process, reasoning, or explanations
3. NEVER include XML tags like <think> or </think>
4. ALWAYS follow this exact format for each class:

ClassName:
- Attributes: attr1: type, attr2: type
- Methods: method1(), method2(param: type)
- Relationships: -> OtherClass, <|-- ParentClass

**System Description:**
{system_description}

**Example Output:**
Doctor:
- Attributes: doctor_id: str, name: str, specialty: str
- Methods: add_availability(), view_schedule()
- Relationships: -> Appointment, <|-- Staff

Patient:
- Attributes: patient_id: str, name: str
- Methods: schedule_appointment()
- Relationships: -> Appointment

Now generate ONLY the UML specification for the given system:"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 700
        }

        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            content = response.json()['choices'][0]['message']['content']

            clean_output = []
            for line in content.splitlines():
                if not line.strip().startswith(('<', '(', '[')) and ':' in line:
                    clean_output.append(line)

            return "\n".join(clean_output)

        except requests.exceptions.RequestException as e:
            raise Exception(f"Groq API Request failed: {e}")
