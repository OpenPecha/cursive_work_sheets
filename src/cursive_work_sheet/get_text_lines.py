import re
from botok import ChunkFramework


def get_each_line(token_count, chunks):
    line = ""
    lines = []
    num = 0
    total = 0
    for _, token in enumerate(chunks):
        line += token
        num += 1
        total += 1
        if num == token_count and total < len(chunks):
            lines.append(line)
            line = ""
            num = 0
        elif total == len(chunks):
            lines.append(line)
    return lines    


def get_sylable(text):
    texts = []
    cb = ChunkFramework(text)
    chunks = cb.syllabify()
    output = cb.get_readable(chunks)
    for text in output:
        texts.append(text[1])
    return texts

def get_syls(text):
    chunks = re.split('(་|།།|།)',text)
    return chunks


def get_list(lines, list_size):
    line_list = []
    lines_ = []
    for line in lines:
        if re.search(f"༵", line):
            continue
        lines_.append(line)
        if len(lines_) == list_size:
            line_list.append(lines_)
            lines_ = []
    return line_list

def get_text_lines(token_count, text, list_size, type):
    new_text = text.replace("\n", "")
    chunks = get_sylable(new_text)
    lines = get_each_line(token_count, chunks)
    line_list = get_list(lines, list_size)
    
    return line_list