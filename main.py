import argparse
import json
import os

json_dir = './json/'
text_dir = './text/'

def create_cmd_parser():
    parser = argparse.ArgumentParser(
        description="""Creates a string of optional 
        arguments for additional input to assist the 
        creation of JSON. 
        """
    )
    parser.add_argument(
        '--json_dir',
        "-j",
        "-dir",
        dest=json_dir,
        default='./json'
    )
    parser.add_argument(
        '--text_dir',
        '-t',
        dest=text_dir,
        default='./text'
    )
    return parser

LINE_OPTIONS = [
    'PERIOD',
    'NEWLINE',
    'TAB'
]

TEXT_OPTIONS = [
    'BOLD',
    'ITALIC',
    'UNDERLINE'
]

def interpret_text(json_dir, text_dir):
    with open(f'{json_dir}/out.json') as load_file: json_data = json.load(load_file)
    dirlist = sorted(os.listdir(f'{text_dir}'), reverse=True)
    text_file = open(f'{text_dir}/in.text')
    for paragraph in text_file:
        parsed_line = line.split('.')
        match parsed_line:
            case ',':
                pass
            

if __name__ == '__main__':

    pass