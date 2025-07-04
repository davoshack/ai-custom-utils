# Add your utilities or helper functions to this file.

import os
import html
from dotenv import load_dotenv, find_dotenv
from IPython.display import display, Markdown, HTML

def load_env():
    _ = load_dotenv(find_dotenv())

class Display_Helper: 

    def wrap(self, long_string):
        escaped_string = html.escape(long_string)
        html_string = escaped_string.replace("\n", "<br>")
        display(HTML(f"<div style='width: 600px; word-wrap: break-word;'>{html_string}</div>"))

    def text_file(self, file_path):
        try:
            # Open the file and read its contents into a string
            with open(file_path, 'r', encoding='utf-8') as file:
                text_string = file.read()

            # Print the contents (optional)
            print(f"{file_path}:")
            self.wrap(text_string)

        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_gemini_api_key():
    load_env()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    return gemini_api_key

def get_activeloop_api_key():
    load_env()
    activeloop_api_key = os.getenv("ACTIVELOOP_TOKEN")
    return activeloop_api_key

def get_cohere_api_key():
    load_env()
    cohere_api_key = os.getenv("COHERE_API_KEY")
    return cohere_api_key

def get_eleven_api_key():
    load_env()
    eleven_api_key = os.getenv("ELEVEN_API_KEY")
    return eleven_api_key

def get_livekit_api_key():
    load_env()
    livekit_api_key = os.getenv("LIVEKIT_API_KEY")
    return livekit_api_key

def get_anthropic_api_key():
    load_env()
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    return anthropic_api_key

def get_deepgram_api_key():
    load_env()
    deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")
    return deepgram_api_key

def get_groq_api_key():
    load_env()
    groq_api_key = os.getenv("GROQ_API_KEY")
    return groq_api_key

def get_langchain_api_key():
    load_env()
    langchain_endpoint = os.getenv("LANGCHAIN_API_KEY")
    return langchain_endpoint

def get_langchain_tracing_v2():
    load_env()
    langchain_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2")
    return langchain_tracing_v2

def get_langchain_endpoint():
    load_env()
    langchain_endpoint = os.getenv("LANGCHAIN_ENDPOINT")
    return langchain_endpoint

def get_langchain_project():
    load_env()
    langchain_project = os.getenv("LANGCHAIN_PROJECT")
    return langchain_project

def get_google_api_key():
    load_env()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    return google_api_key

def get_google_cse_id():
    load_env()
    google_cse_id = os.getenv("GOOGLE_CSE_ID")
    return google_cse_id

def get_trello_api_key():
    load_env()
    trello_api_key = os.getenv("TRELLO_API_KEY")
    return trello_api_key

def get_trello_api_secret():
    load_env()
    trello_api_secret = os.getenv("TRELLO_API_SECRET")
    return trello_api_secret
   
def get_trello_board_id():
    load_env()
    trello_board_id = os.getenv("TRELLO_BOARD_ID")
    return trello_board_id 

def get_serper_api_key():
    load_env()
    serper_api_key = os.getenv("SERPER_API_KEY")
    return serper_api_key

def get_mlflow_tracking_uri():
    load_dotenv()
    mlflow_tracking_uri = os.getenv("DLAI_LOCAL_URL")
    return mlflow_tracking_uri

def get_huggingface_api_key():
    load_env()
    hf_api_key = os.getenv("HUGGINGFACE_API_KEY")
    return hf_api_key
   
def get_e2b_api_key(): 
    load_env()
    e2b_api_key = os.getenv("E2B_API_KEY")
    return e2b_api_key

def get_llama_api_key():
    load_env()
    llama_api_key = os.getenv("LLAMA_API_KEY")
    return llama_api_key

def get_llama_base_url():
    load_env()
    llama_base_url = os.getenv("LLAMA_BASE_URL")
    return llama_base_url

def get_together_api_key():
    load_env()
    together_api_key = os.getenv("TOGETHER_API_KEY")
    return together_api_key

def get_github_api_key():
    load_env()
    github_api_key = os.getenv("GITHUB_API_KEY")
    return github_api_key

def print_response(text):
    display(Markdown(text))