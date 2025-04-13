from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import UMLRequest, UMLResponse
from groq_client import GroqUMLGenerator
from plantuml import convert_to_plantuml, generate_plantuml_url

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = GroqUMLGenerator()

@app.post("/generate-uml", response_model=UMLResponse)
async def generate_uml(request: UMLRequest):
    uml_data = generator.generate_uml(request.system_description)
    plantuml_code = convert_to_plantuml(uml_data)
    diagram_url = generate_plantuml_url(plantuml_code)
    return UMLResponse(
        plantuml_code=plantuml_code,
        diagram_url=diagram_url
    )