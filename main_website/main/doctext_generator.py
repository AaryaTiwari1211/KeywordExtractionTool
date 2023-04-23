from django.conf import settings

def doc_extractor(file):
    document = open("C:/Users/Aarya/OneDrive/Desktop/GITHUB/KeywordExtractionTool/main_website/media/files/" + file, 'r')
    doc_text = document.read()
    return doc_text

