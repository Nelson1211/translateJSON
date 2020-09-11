from googletrans import Translator, LANGUAGES
import json

def translate(file_name, input_language):
    translator = Translator()
    with open(file_name) as f:
        data = json.load(f)
    output = []
    for text in data:
        output.append(translator.translate(text['text'], dest=input_language).text)
    return output

def main():
    languages = LANGUAGES
    try:
        file_name = input('Name of the input file: ')
        input_language = input('Output Language: ')
        if input_language in languages:
            print(translate(file_name, input_language))
        elif input_language in languages.values():
            for key, value in languages.items(): 
                if input_language == value:
                    print(translate(file_name, input_language))
        else:
            print('Language not available')
    except:
        print('Could not find the file')

if __name__ == '__main__':
    main()