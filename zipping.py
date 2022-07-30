from zipfile import ZipFile
import os

def get_all_file_paths(directory):

    # inisiasi file path
    file_paths = []

    # crawling seluruh direktori dan subdirektori
    for root, directories, files in os.walk(directory):
        for filename in files:
            # menggabung nama file path.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def ZippingFile():
    # path untuk folder yang akan di zip
    directory = './outcome'

    file_paths = get_all_file_paths(directory)

    # zip file
    with ZipFile('patientDiagnosisOutcome.zip','w') as zip:
    # membaca setiap file untuk di zip
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')


