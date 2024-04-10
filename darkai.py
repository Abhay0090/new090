#Author t.me/K_HACKER_ANONYMOUS

#the offical tool of https://t.me/+RZC2K-IdwHdhMzc9


import requests
import os
from tqdm import tqdm
import json
# URLs for different modes
urls = { 
    2 : 'http://62.72.6.182:1717/darkgpt',
    1 : 'http://62.72.6.182:1717/check_balance',
    3 : 'http://62.72.6.182:1717/evilgpt',
    4 :'http://62.72.6.182:1717/elonmusk',
    5 :'http://62.72.6.182:1717/sweetbf',
    6 :'http://62.72.6.182:1717/sweetgf',
    7 :'http://62.72.6.182:1717/xsearch',
    8 :'http://62.72.6.182:1717/image',
    9 :'http://62.72.6.182:1717/image4',
    10 :'http://62.72.6.182:1717/rude'
    
}

# File containing the API key
api_key_file = 'api_key.txt'
print("""\033[1m\033[94m
  _____ _           _       _         _______ _     _              
 / ____(_)         | |     | |       |__   __| |   (_)             
| (___  _  ___ __ _| |_ ___| | ____ _   | |  | |__  _  ___ _ __ ___ 
 \___ \| |/ __/ _ | __/ _ \ |/ / _ |  | |  | '_ \| |/ _ \ '__/ __|
 ____) | | (_| (_| | ||  __/   < (_| |  | |  | | | | |  __/ |  \__ \\
|_____/|_|\___\__,_|\__\___|_|\_\__,_|  |_|  |_| |_|_|\___|_|  |___/
\033[0m""")

def download_file(url):
    directory = '/storage/emulated/0/BLACK_DOWNLOADS/'
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    save_path = directory + url.split('/')[-1] 
    with open(save_path, 'wb+') as file, tqdm(
        desc=save_path,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=2048,
    ) as bar:
        for data in response.iter_content(chunk_size=2048):
            file.write(data)
            (bar.update(len(data)))

    #print(f"\033[32mpath {save_path}")

def create_directory():
    directory = '/storage/emulated/0/BLACK_DOWNLOADS/'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"\033[91mDirectory '{directory}' created. please check for all videos and images download")
    else:
        print(f"\033[91mDirectory '{directory}' already exists. please check for all videos and images download")

def get_api_key():
    try:
        with open(api_key_file, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def save_api_key(api_key):
    with open(api_key_file, 'w') as file:
        file.write(api_key)

def send_request(url, api_key, data):
    headers = {'X-API-KEY': api_key,
                'Content-Type':'application/json'
                }
    response = requests.post(url, json=data, headers=headers)
    #print(f"\033[94m{response.content}\033[0m")  # Blue color for response
    return response.json()

def check_api_balance(api_key):
    url = 'http://62.72.6.182:1717/check_balance'
    response = send_request(url, api_key, {})
    print(f"\033[32m{response}\033[0m")  # Green color for API balance response

def chat_mode(api_key, mode):
    url = urls.get(mode)
    if url is None:
        print("\033[91mInvalid mode selection.\033[0m")  # Red color for error
        return
    
    print(f"Welcome to Mode {mode}. Type 'exit' to switch modes.")
    if mode == 2:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'task':"generator",
                'program':"any",
                "prompt":user_input,
                "code":None ,
                'further_description1' :None,
                'further_description2' : None
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('message', api_response.get('message', ''))
            print(f"\033[93mBot: {bot_response}\033[0m")  # Yellow color for bot response
    elif  mode == 4:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'talk':user_input
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('message', api_response.get('message', ''))
            print(f"\033[93mElon: {bot_response}\033[0m")  # Yellow color for bot response
            
    elif  mode == 5:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'talk':user_input
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('message', api_response.get('message', ''))
            print(f"\033[93m❤🧏‍♂️: {bot_response}\033[0m")  # Yellow color for bot response
    elif  mode == 6:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'talk':user_input 
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('message', api_response.get('message', ''))
            print(f"\033[93m💗👰‍♂️: {bot_response}\033[0m")  # Yellow color for bot response
    elif  mode == 7:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            create_directory()
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'search':user_input
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('response', api_response.get('response', ''))
            #print(f"\033[93mElon: {bot_response}\033[0m")  # Yellow color for bot response
            for i in bot_response:
                try:
                    print(f"\033[32mdownloading {i['name']}")
                    jsons = {
                    'link':i['redirect_link']
                    }
                    r = 'http://62.72.6.182:1717/downloadx'
                    ap = send_request(r, api_key, jsons)
                    vid = ap['response']['contentUrl']
                    thumb = (ap['response']['thumbnailUrl'][0])
                    download_file(thumb , '.jpg')
                    download_file(vid.split('?')[0])
                except:
                    pass
                
    elif  mode == 8:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            create_directory()
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'query':user_input
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('images', api_response.get('images', ''))
            print(f"\033[32mDiffussion:\033[0m")  # Yellow color for bot response
            for i in json.loads(bot_response):
                link = (i['imageUrls'][0])
                download_file(link)
    elif  mode == 9:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            #create_directory()
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'query':user_input
            }
            #api_response = send_request(url, api_key, jsons)
            #bot_response = api_response.get('message', api_response.get('message', ''))
            print(f"\033[93mMidjourney: cooming soon\033[0m")  # Yellow color for bot response
    elif  mode == 10:
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            jsons = { 
                'talk':user_input
            }
            api_response = send_request(url, api_key, jsons)
            bot_response = api_response.get('message', api_response.get('message', ''))
            print(f"\033[93mRude: {bot_response}\033[0m")  # Yellow color for bot response
        
    else :
        while True:
            user_input = input("\033[95mYou: \033[0m")  # Purple color for user input
            
            if user_input.lower() == 'exit':
                print("Exiting the current mode.")
                break
            
            api_response = send_request(url, api_key, {'query':user_input})
            bot_response = api_response.get('message', api_response.get('messags', ''))
            print(f"\033[93mBot: {bot_response}\033[0m")  # Yellow color for bot response
    
# Fetch API key or prompt user for a new one
api_key = get_api_key()
if api_key is None:
    api_key = input("\033[1mPlease enter your API key: \033[0m")  # Bold text for input
    save_api_key(api_key)

# Main loop for selecting options
while True:
    print("\033[1mChoose an option:\033[0m")  # Bold text for menu
    print("1. Check API Balance")
    print("2. Dark Ai")
    print("3. Evil Ai")
    print("4. EloN Musk Ai")
    print("5. Husband Ai")
    print("6. Wife Ai")
    print("7. DOWNLOAD XXX")
    print("8. Diffusion")
    print("9. Midjourney")
    print("10. Rude")
    option = input("\033[95mEnter the option number or 'exit' to quit: \033[0m")  # Purple color for input
    
    if option.lower() == 'exit':
        print("\033[1mExiting the program. Goodbye!\033[0m")  # Bold text for exit message
        break
    elif option == '1':
        check_api_balance(api_key)
    else:
        try:
            selected_mode = int(option)
            if selected_mode in urls:
                chat_mode(api_key, selected_mode)
            else:
                print("\033[91mInvalid option.\033[0m")  # Red color for error
        except ValueError:
            print("\033[91mInvalid option. Please enter a number.\033[0m")  # Red color for error
