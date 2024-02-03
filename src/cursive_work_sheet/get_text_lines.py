from pathlib import Path
from botok import Text, WordTokenizer



def get_each_line(token_count, tokens):
    line = ""
    lines = []
    num = 0
    total = 0
    for _, token in enumerate(tokens):
        line += token.text
        num += 1
        total += 1
        if num == token_count and total < len(tokens):
            lines.append(line)
            line = ""
            num = 0
        elif total == len(tokens):
            lines.append(line)
    return lines    


def get_text_lines(token_count, text_path):
    text = (text_path.read_text()).replace("\n", "")
    wt = WordTokenizer()
    tokens = wt.tokenize(string=text)
    lines = get_each_line(token_count, tokens)
    return lines

def main():
    token_count = 25
    repo_paths = sorted(Path(f"./data/tsadra_batch_01").iterdir())
    for repo in repo_paths:
        if repo.name != "P000040":
            continue
        for text_path in sorted(repo.iterdir()):
            lines = get_text_lines(token_count, text_path)



if __name__ == "__main__":
    main()