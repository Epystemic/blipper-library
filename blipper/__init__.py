from io import BufferedReader
from pathlib import Path
import json, requests
from . import _config


__version__ = '0.0.1'

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
        response = requests.post(_config.BLIPPER_AUTH_URL, json=data)
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
        
    def uploadFile(self, src_file, dest_dir):
        if self.authenticated:
            data = {
            'src_file': src_file,
            'dest_dir': dest_dir
            }
            response = requests.post(_config.blipper_url + "uploadFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getAllFiles(self):
        if self.authenticated:
            response = requests.get(_config.blipper_url + "getAllFiles")
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def translateText(self, text, target_lang):
        if self.authenticated:
            data = {
            'text': text,
            'target_lang': target_lang
            }
            response = requests.post(_config.blipper_url + "translateText", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def translateFile(self, file_id, target_lang):
        if self.authenticated:
            data = {
            'file_id': file_id,
            'target_lang': target_lang
            }
            response = requests.post(_config.blipper_url + "translateFile", json=data, headers=self.headers)
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
    
    def analyzeCSV(self, id, query):
        if self.authenticated:
            data = {
            'id': id,
            'query': query
            }
            response = requests.post(_config.blipper_url + "analyzeCSV", json=data, headers=self.headers)
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
        
    def getLanguageFile(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "getLanguageFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def TextFromAudio(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "TextFromAudio", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def AudioFromText(self, text, filename):
        if self.authenticated:
            data = {
            'text': text,
            'filename': filename
            }
            response = requests.post(_config.blipper_url + "AudioFromText", json=data, headers=self.headers)
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
        
    def askImage(self, image_id, query):
        if self.authenticated:
            data = {
            'image_id': image_id,
            'query': query
            }
            response = requests.post(_config.blipper_url + "askImage", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def describeImage(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "describeImage", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def textFromImage(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "textFromImage", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def summarizeTextInOneSentence(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "summarizeTextInOneSentence", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def summarizeFileInOneSentence(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "summarizeFileInOneSentence", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def summarizeTextInOneParagraph(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "summarizeTextInOneParagraph", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None


    def summarizeFileInOneParagraph(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "summarizeFileInOneParagraph", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None


    def promptBlipper(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "promptBlipper", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def getKeyPointsText(self, text, num):
        if self.authenticated:
            data = {
            'text': text,
            'num': num
            }
            response = requests.post(_config.blipper_url + "getKeyPointsText", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def getKeyPointsFile(self, file_id, num):
        if self.authenticated:
            data = {
            'file_id': file_id,
            'num': num
            }
            response = requests.post(_config.blipper_url + "getKeyPointsFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    
    def beepBadWords(self, text, custom_list):
        if self.authenticated:
            data = {
            'text': text,
            'custom_list': custom_list
            }
            response = requests.post(_config.blipper_url + "beepBadWords", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def hasBadWords(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "hasBadWords", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def askFile(self, id, query):
        if self.authenticated:
            data = {
            'id': id,
            'query': query
            }
            response = requests.post(_config.blipper_url + "askFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None


    def recognizeCelebrities(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "recognizeCelebrities", json=data, headers=self.headers)
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
        
    def create_agent(self, name, description, task, instructions):
        if self.authenticated:
            data = {'name': name, 'description': description, 'task': task, "instructions": instructions}
            response = requests.post(self.base_url + "agents/create-agent", json=data, headers=self.headers)
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
    
    def list_agents(self):
        if self.authenticated:
            response = requests.get(_config.blipper_url + "list-agents", headers=self.headers)
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
            # if not stream:
                # data = { "conversation_id": conversation_id, "message": message, "agent_id": agent_id}
                # response = requests.post(self.base_url + "agents/add-user-message/", json=data, headers=self.headers)
                # return response.json()
            data = { "conversation_id": conversation_id, "message": message, "agent_id": agent_id}
            response = requests.post(self.base_url + "agents/add-user-message/", json=data, headers=self.headers, stream=True)
            for chunk in response.iter_content(decode_unicode="utf-8", chunk_size=None):
                yield chunk
        else:
            print_invalid_api_key()
            return None


    def evaluate_resume(self, resume, job_reqs):
        if self.authenticated:
            data = {
            'resume': resume,
            'job_reqs': job_reqs
            }
            response = requests.post(_config.blipper_url + "evaluate-resume", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def explain_topic(self, text, num):
        if self.authenticated:
            data = {
            'text': text,
            'num': num
            }
            response = requests.post(_config.blipper_url + "explain-topic", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def extract_text(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "extractText", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getFileType(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "getFileType", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
    """
    def summarize_chat(self, conversation_id):
        if self.authenticated:
            data = {
            'conversation_id': conversation_id
            }
            response = requests.post(_config.blipper_url + "chat-agents/summarize-chat", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def set_chat_goal(self, conversation_id, goal):
        if self.authenticated:
            data = {
            'conversation_id': conversation_id,
            'goal': goal
            }
            response = requests.post(_config.blipper_url + "chat-agents/set-chat-goal", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def check_chat_goal_completed(self, conversation_id):
        if self.authenticated:
            data = {
            'conversation_id': conversation_id
            }
            response = requests.post(_config.blipper_url + "chat-agents/check-chat-goal-completed", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    
    def get_chat_sentiment(self, conversation_id, criteria, num_max):
        if self.authenticated:
            data = {
            'conversation_id': conversation_id,
            'criteria': criteria,
            'num_max': num_max
            }
            response = requests.post(_config.blipper_url + "chat-agents/chat-sentiment", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
       """ 
    def upload_template_file(self, filename: str, file) -> None:
        from pathlib import Path
        if self.authenticated:
            file = {'file': (filename, file.read(), Path(filename).suffix)}
            response = requests.post(self.base_url + f"upload-template-file/", files=file, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def key_values_from_pdf(self, filename: str, file) -> None:
        if self.authenticated:
            file = {'file': ("", file.read(), Path(filename).suffix)}
            response = requests.post(self.base_url + f"key-values-from-pdf/", files=file, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def create_template(self, template_id: str, values: list[str], source_document: BufferedReader, final_document_id: str):
        if self.authenticated:
            file = {"file": (source_document.name.split("/")[-1], source_document.read(), Path(source_document.name).suffix) }
            data = {
                "template_id": template_id,
                "values": values,
                "final_document_id": final_document_id
            }
            print(data)
            response = requests.post(self.base_url + "create-template/", files=file, data=data)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def breakDownTask(self, text, num):
        if self.authenticated:
            data = {
            'text': text,
            'num': num
            }
            response = requests.post(_config.blipper_url + "breakDownTask", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def toxicityIndex(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "toxicityIndex", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def TranscriptFromConversation(self, s3_uri, language, max_speakers):
        if self.authenticated:
            data = {
                's3_uri': s3_uri,
                'language': language,
                'max_speakers': max_speakers
            }
            response = requests.post(_config.blipper_url + "TranscriptFromConversation", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def deleteFile(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "deleteFile", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def getSentiment(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "getSentiment", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def paraphraseSimple(self, text):
        if self.authenticated:
            data = {
            'text': text
            }
            response = requests.post(_config.blipper_url + "paraphraseSimple", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def paraphrase(self, text, num_words, style):
        if self.authenticated:
            data = {
            'text': text,
            'num_words': num_words,
            'style': style
            }
            response = requests.post(_config.blipper_url + "paraphrase", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def AudioFromVideo(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "AudioFromVideo", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def trimAudioClip(self, file_id, start_minutes, end_minutes):
        if self.authenticated:
            data = {
            'file_id': file_id,
            'start_minutes': start_minutes,
            'end_minutes': end_minutes
            }
            response = requests.post(_config.blipper_url + "trimAudioClip", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None
        
    def TextFromVideo(self, file_id):
        if self.authenticated:
            data = {
            'file_id': file_id
            }
            response = requests.post(_config.blipper_url + "TextFromVideo", json=data, headers=self.headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None