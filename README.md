# Tax Assistant Buddy

A modern web-based AI chatbot for tax-related queries.

## Features

- Clean and modern user interface
- Real-time chat functionality
- Responsive design for all devices
- Easy integration with Flask backend API

## Setup Instructions

1. Make sure you have Python installed on your system
2. Install the required Python packages:
   ```bash
   pip install flask flask-cors
   ```

3. Start your Flask backend server (make sure it's running on port 5000)
4. Open the `index.html` file in your web browser or serve it using a local web server

## Project Structure

- `index.html` - Main HTML file containing the chat interface
- `styles.css` - CSS styles for the application
- `script.js` - JavaScript code for handling chat functionality
- `README.md` - This documentation file

## API Integration

The frontend is configured to communicate with a Flask backend API at `http://localhost:5000/api/chat`. Make sure your Flask API:

1. Accepts POST requests at the `/api/chat` endpoint
2. Expects JSON data in the format: `{ "message": "user message here" }`
3. Returns JSON response in the format: `{ "response": "bot response here" }`

## Customization

You can customize the application by:

1. Modifying the colors in `styles.css`
2. Changing the API endpoint in `script.js`
3. Adding additional features to the chat interface

## License

This project is open source and available for personal and commercial use. 