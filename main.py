import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from googletrans import Translator

def assistente_voz(frase):
    som = pyttsx3.init()
    data_sound = ''
    trans = Translator()

    try:
        in_inter = False
        in_conselho = False
        if 'jogo do inter' in frase:
            in_inter = True

        if 'conselho' in frase:
            in_conselho = True

        if 'piada' in frase:
            in_piada = True

        if in_inter:
            webbrowser.open('https://www.google.com/search?q=inter+jogos', new=0, autoraise=True)
            data_sound = "Buscando jogos do Inter"

        elif in_conselho:
            url = "https://api.adviceslip.com/advice"
            response = requests.request("GET", url)
            conselho = response.json()
            conselho = conselho['slip']['advice']
            data_sound = trans.translate(conselho, dest='pt').text

        elif in_piada:
            url = "https://icanhazdadjoke.com/"
            headers = {'Accept': 'application/json'}
            response = requests.request("GET", url, headers=headers)
            piada = response.json()
            piada = piada['joke']
            data_sound = trans.translate(piada, dest='pt').text

        else:
            data_sound = 'Desculpe, não entendi!'

        print('Você disse: ' + frase)
    except:
        data_sound = 'Desculpe, não entendi!'
    finally:
        print('Resposta: ' + data_sound)
        som.say(data_sound)
        som.runAndWait()


if __name__ == '__main__':
    microfone = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            try:
                microfone.adjust_for_ambient_noise(source)
                print("Ouvindo: ")
                audio = microfone.listen(source)
                frase = microfone.recognize_google(audio, language='pt-BR')
                frase = frase.lower()
                print(frase)
                if('assistente' in frase):
                    assistente_voz(frase)
            except:
                print('Som não reconhecivel')





