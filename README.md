
# BoomerToZoomer

Ever wanted to sound like those TikTok Stars? Boomer to Zoomer" combines a user-friendly web interface with a FastAPI backend and OpenAI integration to provide users with the ability to convert their messages into Gen Z slang. **Boomer to Zoomer Translator** is a web application that leverages OpenAI's language models to convert user-inputted text into Gen Z slang. 

## Table of Contents

- [Components](#components)
- [Functionality](#functionality)
- [Getting Started](#getting-started)
- [Usage](#usage)


## Components

The project comprises three main components:

1. **HTML Frontend**: The frontend interface is created using HTML, defining the structure of the web page. It includes a text area for user input, a translation button, and a result display area. Additionally, CSS styles and JavaScript are linked to enhance the user experience.

2. **FastAPI Backend**: The Python code uses the FastAPI framework to create a backend server. It integrates with OpenAI's language models to perform text translation. The server listens for POST requests on the '/process' endpoint, processes user input, and returns the translated result in JSON format. CORS (Cross-Origin Resource Sharing) is implemented to allow requests from specific origins.

3. **JavaScript for User Interaction**: JavaScript code waits for the document to load before attaching an event listener to the translation button. When the button is clicked, it collects the user's input, sends it to the FastAPI backend, and receives the translated response. The translated text is then displayed on the web page. Error handling is implemented to gracefully manage any issues.

## Functionality

The core functionality of Boomer to Zoomer Translator is to convert user-provided text into Gen Z slang. Here's how it works:

1. Users visit the web page and enter text into the provided text area.
2. After clicking the "Translate" button, the user input is sent to the FastAPI backend for processing.
3. The backend communicates with OpenAI's language model to translate the input into Gen Z slang.
4. The translated result is displayed on the web page for the user to see.

## Getting Started

To set up and run the Boomer to Zoomer Translator locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up an OpenAI API key and store it as an environment variable named `openai_key`.
4. Run the FastAPI server using `uvicorn main:app --host 0.0.0.0 --port 8000`.
5. Access the web application at `http://localhost:8000` in your web browser.

## Usage

1. Open the web application in your web browser.
2. Enter text into the text area that you want to translate into Gen Z slang.
3. Click the "Translate" button.
4. The translated result will be displayed on the web page.
