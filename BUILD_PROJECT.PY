import os

# Define the project directory structure and files
project_structure = {
    "market_dash": [
        "README.md",
        "docker-compose.yml",
        "Dockerfile"
    ],
    "market_dash/frontend": [
        "index.html"
    ],
    "market_dash/backend": [
        "requirements.txt",
        "main.py"
    ],
    "market_dash/backend/services": [
        "__init__.py",
        "market_data.py",
        "cache_service.py"
    ],
    "market_dash/backend/analysis": [
        "__init__.py",
        "indicators.py",
        "scoring.py",
        "report_engine.py",
        "router.py"
    ]
}

def build_project():
    print("🚀 Building Kite Lite project structure...")
    
    for folder, files in project_structure.items():
        # Create directories
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Created folder: {folder}")
        
        # Create empty files inside the directories
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'w') as f:
                # Add a quick comment at the top of Python files
                if file.endswith('.py'):
                    f.write(f"# {file} - Paste your code here\n")
            print(f"   📄 Created file: {file}")
            
    print("\n✅ Project structure built successfully! You can now paste the code into the files.")

if __name__ == "__main__":
    build_project()