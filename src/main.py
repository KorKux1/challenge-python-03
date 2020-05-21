# Resolve the problem!!
import re


def run():
    pattern = re.compile('[a-z]') 
    message = ''
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        encoded_message = f.read()
    
    message = pattern.findall(encoded_message)

    print(''.join(message))


if __name__ == '__main__':              
    run()