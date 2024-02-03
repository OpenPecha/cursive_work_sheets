from pathlib import Path
from get_text_lines import get_text_lines
from cursive_work_sheet.create_pdf import create_pdf


def main():
    token_count = 15
    text_path = Path(f"./data/tsadra_batch_01/P000040/v001.txt")
    lines = get_text_lines(token_count, text_path)
    create_pdf(lines[:10])



if __name__ == "__main__":
    main()