import os
import subprocess
import platform
import time
import webbrowser
import requests
from bs4 import BeautifulSoup


def fileExists(filename, directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            return True
        else:
            return False
def listFiles(directory):
    files = os.listdir(directory)
    return files
def listProcesses():
    processes = os.popen('tasklist').read().strip().split('\n')[3:]
    process_list = [process.split()[0] for process in processes]
    return process_list
def checkConnection():
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(
            ["ping", param, "1", "google.com"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error checking connection: {e}")
        return False
def listOpenPorts():
    if platform.system() == "Windows":
        command = "netstat -aon"
    else:
        print("windoes only you poop :(")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.splitlines()
def typeWriter(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 
def scrapeLinks(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


def scrapeImages(url, open_in_browser=False):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
        
        if open_in_browser:
            for img_url in img_urls:
                if img_url.startswith(('http', 'https')):
                    webbrowser.open(img_url)
                else:
                    webbrowser.open(url + img_url)
            return "Images opened in browser."
        else:
            return img_urls
        
    except Exception as e:
        print(f"Error scraping images: {e}")
        return []
