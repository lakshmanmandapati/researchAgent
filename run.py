"""
Launch script for the Streamlit application
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import streamlit
        import crewai
        import dotenv
        print("✅ All required packages are available")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def check_env_vars():
    """Check if environment variables are set"""
    from dotenv import load_dotenv
    load_dotenv()
    
    required_vars = ["GEMINI_API_KEY", "TAVILY_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        print("Please set these in your .env file")
        return False
    
    print("✅ All environment variables are configured")
    return True

def main():
    """Main launch function"""
    print("🚀 Launching Synapse - AI Use Case Generator")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check environment
    if not check_env_vars():
        sys.exit(1)
    
    # Launch Streamlit
    print("🌐 Starting Streamlit application...")
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "main.py",
        "--server.address", "localhost",
        "--server.port", "8501",
        "--server.headless", "false"
    ])

if __name__ == "__main__":
    main()