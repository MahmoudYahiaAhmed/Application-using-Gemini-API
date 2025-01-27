# Google API Text Generator with FastAPI

This FastAPI application provides an endpoint that allows users to generate text using the Google Generative AI API (Gemini-Pro). The app leverages the Google Generative AI to generate responses to user inputs.

## Features

- **API Endpoint:** Users can send a POST request with text and receive AI-generated responses.
- **Google Generative AI Integration:** The app is configured to use the Google Generative AI API to generate text responses.

## Prerequisites

Before you can run this app, make sure you have the following:

- Python 3.7 or higher
- FastAPI
- Google Generative AI Python Client Library
- A Google API Key with access to the Generative AI API

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project and add your Google API key.

   ```env
   Google_api_key=your_google_api_key
   ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

## Usage

To generate text using the API, send a POST request to the `/generate` endpoint with a JSON payload containing the text input.

Example request:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Your input text here"
}'
```

The response will contain the generated text from the Google Generative AI.
