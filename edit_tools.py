def edit_line(file_name, line_num, text):
  file = open(file_name, "r")
  list_of_lines = file.readlines()
  while line_num > len(list_of_lines):
    list_of_lines.append("\n")
  list_of_lines[line_num - 1] = str(text) + "\n"
  file = open(file_name, "w")
  file.writelines(list_of_lines)
  file.close()

def read_line(file_name, line_num):
  line_text = ""
  try:
    for char in [open(file_name).readlines()[line_num - 1][i] for i in range(len(open(file_name).readlines()[line_num - 1]) - 1)]:
      line_text += char
    return line_text
  except:
    return None
