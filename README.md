# Amigo Chat Bot API

## Overview
This document outlines the backend architecture of the Amigo Chat Bot API,
developed with FastAPI, OpenAI, and integrated with Swagger UI for easy interaction.
It serves as a guide for setup, deployment, and understands the codebase's structure and features.

## Project Arhitecture
- FastAPI: A modern, fast (high performance) web framework for building APIs with Python.
- OpenAI Integration: Utilizes OpenAI's powerful language models for generating chat responses.
- Swagger UI: Provides interactive API documentation through Swagger/OpenAPI.

## Prerequisites
- Python 3.7 or higher
- OpenAI API Key (Get yours from OpenAI's platform)
- Docker (for containerization, optional)

## Getting Started
### Installation
1. Clone the repository: `git clone repository-url`
2. Navigate to the project directory: `cd project-directory`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file and add your OpenAI API key:
    OPEN_AI_API_KEY=your-api-key-goes-here
5. Build the Docker image (optional): `docker build -t amigo-chat-api .`
6. Run the Docker container (optional): `docker run -d -p 80:80 amigo-chat-api`

### Running the application
- Start the application: `uvicorn main:app --host 0.0.0.0 --port 8080`
- Access Swagger UI: `http://localhost:8080/docs`

## Features
- **User Interaction**: Accepts user messages via HTTP POST requests and generates chat responses.
- **OpenAI Chat**: Utilizes OpenAI's language models to provide human-like responses to user queries.
- **Swagger Documentation**: Interactive API documentation accessible at `/docs` endpoint for testing and exploration.

## Environmental Variables
OPEN_AI_API_KEY: Your OpenAI API key for accessing the language model.

## Acknowledgments
FastAPI: https://fastapi.tiangolo.com/
OpenAI API: https://beta.openai.com/docs/
Swagger UI: https://swagger.io/tools/swagger-ui/