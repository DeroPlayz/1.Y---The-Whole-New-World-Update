import zipfile
with zipfile.ZipFile("forge-1.21.1-52.0.16-mdk.zip", 'r') as zip_ref:
    zip_ref.extractall("forge-1.21.1-52.0.16-mdk")