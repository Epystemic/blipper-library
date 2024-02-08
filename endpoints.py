import requests

import _config
from _config import BITL_API_KEY


def print_invalid_api_key():
    print("Invalid API key")

class Bitl:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = _config.bitl_url
        self.authenticated, self.user = self.verify_api_key()

    def verify_api_key(self):
        if self.api_key == BITL_API_KEY:
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
            response = requests.post(_config.bitl_url + "categorizeSingleCategory", json=data)
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
            response = requests.post(_config.bitl_url + "categorizeMultipleCategories", json=data)
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
            response = requests.post(_config.bitl_url + "uploadFile", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getIdFromFile(self, filename):
        if self.authenticated:
            data = {
            'filename': filename
            }
            response = requests.get(_config.bitl_url + "getIdFromFile", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getFileFromId(self, id):
        if self.authenticated:
            data = {
            'id': id
            }
            response = requests.get(_config.bitl_url + "getFileFromId", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getAllFilesAndIds(self):
        if self.authenticated:
            response = requests.get(_config.bitl_url + "getAllFilesAndIds")
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
            response = requests.post(_config.bitl_url + "translate", json=data)
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
            response = requests.post(_config.bitl_url + "replaceFile", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def htmlize(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "htmlize", json=data)
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
            response = requests.post(_config.bitl_url + "analyzeCsv", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getLanguageText(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "getLanguageText", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getLanguageFile(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "getLanguageFile", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def speechToText(self, filename):
        if self.authenticated:
            data = {
            'filename': filename
            }
            response = requests.post(_config.bitl_url + "speechToText", json=data)
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
            response = requests.post(_config.bitl_url + "textToSpeech", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def generateImage(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "generateImage", json=data)
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
            response = requests.post(_config.bitl_url + "askImage", json=data)
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
            response = requests.post(_config.bitl_url + "answerQuestion", json=data)
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
            response = requests.post(_config.bitl_url + "categorize-text-from-options", json=data)
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
            response = requests.post(_config.bitl_url + "categorize-text-multiple-from-options", json=data)
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
            response = requests.post(_config.bitl_url + "create-agent", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None   