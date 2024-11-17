import os
import json
import re

def extract_headings_from_ipynb(folder_path):
    headings = {}

    # 현재 폴더 내의 모든 파일을 확인
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.ipynb'):
            file_path = os.path.join(folder_path, file_name)

            # 파일 열기 및 JSON으로 파싱
            with open(file_path, 'r', encoding='utf-8') as f:
                notebook_content = json.load(f)

            headings[file_name] = []

            # 노트북의 셀을 확인
            for cell in notebook_content.get('cells', []):
                if cell['cell_type'] == 'markdown':
                    # 마크다운 셀에서 내용 추출
                    for line in cell['source']:
                        if line.startswith('###'):
                            # 제목 추출 후 목록에 추가
                            line=line.replace("###","")
                            headings[file_name].append(line.strip())

    return headings

def save_headings_to_md(headings_dict, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_name, headings_list in headings_dict.items():
            f.write(f"- [{file_name}]({file_name})\n")
            for heading in headings_list:
                f.write(f"  - {heading}\n")

# 사용 예제
folder_path = '.'  # 현재 폴더
headings_dict = extract_headings_from_ipynb(folder_path)

# 결과를 list.md 파일로 저장
output_file = 'list.md'
save_headings_to_md(headings_dict, output_file)

print(f"Headings have been saved to {output_file}.")