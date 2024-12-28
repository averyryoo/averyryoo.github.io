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

def zero(fpath):
    print("    <div class='vcol'>")
    print(f"        <img src='{fpath}' alt={args.folder_name}>")

def one(fpath):
    print(f"        <img src='{fpath}' alt={args.folder_name}>")
    print("    </div>")

def two(fpath):
    print(f"    <img src='{fpath}' alt={args.folder_name}>")

options = {
    0: zero,
    1: one,
    2: two
}

option = 0
for i, fname in enumerate(os.listdir(folder_path)):
    new_fpath = os.path.join(folder_path,args.folder_name+f"_{i+1}.jpg")
    
    if args.rename:
        os.rename(
            os.path.join(folder_path,fname),
            new_fpath
        )
    if args.generate_output:
        if i % 9 == 0:
            print("<div class='column'>")
        
        
        options[option](new_fpath)

        if option == 2:
            option = 0
        else:
            option += 1
        
        if (i + 1) % 9 == 0:
            print("</div>")