import speech_recognition as sr
import os

def talk(text: str):
    text = text.lower()
    tasks = {
      # 'execute music': {
      'abrir música': {
        #'to_talk': 'executing music, wait.',
        'to_talk': 'abrindo musica, aguarde.',
        'cmd': 'brave https://www.youtube.com/watch\?v\=68xMEJqkUz4',
      },
      # 'show me bitcoin': {
      'mostre-me o bitcoin': {
        'to_talk': 'abrindo o navegador, aguarde.',
        'cmd': 'brave https://www.google.com/search?q=bitcoin',
      },
      'show me the weather': {
        'to_talk': 'showing the time today, wait.',
        'cmd': 'brave https://weather.com/pt-BR/clima/10dias/l/Presidente+Prudente+S%C3%A3o+Paulo?canonicalCityId=b9f000ab9c1ab94290c237f3d880b76719a7ee13e86687f5f5dead3f699e40ba',
      },
      'which is my system': {
        'to_talk': 'your system is Arch linux.',
      },
      'toque uma música doida': {
        'to_talk': 'executando, aguarde.',
        'cmd': 'brave https://www.youtube.com/watch?v=nYc09Xqy3hE'
      },
      'toque roberto carlos': {
        'to_talk': 'executando, aguarde.',
        'cmd': 'google-chrome-stable https://www.youtube.com/watch?v=54xxnkXqltw'
      },
      
    }
    task = tasks[text]

    for tx in task['to_talk'].split(' '):
        print(tx, end='')
        os.system(f'espeak -v pt {tx}')
        # os.system(f'espeak {tx}')
    try:
      os.system(task['cmd'])
    except:
      pass

recognizer = sr.Recognizer()
''' recording the sound '''

while True:
    with sr.Microphone() as source:
        # os.system('clear')

        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Recording...")
        recorded_audio = recognizer.listen(source)
        print("Done recording")

        ''' Recorgnizing the Audio '''
        try:
            print("Recognizing the text")
            text = recognizer.recognize_google(
                recorded_audio, 
                language="pt-BR"
                #language="en-US"
            )
            print("Decoded Text : {}".format(text))
            talk(text)

        except Exception as ex:
            print(ex)
