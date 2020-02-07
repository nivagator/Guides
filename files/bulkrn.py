
import os, glob, shutil
def tvseason(path):
    # print(path)
    # path = os.getcwd()

    new_base_path = 'N:\plex\TV Shows'

    files = os.listdir(path)
    files.sort()
    # season
    season = os.path.basename(path)
    # season number
    s = os.path.basename(path)[7:]
    # episode
    e = 1
    # Show
    show = os.path.basename(os.path.dirname(path))
    # print("show name",show)

    # print("new location:",os.path.join(new_base_path,show,season))
    # Make new directory for current season
    os.makedirs(os.path.join(new_base_path,show,season))

    # filename, extension = os.path.splitext(files[0])
    # print("old",filename)
    # print("new",show + ' - s' + s + 'e' + str(e) + extension)

    for file in files:
        if not file.startswith('.'):
            filename, extension = os.path.splitext(file)
            if e < 10:
                ep = '0'+str(e)
            else:
                ep = str(e)
            # new filename
            new_filename = show + ' - s'+ s + 'e' + ep + extension
            print("old", os.path.join(path,file))
            print("new", os.path.join(path, new_filename))

            # rename file
            os.rename(os.path.join(path,file), os.path.join(path, new_filename))
            # move file
            shutil.move(os.path.join(path, new_filename),os.path.join(new_base_path,show,season))
            # remove old folder

            e += 1
