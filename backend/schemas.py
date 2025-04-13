from pydantic import BaseModel

class UMLRequest(BaseModel):
    system_description: str

class UMLResponse(BaseModel):
    plantuml_code: str
    diagram_url: str