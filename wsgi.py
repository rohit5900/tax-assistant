from waitress import serve
from app import app
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Tax Assistant Buddy API on port {port}")
    serve(app, host='0.0.0.0', port=port) 