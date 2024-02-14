import requests

import _config
from _config import BLIPPER_API


def print_invalid_api_key():
    print("Invalid API key")

class Blipper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = _config.blipper_url
        self.headers = {"api_key_header": api_key}
        self.authenticated, self.user = self.verify_api_key()

    def verify_api_key(self):
        if self.api_key == BLIPPER_API:
            # Connect to L2 layer for authentication
            return True, "User1"
        else:
            return False, None

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
        
    def create_agent(self, name, description, instructions):
        if self.authenticated:
            data = {
            'name': name,
            'description': description,
            'instructions': instructions
            }
            response = requests.post(_config.blipper_url + "create-agent", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def get_conversation(self, conversation_id):
        if self.authenticated:
            data = {
            'conversation_id': conversation_id
            }
            response = requests.post(_config.blipper_url + "get-conversation", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None