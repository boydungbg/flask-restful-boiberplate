from dotenv import load_dotenv
from app import create_app
from config.app import AppConfig

load_dotenv()

app = create_app()

@app.cli.command("test")
def test():
    """Run test for app"""
    print("Run test here")
    

if __name__ == "__main__":
    is_debug = True
    if AppConfig.app_development == "true":
        is_debug = True
    else:
        is_debug = False
    app.run(debug=is_debug, port=int(AppConfig.app_port))