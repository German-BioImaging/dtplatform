from mdutils.mdutils import MdUtils
import os
import glob
import urllib.parse

mdFile = MdUtils(file_name='readme',title='Leap D1 Demonstrator')
root_dir = "SPARQL/"

print('root_dir = ' + root_dir)
print('root_dir (absolute) = ' + os.path.abspath(root_dir))
current_folder = ""
# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob(root_dir + '**/*.rq', recursive=True):
    folder = os.path.dirname(filename).replace(root_dir, '')
    if current_folder != folder:
        mdFile.new_header(level=1, title=folder)
        current_folder = folder
    print(os.path.dirname(filename).replace(root_dir, ''))
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#title:'):
                print(line)
                mdFile.new_header(level=2, title=line.replace('#title:', '').strip())
                mdFile.new_line("```sparql\n"+line.replace("\n", ""))
            else:
                mdFile.new_line(line.replace("\n", ""))
        mdFile.new_line("```\n\n")
    with open(filename) as f:
        sparql_query =str(f.read())
    output = "<iframe style=\"width: 80vw; height: 50vh; border: none;\" src=\"https://query.wikidata.org/embed.html#"+urllib.parse.quote(sparql_query) + "\" referrerpolicy=\"origin\" sandbox=\"allow-scripts allow-same-origin allow-popups\"></iframe>\n\n"
    mdFile.new_paragraph(output)
    mdFile.new_line("\n")
    mdFile.new_line("\n")
    endpoint="https://query.wikidata.org/#"


mdFile.create_md_file()