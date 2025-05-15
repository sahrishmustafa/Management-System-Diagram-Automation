# UML Diagram Generator with Groq & Streamlit

A system that converts natural language descriptions into UML class diagrams using Groq's LLM API and displays them via a Streamlit interface.

## Features

- 🚀 Natural Language to UML conversion
- 🌐 Real-time PlantUML rendering
- 🔄 Auto-detection of classes, attributes, methods, and relationships
- 🛠️ Error correction and validation layer
- 📱 Responsive web interface

## Technologies

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **AI Provider**: Groq (Llama-3-70B)
- **UML Rendering**: PlantUML
- **Environment**: Python 3.10+

## Installation

### Prerequisites
- Python 3.10+
- Groq API Key (free tier available)

### Setup

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/uml-generator.git
cd uml-generator

2. Create Virtual Environment
``` bash
python -m venv .venv
```

3. Activate Environment
``` bash
# Windows
.\.venv\Scripts\activate
```

4. Install Dependencies
``` bash
pip install -r requirements.txt
```

5. Configure Environment
``` bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

## Usage

### Running 
1. Start Backend API
``` bash
cd backend
uvicorn main:app --reload
```

2. Start Frontend UI
``` bash
cd frontend
streamlit run app.py
```

### Example Inputs
Try these system descriptions:
- "Library system with books, members, and loans"
- "E-commerce platform with products, customers, and orders"
- "Hospital management system with doctors, patients, and appointments"

## Project Structure
```
uml-generator/
├── .env
├── .venv/
├── backend/
│   ├── main.py         # FastAPI server
│   ├── groq_client.py  # LLM interface
│   ├── plantuml.py     # UML conversion
│   └── schemas.py      # Data models
├── frontend/
│   └── app.py          # Streamlit UI
├── requirements.txt
└── README.md
```