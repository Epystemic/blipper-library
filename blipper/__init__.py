import os
import logging
from io import BufferedReader
from pathlib import Path
import json
import requests
from typing import Literal
from . import _config


logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

__version__ = "0.0.1"


def print_invalid_api_key():
    logger.error("Invalid API key")


class Blipper:
    def __init__(
        self,
        blipper_api_key,
        verbose=True,
        user_id=None,
        conversation_id=None,
        model=None,
        anthropic_api_key=None,
        woocommerce_url=None,
        woocommerce_consumer_key=None,
        woocommerce_consumer_secret=None,
    ):
        self.blipper_api_key = blipper_api_key
        self.anthropic_api_key = anthropic_api_key
        self.base_url = (_config.blipper_url,)
        self.model = (model,)
        self.headers = {
            "blipper-api-key": blipper_api_key,
            "user_id": user_id,
            "conversation_id": conversation_id,
            "atenea-woocommerce-url":woocommerce_url,
            "atenea-woocommerce-consumer-key":woocommerce_consumer_key,
            "atenea-woocommerce-consumer-secret": woocommerce_consumer_secret,
            "model": model,
        }
        self.authenticated, self.user = self.verify_api_key()
        self.verbose = verbose

    def response_template(self, input_data: dict, func_name: str):
        if self.authenticated:
            response = requests.post(
                _config.blipper_url + func_name, json=input_data, headers=self.headers
            )
            logger.info(f"response: {response}")
            if self.verbose:
                resp_json = response.json()
                resp_json["user_id"] = self.headers["user_id"]
                resp_json["conversation_id"] = self.headers["conversation_id"]
                return resp_json
            else:
                return response.json()["response"]
        else:
            print_invalid_api_key()
            return None

    def response_files(self, input_data: dict, files: dict, func_name: str):
        if self.authenticated:
            response = requests.post(
                _config.blipper_url + func_name, files=files, data=input_data, headers=self.headers
            )
            logger.info(f"response: {response}")
            if self.verbose:
                resp_json = response.json()
                resp_json["user_id"] = self.headers["user_id"]
                resp_json["conversation_id"] = self.headers["conversation_id"]
                return resp_json
            else:
                return response.json()["response"]
        else:
            print_invalid_api_key()
            return None

    def getBlipperStatus(self, apikey):
        data = {"key": apikey}
        response = requests.post(_config.BLIPPER_AUTH_URL, json=data)
        return json.loads(response.content)

    def getAnthropicStatus(self, apikey):
        headers = {
            "x-api-key": apikey,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01",
        }
        data = {
            "model": "claude-3-haiku-20240307",
            "messages": [{"role": "user", "content": "Test"}],
            "max_tokens": 1,
        }

        response = requests.post(_config.ANTHROPIC_AUTH_URL, json=data, headers=headers)
        return response.ok
        #     response.raise_for_status()
        #     return True
        #     print("API Key is valid.")
        # except requests.exceptions.HTTPError as http_err:
        #     if response.status_code == 401:
        #         print("Unauthorized: Invalid API Key.")
        #     else:
        #         print(f"HTTP error occurred: {http_err}")
        #     return False
        # except Exception as err:
        #     print(f"Other error occurred: {err}")
        #     return False

    def verify_api_key(self):
        is_blipper, user = self.verify_blipper_api_key()
        if is_blipper:
            if self.anthropic_api_key:
                is_anthropic = self.verify_anthropic_api_key()
                if is_anthropic:
                    return True, user
                else:
                    return False, None
        else:
            return False, None
        return is_blipper, user

    def verify_anthropic_api_key(self):
        is_valid = self.getAnthropicStatus(self.anthropic_api_key)
        return is_valid

    def verify_blipper_api_key(self):
        response = self.getBlipperStatus(self.blipper_api_key)
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

    # def uploadFile(self, src_file, dest_dir):
    #     data = {"src_file": src_file, "dest_dir": dest_dir}
    #     func_name = "uploadFile"
    #     result = self.response_template(input_data=data, func_name=func_name)
    #     return result

    def uploadFile(self, src_file, dest_dir):
        if not os.path.exists(src_file):
            raise FileNotFoundError(f"{src_file} does not exist")

        with open(src_file, 'rb') as f:
            files = {'src_file': (os.path.basename(src_file), f)}
            data = {'dest_dir': dest_dir}
            func_name = "uploadFile"
            result = self.response_files(input_data=data, files=files, func_name=func_name)
        return result

    def getAllFiles(self):
        if self.authenticated:
            headers = {
                'accept': 'application/json',
                'blipper-api-key': self.blipper_api_key
                }
            response = requests.get(_config.blipper_url + "getAllFiles", headers=headers)
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def translateText(
        self,
        text: str,
        target_lang: Literal["inglés", "español", "aleman", "portugues"],
    ):
        """
        Function to translate a given text into a selected language
        """
        data = {"text": text, "target_lang": target_lang}
        func_name = "translateText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def translateFile(
        self,
        file_id: str,
        target_lang: Literal["inglés", "español", "aleman", "portugues"],
    ):
        """
        Function to translate the text of a given file into a selected language
        """
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

    def describeImage(self, file_id: str, language=None):
        data = {"file_id": file_id, "language": language}
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

    def hideSwearWords(self, text, custom_list):
        data = {"text": text, "custom_list": custom_list}
        func_name = "hideSwearWords"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def hasSwearWords(self, text):
        data = {"text": text}
        func_name = "hasSwearWords"
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

    def uploadTemplateFile(self, filename: str, file: BufferedReader) -> None:
        if self.authenticated:
            file = {"file": (filename, file.read(), Path(filename).suffix)}
            response = requests.post(
                self.base_url + "upload-template-file/",
                files=file,
                headers=self.headers,
            )
            return response.json()
        else:
            print_invalid_api_key()
            return None

    def createTemplate(
        self,
        template_id: str,
        source_documents: list[str],
        final_document_id: str,
    ):
        """
        Function to complete variables of a document template based on information from source documents.
        """
        if self.authenticated:
            data = {
                "template_id": template_id,
                "final_document_id": final_document_id,
                "source_files_ids": source_documents,
            }
        func_name = "create-template"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def breakDownTask(self, text: str, num: int):
        if self.authenticated:
            data = {"text": text, "num": num}
        func_name = "breakDownTask"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def toxicityIndex(self, text: str):
        if self.authenticated:
            data = {"text": text}
        func_name = "toxicityIndex"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def TranscriptFromConversation(self, s3_uri: str, max_speakers: int, language=None):
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

    def paraphraseSimple(self, text: str, language=None):
        if self.authenticated:
            data = {"text": text, "language": language}
        func_name = "paraphraseSimple"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def paraphrase(self, text: str, num_words: int, style: str):
        if self.authenticated:
            data = {"text": text, "num_words": num_words, "style": style}
        func_name = "paraphrase"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def AudioFromVideo(self, file_id: str):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "AudioFromVideo"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def trimAudioClip(self, file_id: str, start_minutes, end_minutes):
        if self.authenticated:
            data = {
                "file_id": file_id,
                "start_minutes": start_minutes,
                "end_minutes": end_minutes,
            }
        func_name = "trimAudioClip"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def TextFromVideo(self, file_id: str):
        if self.authenticated:
            data = {"file_id": file_id}
        func_name = "TextFromVideo"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def SendWhatsappMessage(self, waapi_apikey, phone_number, message):
        if self.authenticated:
            data = {
                "waapi_apikey": waapi_apikey,
                "phone_number": phone_number,
                "message": message,
            }
        func_name = "whatsapp/send-message"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def SendWhatsappMedia(self, waapi_apikey, phone_number, mediaUrl):
        if self.authenticated:
            data = {
                "waapi_apikey": waapi_apikey,
                "phone_number": phone_number,
                "mediaUrl": mediaUrl,
            }
        func_name = "whatsapp/send-media"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def SendWhatsappAudioFromText(self, waapi_apikey, phone_number, text):
        if self.authenticated:
            data = {
                "waapi_apikey": waapi_apikey,
                "phone_number": phone_number,
                "text": text,
            }
        func_name = "whatsapp/send-AudioFromText"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def routeQuery(self, text):
        if self.authenticated:
            data = {
                "text": text
            }
        func_name = "rag/route-query"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def textFromURL(self, url):
        if self.authenticated:
            data = {
                "url": url
            }
        func_name = "TextFromURL"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def promptClaude(self, text):
        if self.authenticated:
            data = {
                "text": text
            }
        func_name = "TextFromURL"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def generateImageStableDiffusion(self, text):
        if self.authenticated:
            data = {
                "text": text
            }
        func_name = "generateImageStableDiffusion"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def textFromImageOpenAI(self, file_id):
        if self.authenticated:
            data = {
                "file_id": file_id
            }
        func_name = "textFromImageOpenAI"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def detectExplicitContent(self, file_id):
        if self.authenticated:
            data = {
                "file_id": file_id
            }
        func_name = "detectExplicitContent"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def summarizeFile(self, file_id, length_words):
        if self.authenticated:
            data = {
                "file_id": file_id,
                "length_words": length_words
            }
        func_name = "files-manager/summarize-file"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def categorizeFile(self, file_id, options):
        if self.authenticated:
            data = {
                "file_id": file_id,
                "options": options
            }
        func_name = "files-manager/categorize-file"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def questionFile(self, file_id, query):
        if self.authenticated:
            data = {
                "file_id": file_id,
                "query": query
            }
        func_name = "files-manager/question-file"
        result = self.response_template(input_data=data, func_name=func_name)
        return result

    def answerQuestion(self, text, query, language=None):
        if self.authenticated:
            data = {
                "text": text,
                "query": query,
                "language": language
            }
        func_name = "answerQuestion"
        result = self.response_template(input_data=data, func_name=func_name)
        return result
    
    def WooconnerceGetProductDetailsFromUrl(
        self,
        domain: str,
        product_directory: str,
        product_url: str,
        desired_basic_attributes: list[str] | None = None,
        desired_variation_attributes: list[str] | None = None
    ):
        if self.authenticated:
            data = {
                "domain": domain,
                "product_directory": product_directory,
                "product_url": product_url,
                "desired_basic_attributes": desired_basic_attributes,
                "desired_variation_attributes": desired_variation_attributes,
            }
        func_name = "woocommerce/get-product-details-from-url"
        result = self.response_template(input_data=data, func_name=func_name)
        return result
