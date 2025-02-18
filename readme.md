# Assistant

This is a simple AI assistant that can be used to answer questions.

## Prerequisites

- Python 3.6 or higher
- OpenAI API key
- pip

## Setup

1. Clone the repository

```bash
git clone https://github.com/forjoa/assistant.git
```

2. Create a virtual environment 
```bash
python -m venv venv
```

3. Activate the virtual environment
    - Windows
    ```bash
    venv\Scripts\activate
    ```
    - Linux or Mac
    ```bash
    source venv/bin/activate
    ```

4. Install the dependencies 
```bash
pip install -r requirements.txt
```

5. Set the OpenAI API key as an environment variable

```bash
OPENAI_API_KEY=your_api_key
```

## Run the assistant
1. Start the assistant server with Streamlit
```bash
streamlit run app.py
```

2. Access the assistant at  the assistant at `localhost:8501`