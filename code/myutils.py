
import spacy
import langdetect
from wordcloud import WordCloud 
from langdetect import DetectorFactory, detect, detect_langs
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunkDocs(doc, size):  
    r_text_splitter = RecursiveCharacterTextSplitter(
        # Set custom chunk size
        chunk_size = size,
        chunk_overlap  = 0,
        separators = ['\n\n', '\n', ' ', '']
    )
    split = r_text_splitter.split_documents(doc)
    # splits = r_text_splitter.split_text(doc)
    return split 

def langDetect(text):
    mylang = ''
    mylangprob = 0.0
    try:
        langs = langdetect.detect_langs(text)
        mylang, mylangprop = langs[0].lang, langs[0].prob 
        
        # English
        if mylang=='en': 
            models = ['en_core_web_md', 'da_core_news_md']
            default_model = 'en_core_web_md'
        # Danish    
        elif mylang=='da' or lang=='no': 
            models = ['da_core_news_md', 'en_core_web_md']
            default_model = 'da_core_news_md'
        # both    
        nlp = spacy.load(default_model)
        stopw = nlp.Defaults.stop_words
    
    # another language
    except langdetect.lang_detect_exception.LangDetectException:
        log.debug('Language not supported')
        
    return default_model, stopw

# Create a WordCloud object of a dataframe
def wordCloud(df, col):   
    longstring = [','.join(list(x)) for x in df[col].values]
    longstring = str(longstring).replace('\\n',' ')
    longstring = str(longstring).replace(col,' ')
    # get stopwords
    stopw = langDetect(longstring)[1]
    # remove stopwords
    words = [word for word in longstring.split() if word.lower() not in stopw]
    clean_text = " ".join(words)
    # settings
    wordcloud = WordCloud(background_color="white", max_words=1500, contour_width=3, contour_color='steelblue')
    # view
    wordcloud.generate(str(clean_text))
    im = wordcloud.to_image()
    return im,longstring
