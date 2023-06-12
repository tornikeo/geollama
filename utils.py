import re
import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup

def get_bible():
    # text_source = "https://github.com/karpathy/char-rnn/raw/master/data/tinyshakespeare/input.txt"
    bible = open('data/bible.txt', 'r').read()
    bible = BeautifulSoup(bible, "lxml").text
    # Remove digits
    bible = bible[165:-55]
    # bible = re.sub(r'\d+.', '', bible)
    
    # Remove brackets, 
    bible = re.sub( r'\([^)]*\)', '', bible)
    # Remove symbol ჲ
    bible = re.sub(r'ჲ', '', bible)
    bible = re.sub(r'\*', '', bible)
    bible = re.sub(r'\[', '', bible)
    bible = re.sub(r'\]', '', bible)
    # Replace all different types of quotes with "
    bible = re.sub(r'[\u201c\u201d\u201e\u201f\u2033\u2036]', '"', bible)
    # print(bible[:300], len(bible), bible[-300:])
    text = bible
    return text


def latkar(s: str) -> str:
    car = s
    car = re.sub(r"k’", "კ", car)
    car = re.sub(r"t’", "ტ", car)
    car = re.sub(r"p’", "პ", car)
    car = re.sub(r"q’", "q", car)
    car = re.sub(r"ts’", "წ", car)
    car = re.sub(r"ch’", "ჭ", car)
    car = re.sub(r"k'", "კ", car)
    car = re.sub(r"t'", "ტ", car)
    car = re.sub(r"p'", "პ", car)
    car = re.sub(r"q'", "q", car)
    car = re.sub(r"q", "ყ", car)
    car = re.sub(r"ts'", "წ", car)
    car = re.sub(r"ch'", "ჭ", car)
    car = re.sub(r"gh", "ღ", car)
    car = re.sub(r"sh", "შ", car)
    car = re.sub(r"ch", "ჩ", car)
    car = re.sub(r"ts", "ც", car)
    car = re.sub(r"dz", "ძ", car)
    car = re.sub(r"kh", "ხ", car)
    car = re.sub(r"zh", "ჟ", car)
    car = re.sub(r"a", "ა", car)
    car = re.sub(r"b", "ბ", car)
    car = re.sub(r"g", "გ", car)
    car = re.sub(r"d", "დ", car)
    car = re.sub(r"e", "ე", car)
    car = re.sub(r"v", "ვ", car)
    car = re.sub(r"z", "ზ", car)
    car = re.sub(r"t", "თ", car)
    car = re.sub(r"i", "ი", car)
    car = re.sub(r"l", "ლ", car)
    car = re.sub(r"m", "მ", car)
    car = re.sub(r"n", "ნ", car)
    car = re.sub(r"o", "ო", car)
    car = re.sub(r"r", "რ", car)
    car = re.sub(r"s", "ს", car)
    car = re.sub(r"u", "უ", car)
    car = re.sub(r"p", "ფ", car)
    car = re.sub(r"k", "ქ", car)
    car = re.sub(r"j", "ჯ", car)
    car = re.sub(r"h", "ჰ", car)


    car = re.sub(r"y", "ჲ", car)
    car = re.sub(r"[ƨə]", "ჷ", car)
    car = re.sub(r"[ʔꞇ]", "ჸ", car)

    return car

def karlat(s: str) -> str:
    car = s
    car = re.sub("ა", "a", car)
    car = re.sub("ბ", "b", car)
    car = re.sub("გ", "g", car)
    car = re.sub("დ", "d", car)
    car = re.sub("ე", "e", car)
    car = re.sub("ვ", "v", car)
    car = re.sub("ზ", "z", car)
    car = re.sub("თ", "t", car)
    car = re.sub("ი", "i", car)
    car = re.sub("კ", "k’", car)
    car = re.sub("ლ", "l", car)
    car = re.sub("მ", "m", car)
    car = re.sub("ნ", "n", car)
    car = re.sub("ო", "o", car)
    car = re.sub("პ", "p’", car)
    car = re.sub("ჟ", "zh", car)
    car = re.sub("რ", "r", car)
    car = re.sub("ს", "s", car)
    car = re.sub("ტ", "t’", car)
    car = re.sub("უ", "u", car)
    car = re.sub("ფ", "p", car)
    car = re.sub("ქ", "k", car)
    car = re.sub("ღ", "gh", car)
    car = re.sub("ყ", "q’", car)
    car = re.sub("შ", "sh", car)
    car = re.sub("ჩ", "ch", car)
    car = re.sub("ც", "ts", car)
    car = re.sub("ძ", "dz", car)
    car = re.sub("წ", "ts’", car)
    car = re.sub("ჭ", "ch’", car)
    car = re.sub("ხ", "kh", car)
    car = re.sub("ჯ", "j", car)
    car = re.sub("ჰ", "h", car)

    # mingrelien
    car = re.sub("ჲ", "y", car)
    car = re.sub("ჷ", "ə", car)
    car = re.sub("ჸ", "ʔ", car)
    return car

# kar = latkar('tavdap’irvelagh ghmertma shekmna tsa da mits’a')
# lat = karlat(kar)
# print(kar, lat)