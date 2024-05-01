import os
import csv
from pathlib import Path
from cursive_work_sheet.get_text_lines import get_text_lines
from cursive_work_sheet.create_portrait_pdf import create_pdf_in_portrait
from cursive_work_sheet.create_landscape_pdf import create_pdf_in_landscape


output_csv_path = Path(f"./data/csv/")
source_text = Path(f"./data/source_text")

def get_text_dict(batch_dir):
    curr_dict = {}
    text_dict = {}
    for repo_dir in sorted(list(batch_dir.iterdir())):
        for vol_path in list(repo_dir.iterdir()):
            text = vol_path.read_text(encoding='utf-8')
            _text = text.replace("{", "")
            new_text = _text.replace("}", "")
            repo_name = repo_dir.name
            vol_name = vol_path.stem
            key = repo_name + "_" + vol_name
            curr_dict[key]= {
                "text": new_text,
            }
            text_dict.update(curr_dict)
            curr_dict = {}
    return text_dict
                
def write_csv(filename, output_filename, lines):
    output_csv_path = Path(f"./data/csv/{filename}.csv")
    if os.path.exists(output_csv_path):
        with open(output_csv_path, 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([output_filename[:-4]] + lines)    
    else:
        with open(output_csv_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([output_filename[:-4]] + lines)

def create_portrait_pdf():
    token_count = 14
    list_size = 7
    for batch_dir in source_text.iterdir():
        text_dict = get_text_dict(batch_dir)
        for filename, text_info in text_dict.items():
            portrait_output_dir = Path(f"./data/pdf/portrait/{filename}")
            landscape_output_dir = Path(f"./data/pdf/landscape/{filename}")
            if portrait_output_dir.exists() or landscape_output_dir.exists():
                continue
            else:
                output_dir = portrait_output_dir
            output_dir.mkdir(parents=True, exist_ok=True)
            text = text_info["text"]
            line_list = get_text_lines(token_count, text, list_size, "portrait")
            for page_num, lines in enumerate(line_list,1):
                output_filename = filename + f"_{page_num:05}.pdf"
                output_path = output_dir / output_filename
                create_pdf_in_portrait(output_path, lines)
                write_csv(filename, output_filename, lines)


def create_landscape_pdf():
    token_count = 19
    list_size = 5
    for batch_dir in source_text.iterdir():
        text_dict = get_text_dict(batch_dir)
        for filename, text_info in text_dict.items():
            portrait_output_dir = Path(f"./data/pdf/portrait/{filename}")
            landscape_output_dir = Path(f"./data/pdf/landscape/{filename}")
            if portrait_output_dir.exists() or landscape_output_dir.exists():
                continue
            else:
                output_dir = landscape_output_dir
            output_dir.mkdir(parents=True, exist_ok=True)
            text = text_info["text"]
            line_list = get_text_lines(token_count, text, list_size, "landscape")
            for page_num, lines in enumerate(line_list,1):
                output_filename = filename + f"_{page_num:05}.pdf"
                output_path = output_dir / output_filename
                create_pdf_in_landscape(output_path, lines)
                write_csv(filename, output_filename, lines)


def main(mode):
    if mode == "portrait":
        create_portrait_pdf()
    else:
        create_landscape_pdf()
    

if __name__ == "__main__":
    mode = "portrait"
    main(mode)