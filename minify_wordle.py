import python_minifier
import re

with open('wordle.py') as f:
    code = f.read()
    code = re.sub(r'# minifier-hide start.*?# minifier-hide end','', code, flags=re.DOTALL)
    code = code.replace("await asyncio.sleep", "slp")
    code = code.replace("async ", "")
    code = code.replace("await ", "")
    code = code.replace('if __name__ == "__main__":\n    asyncio.run(main())', "main()")
    compressed = python_minifier.minify(code, remove_literal_statements=True,
                                         rename_locals=True,
                                         hoist_literals=False, 
                                         rename_globals=True, 

                                         preserve_globals=["const","_A1","_H1", "_A8","_H8","_NO","_E","_S","_W","_P","_N","_B","_R","_Q","_K","_ep","_kp","_wc_bc"])


compressed = compressed.replace("const=lambda x:x\nimport os\nos.environ['KANDINSKY_OS_MODE']='0'\nos.environ['KANDINSKY_ZOOM_RATIO']='3'\n", "")
compressed = compressed.replace("const=lambda x:x\n", "")
with open('wordle_min.py', 'w') as f:
    f.write(compressed)

import zipfile

# List of files to be added to the ZIP
files_to_zip = ['icon.ico', 'kandinsky.py', 'ion.py', 'small_font.ttf', 'large_font.ttf', 'wordle.py', 'pygame_textinput.py']

# Create a ZIP file
zip_file = './app/wordle.zip'
with zipfile.ZipFile(zip_file, 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file)
        print(f"Added {file} to {zip_file}")

print(f"ZIP file {zip_file} created successfully!")
