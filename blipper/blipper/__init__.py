import json, requests
from . import _config
from ._config import BLIPPER_AUTH_URL


def print_invalid_api_key():
    print("Invalid API key")

class Blipper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = _config.blipper_url
        self.headers = {"api_key_header": api_key}
        self.authenticated, self.user = self.verify_api_key()

    def getStatus(self, apikey):
        data = {"key": apikey}
        response = requests.post(BLIPPER_AUTH_URL, json=data)
        return json.loads(response.content)

    def verify_api_key(self):
        response = self.getStatus(self.api_key)
        is_valid = True if response['status'] == 1 else False
        user_id = response['client_id']
        return is_valid, user_id

    def categorizeSingleCategory(self, text, categories):
        if self.authenticated:
            data = {
            'text': text,
            'categories': categories
            }
            response = requests.post(_config.blipper_url + "categorizeSingleCategory", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def categorizeMultipleCategories(self, text, categories):
        if self.authenticated:
            data = {
            'text': text,
            'categories': categories
            }
            response = requests.post(_config.blipper_url + "categorizeMultipleCategories", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def uploadFile(self, filename, directory):
        if self.authenticated:
            data = {
            'filename': filename,
            'directory': directory
            }
            response = requests.post(_config.blipper_url + "uploadFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getIdFromFile(self, filename):
        if self.authenticated:
            data = {
            'filename': filename
            }
            response = requests.get(_config.blipper_url + "getIdFromFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getFileFromId(self, id):
        if self.authenticated:
            data = {
            'id': id
            }
            response = requests.get(_config.blipper_url + "getFileFromId", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getAllFilesAndIds(self):
        if self.authenticated:
            response = requests.get(_config.blipper_url + "getAllFilesAndIds")
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def translate(self, text, target_lang):
        if self.authenticated:
            data = {
            'text': text,
            'target_lang': target_lang
            }
            response = requests.post(_config.blipper_url + "translate", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def replaceFile(self, filename, id):
        if self.authenticated:
            data = {
            'filename': filename,
            'id': id
            }
            response = requests.post(_config.blipper_url + "replaceFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def htmlize(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "htmlize", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def analyzeCsv(self, csv_file, query):
        if self.authenticated:
            data = {
            'csv_file': csv_file,
            'query': query
            }
            response = requests.post(_config.blipper_url + "analyzeCsv", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getLanguageText(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "getLanguageText", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getLanguageFile(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "getLanguageFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def speechToText(self, filename):
        if self.authenticated:
            data = {
            'filename': filename
            }
            response = requests.post(_config.blipper_url + "speechToText", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def textToSpeech(self, text, output_path):
        if self.authenticated:
            data = {
            'text': text,
            'output_path': output_path
            }
            response = requests.post(_config.blipper_url + "textToSpeech", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def generateImage(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "generateImage", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def askImage(self, url, query):
        if self.authenticated:
            data = {
            'url': url,
            'query': query
            }
            response = requests.post(_config.blipper_url + "askImage", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def answer_question_from_text(self, text, query):
        if self.authenticated:
            data = {
            'text': text,
            'query': query
            }
            response = requests.post(_config.blipper_url + "answerQuestion", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None    
        
    def categorize_text_from_options(self, text, options):
        if self.authenticated:
            data = {
            'text': text,
            'options': options
            }
            response = requests.post(_config.blipper_url + "categorize-text-from-options", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def categorize_text_multiple_from_options(self, text, options):
        if self.authenticated:
            data = {
            'text': text,
            'options': options
            }
            response = requests.post(_config.blipper_url + "categorize-text-multiple-from-options", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def create_agent(self, name, description, task):
        if self.authenticated:
            data = {'name': name, 'description': description, 'task': task}
            response = requests.post(self.base_url + "create-agent", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def update_agent(self, agent_id: str, agent_info: dict):
        if self.authenticated:
            data = {"id": agent_id, **agent_info}
            response = requests.post(self.base_url + "agents/update-agent", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def agent_detail(self, agent_id: str):
        if self.authenticated:
            data = { "agent_id": agent_id }
            response = requests.post(self.base_url + "agents/agent-detail", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def create_conversation(self, agent_id: str, user_id: str | None = None) -> str:    
        if self.authenticated:
            data = { "agent_id": agent_id, "user_id": user_id }
            response = requests.post(self.base_url + "agents/create-conversation", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def get_conversation(self, conversation_id):
        if self.authenticated:
            data = {'conversation_id': conversation_id}
            response = requests.post(self.base_url + "agents/get-conversation", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def add_file_to_agent(self, agent_id: str, filename: str, file) -> None:
        from pathlib import Path        
        if self.authenticated:
            file = {'file': (filename, file.read(), Path(filename).suffix)}
            response = requests.post(self.base_url + f"agents/add-file-to-agent/{agent_id}", files=file, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def agent_files(self, agent_id: str):
        if self.authenticated:
            data = { "agent_id": agent_id }
            response = requests.post(self.base_url + "agents/agent-files/", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def delete_agent_file(self, agent_id: str, file_id: str):
        if self.authenticated:
            response = requests.post(self.base_url + f"agents/remove-agent-file/{agent_id}/{file_id}", headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
                
    def add_user_message(self, conversation_id: str, message: str, agent_id: str):
        if self.authenticated:
            data = { "conversation_id": conversation_id, "message": message, "agent_id": agent_id}
            response = requests.post(self.base_url + "agents/add-user-message/", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None