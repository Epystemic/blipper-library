from io import BufferedReader
from pathlib import Path
import json, requests
from . import _config


__version__ = "0.0.1"

def print_invalid_api_key():
    print("Invalid API key")


class Blipper:
    def __init__(self, api_key, verbatim=True):
        self.api_key = api_key
        self.base_url = _config.blipper_url
        self.headers = {"api_key_header": api_key}
        self.authenticated, self.user = self.verify_api_key()
        self.verbatim = verbatim

    def response_template(self, input_data: dict, func_name: str):
        if self.authenticated:
            response = requests.post(
                _config.blipper_url + func_name, json=input_data, headers=self.headers
            )
            if self.verbatim:
                return response.json()
            else:
                return response.json()["response"]
        else:
            print_invalid_api_key()
            return None

    def getStatus(self, apikey):
        data = {"key": apikey}
        response = requests.post(_config.BLIPPER_AUTH_URL, json=data)
        return json.loads(response.content)

    def verify_api_key(self):
        response = self.getStatus(self.api_key)
        is_valid = True if response["status"] == 1 else False
        user_id = response["client_id"]
        return is_valid, user_id

    def categorizeSingleCategory(self, text, categories):
        data = {"text": text, "categories": categories}
        func_name = "categorizeSingleCategory"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def categorizeMultipleCategories(self, text, categories):
        data = {"text": text, "categories": categories}
        func_name = "categorizeMultipleCategories"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def uploadFile(self, src_file, dest_dir):
        data = {"src_file": src_file, "dest_dir": dest_dir}
        func_name = "uploadFile"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getAllFiles(self):
        if self.authenticated:
            response = requests.get(_config.blipper_url + "getAllFiles")
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def translateText(self, text, target_lang):
        data = {"text": text, "target_lang": target_lang}
        func_name = "translateText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def translateFile(self, file_id, target_lang):
        data = {"file_id": file_id, "target_lang": target_lang}
        func_name = "translateFile"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def htmlize(self, text):
        data = {"text": text}
        func_name = "htmlize"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def analyzeCSV(self, id, query):
        data = {"id": id, "query": query}
        func_name = "analyzeCSV"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getLanguageText(self, text):
        data = {"text": text}
        func_name = "getLanguageText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getLanguageFile(self, file_id):
        data = {"file_id": file_id}
        func_name = "getLanguageFile"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def TextFromAudio(self, file_id):
        data = {"file_id": file_id}
        func_name = "TextFromAudio"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def AudioFromText(self, text, filename):
        data = {"text": text, "filename": filename}
        func_name = "AudioFromText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def generateImage(self, text):
        data = {"text": text}
        func_name = "generateImage"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def askImage(self, image_id, query):
        data = {"image_id": image_id, "query": query}
        func_name = "askImage"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def describeImage(self, file_id):
        data = {"file_id": file_id}
        func_name = "describeImage"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def textFromImage(self, file_id):
        data = {"file_id": file_id}
        func_name = "textFromImage"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def summarizeTextInOneSentence(self, text):
        data = {"text": text}
        func_name = "summarizeTextInOneSentence"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def summarizeFileInOneSentence(self, file_id):
        data = {"file_id": file_id}
        func_name = "summarizeFileInOneSentence"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def summarizeTextInOneParagraph(self, text):
        data = {"text": text}
        func_name = "summarizeTextInOneParagraph"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def summarizeFileInOneParagraph(self, file_id):
        data = {"file_id": file_id}
        func_name = "summarizeFileInOneParagraph"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def promptBlipper(self, text):
        data = {"text": text}
        func_name = "promptBlipper"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getKeyPointsText(self, text, num):
        data = {"text": text, "num": num}
        func_name = "getKeyPointsText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getKeyPointsFile(self, file_id, num):
        data = {"file_id": file_id, "num": num}
        func_name = "getKeyPointsFile"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def beepBadWords(self, text, custom_list):
        data = {"text": text, "custom_list": custom_list}
        func_name = "beepBadWords"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def hasBadWords(self, text):
        data = {"text": text}
        func_name = "hasBadWords"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def askFile(self, id, query):
        data = {"id": id, "query": query}
        func_name = "askFile"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def recognizeCelebrities(self, file_id):
        data = {"file_id": file_id}
        func_name = "recognizeCelebrities"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def answer_question_from_text(self, text, query):
        data = {"text": text, "query": query}
        func_name = "answerQuestion"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def categorize_text_from_options(self, text, options):
        data = {"text": text, "options": options}
        func_name = "categorize-text-from-options"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def categorize_text_multiple_from_options(self, text, options):
        data = {"text": text, "options": options}
        func_name = "categorize-text-multiple-from-options"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def create_agent(self, name, description, task, instructions):
        data = {
            "name": name,
            "description": description,
            "task": task,
            "instructions": instructions,
        }
        func_name = "agents/create-agent"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def create_conversation(self, agent_id: str, user_id: str | None = None) -> str:
        data = {"agent_id": agent_id, "user_id": user_id}
        func_name = "agents/create-conversation"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def get_conversation(self, conversation_id):
        data = {"conversation_id": conversation_id}
        func_name = "agents/get-conversation"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def update_agent(self, agent_id: str, agent_info: dict):
        data = {"id": agent_id, **agent_info}
        func_name = "agents/update-agent"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def agent_detail(self, agent_id: str):
        data = {"agent_id": agent_id}
        func_name = "agents/agent-detail"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def list_agents(self):
        if self.authenticated:
            response = requests.get(
                _config.blipper_url + "list-agents", headers=self.headers
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def add_file_to_agent(self, agent_id: str, filename: str, file) -> None:
        from pathlib import Path

        if self.authenticated:
            file = {"file": (filename, file.read(), Path(filename).suffix)}
            response = requests.post(
                self.base_url + f"agents/add-file-to-agent/{agent_id}",
                files=file,
                headers=self.headers,
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def agent_files(self, agent_id: str):
        data = {"agent_id": agent_id}
        func_name = "agents/agent-files/"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def delete_agent_file(self, agent_id: str, file_id: str):
        if self.authenticated:
            response = requests.post(
                self.base_url + f"agents/remove-agent-file/{agent_id}/{file_id}",
                headers=self.headers,
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def add_user_message(self, conversation_id: str, message: str, agent_id: str):
        if self.authenticated:
            data = {
                "conversation_id": conversation_id,
                "message": message,
                "agent_id": agent_id,
            }
            response = requests.post(
                self.base_url + "agents/add-user-message/",
                json=data,
                headers=self.headers,
                stream=True,
            )
            for chunk in response.iter_content(decode_unicode="utf-8", chunk_size=None):
                yield chunk
        else:
            print_invalid_api_key()
            return None

    def evaluate_resume(self, resume, job_reqs):
        if self.authenticated:
            data = {"resume": resume, "job_reqs": job_reqs}
        func_name = "evaluate-resume"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def explain_topic(self, text, num):
        if self.authenticated:
            data = {"text": text, "num": num}
        func_name = "explain-topic"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def extract_text(self, file_id):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "extractText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getFileType(self, file_id):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "getFileType"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def upload_template_file(self, filename: str, file) -> None:
        from pathlib import Path

        if self.authenticated:
            file = {"file": (filename, file.read(), Path(filename).suffix)}
            response = requests.post(
                self.base_url + f"upload-template-file/",
                files=file,
                headers=self.headers,
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def key_values_from_pdf(self, filename: str, file) -> None:
        if self.authenticated:
            file = {"file": ("", file.read(), Path(filename).suffix)}
            response = requests.post(
                self.base_url + f"key-values-from-pdf/",
                files=file,
                headers=self.headers,
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def create_template(
        self,
        template_id: str,
        values: list[str],
        source_document: BufferedReader,
        final_document_id: str,
    ):
        if self.authenticated:
            file = {
                "file": (
                    source_document.name.split("/")[-1],
                    source_document.read(),
                    Path(source_document.name).suffix,
                )
            }
            data = {
                "template_id": template_id,
                "values": values,
                "final_document_id": final_document_id,
            }
            print(data)
            response = requests.post(
                self.base_url + "create-template/", files=file, data=data
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def breakDownTask(self, text, num):
        if self.authenticated:
            data = {"text": text, "num": num}
        func_name = "breakDownTask"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def toxicityIndex(self, text):
        if self.authenticated:
            data = {"text": text}
        func_name = "toxicityIndex"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def TranscriptFromConversation(self, s3_uri, language, max_speakers):
        if self.authenticated:
            data = {
                "s3_uri": s3_uri,
                "language": language,
                "max_speakers": max_speakers,
            }
        func_name = "TranscriptFromConversation"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def deleteFile(self, file_id):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "deleteFile"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def getSentiment(self, text):
        if self.authenticated:
            data = {"text": text}
        func_name = "getSentiment"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def paraphraseSimple(self, text):
        if self.authenticated:
            data = {"text": text}
        func_name = "paraphraseSimple"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def paraphrase(self, text, num_words, style):
        if self.authenticated:
            data = {"text": text, "num_words": num_words, "style": style}
        func_name = "paraphrase"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def AudioFromVideo(self, file_id):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "AudioFromVideo"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def trimAudioClip(self, file_id, start_minutes, end_minutes):
        if self.authenticated:
            data = {
                "file_id": file_id,
                "start_minutes": start_minutes,
                "end_minutes": end_minutes,
            }
        func_name = "trimAudioClip"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def TextFromVideo(self, file_id):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "TextFromVideo"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

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