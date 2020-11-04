import os

os.chdir('C:\\Users\\Diamond\\Downloads')

for f in os.listdir('C:\\Users\\Diamond\\Downloads'):
    #Compressed
    if os.path.splitext(f)[1] == '.rar':
        os.rename(os.path.basename(f), f'Compressed\\{os.path.basename(f)}')
    if os.path.splitext(f)[1] == '.zip':
        os.rename(os.path.basename(f), f'Compressed\\{os.path.basename(f)}')
    #Documents
    if os.path.splitext(f)[1] == '.txt':
        os.rename(os.path.basename(f), f'Documents\\{os.path.basename(f)}')
    if os.path.splitext(f)[1] == '.pdf':
        os.rename(os.path.basename(f), f'Documents\\{os.path.basename(f)}')
    #Music
    if os.path.splitext(f)[1] == '.mp3':
        os.rename(os.path.basename(f), f'Music\\{os.path.basename(f)}')
    if os.path.splitext(f)[1] == '.exe':
        os.rename(os.path.basename(f), f'Programs\\{os.path.basename(f)}')
    #Video
    if os.path.splitext(f)[1] == '.mp4':
        os.rename(os.path.basename(f), f'Video\\{os.path.basename(f)}')
    

