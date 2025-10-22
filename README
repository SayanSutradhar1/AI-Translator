# AI Text Translator API

A FastAPI-based REST API service that provides text translation capabilities using Google Translate.

## Features

- Text translation to multiple languages
- Simple REST API interface
- Error handling and validation
- Asynchronous request processing

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
uvicorn app:app --reload
```

2. The server will start on `http://localhost:8000`

## API Endpoints

### GET /

Health check endpoint that returns "Server is running"

### POST /translate

Translates text to the specified target language.

**Request Body:**
```json
{
    "text": "Hello, world!",
    "target_language": "es"
}
```

**Response:**
```json
{
    "translated_text": "¡Hola Mundo!"
}
```

## Error Handling

The API returns appropriate error messages when:
- Translation service fails
- Invalid language codes are provided
- Required fields are missing

## Dependencies

- FastAPI - Web framework
- Uvicorn - ASGI server
- googletrans - Google Translate API wrapper

## License

This project is open source and available under the MIT License.