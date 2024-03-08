import os
from typing import List

# LangChain Document readers
from langchain.document_loaders import WikipediaLoader
from langchain.document_loaders import YoutubeLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
# from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

# Load Entire Dir
def loadDir(path, filetype='*')->List:    
    loader = DirectoryLoader(path, glob="**/*." + filetype, show_progress=True)
    docs = loader.load()
    return docs


# Load Single Files
def loadFile(file) -> List:
    if file.endswith(".pdf"):
        loader = PyPDFLoader(file)
    elif file.endswith('.docx') or file.endswith('.doc'):
        loader = Docx2txtLoader(file)
    elif file.endswith('.txt'):
        loader = TextLoader(file)
    docs = loader.load()
    return docs


# Load Wiki
def loadWiki(query, lang, n) -> List:
    loader = WikipediaLoader(query=query, lang=lang, load_max_docs=n)
    docs = loader.load()
    return docs


# Load Youtube
def loadYoutube(url, lang) -> List:
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True, language = lang, translation = lang)
    docs = loader.load()
    return docs


# Read API
def readAPI(url, params, headers, filename):  
    import json
    import requests
    list = []
    response = requests.get(url, params=params, headers=headers).json()
    list.append(response)
    
    # save in json file        
    with open(filename, 'w') as f:
        json.dump(list,f, indent=4)
