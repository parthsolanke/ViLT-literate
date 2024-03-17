# ViLT-literate
FastAPI App for ViLT: Vision-and-Language Transformer 👁️

This repository contains code for an application built with FastAPI for answering questions related to images. It uses a pre-trained model to perform question-answering tasks on images.

## Features

- Allows users to upload an image and input a question.
- Utilizes a pre-trained model to predict the answer based on the provided image and question.
- Provides a simple and intuitive user interface.

## Setup

### Prerequisites

- Python (version 3.9.9 recommended)
- Docker (if running the app in a containerized environment)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

#### Locally

To run the server locally, execute:

```bash
python server.py
```

To run the app locally, execute:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to access the application.

#### Using Docker

To run the app using Docker, build the Docker image and run a container:

```bash
docker build -t image-qa-app .
docker run -d -p 8000:8000 image-qa-app
```

The app will be accessible at `http://localhost:8000`.

## Usage

1. Upload an image by clicking the "Upload Image" button.
2. Enter your question in the text input box provided.
3. Click the "Get Answer" button to receive the predicted answer.

## License

[MIT License](LICENSE)