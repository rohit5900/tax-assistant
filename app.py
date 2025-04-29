from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import google.generativeai as genai
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY not found in environment variables")
    raise ValueError("GOOGLE_API_KEY environment variable is required")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Tax context prompt to guide the model
TAX_CONTEXT = """You are a knowledgeable tax assistant who helps people with tax-related queries. 
Focus on providing accurate, helpful information about:
- Income tax calculations and rules
- Tax deductions and exemptions
- GST (Goods and Services Tax)
- Tax filing procedures and deadlines
- PAN card and other tax-related documents
- TDS (Tax Deducted at Source)
- Tax refunds and returns
- Capital gains tax
- HRA and other salary components
Keep responses concise, accurate, and easy to understand. Focus on Indian taxation system."""

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data:
            logger.warning("Received empty request body")
            return jsonify({"error": "Request body is required"}), 400
            
        user_message = data.get('message', '')
        
        if not user_message:
            logger.warning("Received empty message")
            return jsonify({"error": "No message provided"}), 400

        logger.info(f"Received query: {user_message}")
        
        # Combine context and user query
        prompt = f"{TAX_CONTEXT}\n\nUser Query: {user_message}\n\nResponse:"
        
        # Generate response using Gemini
        response = model.generate_content(prompt)
        
        # Extract and clean the response text
        response_text = response.text.strip()
        logger.info("Successfully generated response")
        
        return jsonify({"response": response_text})
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        return jsonify({"error": "An error occurred while processing your request"}), 500

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    # Use environment variable if available, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Use environment variable if available, otherwise default to False
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Tax Assistant Buddy API on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug) 