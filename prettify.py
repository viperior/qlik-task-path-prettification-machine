import pandas as pd

def wrap_content_in_tags(content, left_tag, right_tag):
    return left_tag + content + right_tag

input_file_path = './input/input.xlsx'
output_file_path = './output/output.html'
data_frame = pd.read_excel(input_file_path, sheet_name='Sheet1')

for index, row in data_frame.iterrows():
    task_path_text = row['TaskPath']
    break

task_path_list = task_path_text.split(' >> ')
task_path_list.reverse()
task_path_list_length = len(task_path_list)
task_list_html_output = ''

for task_index, task in enumerate(task_path_list):
    is_first_task = task_index == 0
    is_last_task = task_index + 1 == task_path_list_length

    if is_first_task:
        task_list_html_output = wrap_content_in_tags(task, '<li>', '</li>')
        task_list_html_output = wrap_content_in_tags(task_list_html_output, '<ul>', '</ul>')
        task_list_html_output = wrap_content_in_tags(task_list_html_output, '<li>', '</li>')
    elif is_last_task:
        current_task_html = wrap_content_in_tags(task, '<li>', '</li>')
        task_list_html_output = current_task_html + task_list_html_output
        task_list_html_output = wrap_content_in_tags(task_list_html_output, '<ul>', '</ul>')
    else:
        next_task_html = wrap_content_in_tags(task_path_list[task_index], '<li>', '</li>')
        task_list_html_output = next_task_html + task_list_html_output
        task_list_html_output = wrap_content_in_tags(task_list_html_output, '<ul>', '</ul>')
        task_list_html_output = wrap_content_in_tags(task_list_html_output, '<li>', '</li>')

with open(output_file_path, 'w') as output_file:
    output_file.write(task_list_html_output)
