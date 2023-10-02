# BoomerToZoomer

Ever wanted to sound like those TikTok Stars? Boomer to Zoomer" combines a user-friendly web interface with a FastAPI backend and OpenAI integration to provide users with the ability to convert their messages into Gen Z slang. 

# features
HTML Frontend: The HTML code defines the structure of the web page, providing a user interface for input and display. It includes a text area for users to enter text, a button to trigger the translation process, and a result paragraph to display the translated text. 

FastAPI Backend: The Python code utilizes the FastAPI framework to create a backend server. It incorporates OpenAI for text translation. The server listens for POST requests on the '/process' endpoint, processes the user's input, and sends back the translated result in JSON format. It also implements CORS (Cross-Origin Resource Sharing) to allow requests from specified origins.

JavaScript for User Interaction: This JavaScript code waits for the document to load before attaching an event listener to the submit button. When the button is clicked, it fetches the user's input, sends it to the FastAPI backend, and receives the translated response. The translated text is then displayed on the web page. 

