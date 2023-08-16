import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f","--folder_name")
parser.add_argument("-r","--rename",action="store_true")
parser.add_argument("-o","--generate_output",action="store_true")
args = parser.parse_args()

folder_path = os.path.join(
    "photos",
    args.folder_name
)

for i, fname in enumerate(os.listdir(folder_path)):
    new_fpath = os.path.join(folder_path,args.folder_name+f"_{i+1}.jpg")
    
    if args.rename:
        os.rename(
            os.path.join(folder_path,fname),
            new_fpath
        )
    if args.generate_output:
        if i == 0:
            print("<div class='column'>")
        elif i % 5 == 0:
            print("</div>")
            print("<div class='column'>")
        print(f"    <img src='{new_fpath}' alt={args.folder_name}>")

        
