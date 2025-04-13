
def convert_to_plantuml(uml_text: str) -> str:
    """
    Convert to PlantUML with enhanced relationship support.
    Now handles:
    - Inheritance (<|--)
    - Associations (->, -->)
    - Composition (*--)
    - Aggregation (o--)
    """
    plantuml = "@startuml\n\n"
    plantuml += "skinparam class {\n"
    plantuml += "  BackgroundColor White\n"
    plantuml += "  BorderColor Black\n"
    plantuml += "  ArrowColor Black\n"
    plantuml += "}\n\n"
    
    current_class = None
    relationships = []

    for line in uml_text.splitlines():
        line = line.strip()
        if not line:
            continue
            
        # Class definition
        if line.endswith(":"):
            if current_class:
                plantuml += "}\n\n"
            current_class = line[:-1].strip()
            plantuml += f"class {current_class} {{\n"
            
        # Attributes
        elif line.startswith("- Attributes:"):
            attrs = line[len("- Attributes:"):].strip()
            if attrs:
                for attr in [a.strip() for a in attrs.split(",")]:
                    if attr:
                        plantuml += f"  {attr}\n"
        
        # Methods
        elif line.startswith("- Methods:"):
            methods = line[len("- Methods:"):].strip()
            if methods:
                for method in [m.strip() for m in methods.split(",")]:
                    if method:
                        if "(" not in method:
                            method = f"{method}()"
                        plantuml += f"  + {method}\n"
        
        # Relationships
        elif line.startswith("- Relationships:"):
            rels = line[len("- Relationships:"):].strip()
            if rels:
                for rel in [r.strip() for r in rels.split(",")]:
                    if rel and rel.startswith(("->", "<|--", "*--", "o--")):
                        relationships.append(f"{current_class} {rel}")

    # Close last class if exists
    if current_class:
        plantuml += "}\n\n"
    
    # Add all relationships
    for rel in relationships:
        plantuml += f"{rel}\n"
    
    plantuml += "\n@enduml"
    return plantuml

def generate_plantuml_url(plantuml_code: str) -> str:
    """
    Generate a PlantUML image URL from the code.
    Uses the PlantUML web server for rendering.
    """
    # Encode the diagram in PlantUML's special format
    import zlib
    import base64
    
    plantuml_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    
    def encode_6bit(b):
        return plantuml_alphabet[b & 0x3F]
    
    def append3bytes(b1, b2, b3):
        c1 = b1 >> 2
        c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
        c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
        c4 = b3 & 0x3F
        return encode_6bit(c1) + encode_6bit(c2) + encode_6bit(c3) + encode_6bit(c4)
    
    # Compress the PlantUML code
    compressed = zlib.compress(plantuml_code.encode('utf-8'))[2:-4]
    encoded = ""
    i = 0
    
    while i + 2 < len(compressed):
        encoded += append3bytes(compressed[i], compressed[i+1], compressed[i+2])
        i += 3
    
    # Handle remaining bytes
    if i < len(compressed):
        encoded += append3bytes(compressed[i], 0, 0)
    elif i + 1 < len(compressed):
        encoded += append3bytes(compressed[i], compressed[i+1], 0)
    
    return f"https://www.plantuml.com/plantuml/png/{encoded}"
