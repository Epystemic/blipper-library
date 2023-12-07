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

    def categorize_single_category(self, text, categories):
        if self.authenticated:
            data = {
            'text': text,
            'categories': categories
            }
            response = requests.post(_config.bitl_url + "categorize_single_category", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def categorize_multiple_categories(self, text, categories):
        if self.authenticated:
            data = {
            'text': text,
            'categories': categories
            }
            response = requests.post(_config.bitl_url + "categorize_multiple_categories", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def upload_doc(self, filename, directory):
        if self.authenticated:
            data = {
            'filename': filename,
            'directory': directory
            }
            response = requests.post(_config.bitl_url + "upload_doc", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def get_id_from_doc(self, filename):
        if self.authenticated:
            data = {
            'filename': filename
            }
            response = requests.get(_config.bitl_url + "get_id_from_doc", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def get_doc_from_id(self, id):
        if self.authenticated:
            data = {
            'id': id
            }
            response = requests.get(_config.bitl_url + "get_doc_from_id", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def get_all_docs_and_ids(self):
        if self.authenticated:
            response = requests.get(_config.bitl_url + "get_all_docs_and_ids")
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
        
    def replace_doc_id(self, filename, id):
        if self.authenticated:
            data = {
            'filename': filename,
            'id': id
            }
            response = requests.post(_config.bitl_url + "replace_doc_id", json=data)
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
    
    def analyze_csv(self, csv_file, query):
        if self.authenticated:
            data = {
            'csv_file': csv_file,
            'query': query
            }
            response = requests.post(_config.bitl_url + "analyze_csv", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def get_language_txt(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "get_language_txt", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def get_language_doc(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "get_language_doc", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def speech_to_text(self, filename):
        if self.authenticated:
            data = {
            'filename': filename
            }
            response = requests.post(_config.bitl_url + "speech_to_text", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def text_to_speech(self, text, output_path):
        if self.authenticated:
            data = {
            'text': text,
            'output_path': output_path
            }
            response = requests.post(_config.bitl_url + "text_to_speech", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def generate_image(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.bitl_url + "generate_image", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def ask_image(self, url, query):
        if self.authenticated:
            data = {
            'url': url,
            'query': query
            }
            response = requests.post(_config.bitl_url + "ask_image", json=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        