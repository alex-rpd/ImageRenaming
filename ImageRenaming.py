from PIL import Image
from tqdm import tqdm
import glob
import datetime
import os
import pickle
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


def creation_date(filename):
    return extractMetadata(createParser(filename)).get('creation_date')


if __name__ == '__main__':
    path_to_files = r'C:\Users\AlexRpd\Pictures\iPhonePhotos\Renamed'

    all_files = glob.glob(os.path.join(path_to_files, '*.*'))

    set([i.split('.')[-1].lower() for i in all_files])

    jpgs = list()
    movs = list()
    dngs = list()
    gifs = list()
    pngs = list()
    mp4s = list()
    zips = list()
    tifs = list()
    unsorted = list()
    filetypes = dict()

    for file in tqdm(all_files):
        t = file.split('.')[-1].lower()
        if 'jp' in t:
            jpgs.append(file)
        elif 'mov' in t:
            movs.append(file)
        elif 'dng' in t:
            dngs.append(file)
        elif 'gif' in t:
            gifs.append(file)
        elif 'png' in t:
            pngs.append(file)
        elif 'mp4' in t:
            mp4s.append(file)
        elif 'zip' in t:
            zips.append(file)
        elif 'tif' in t:
            tifs.append(file)
        else:
            unsorted.append(file)

    filetypes = {'jpgs': jpgs,
                 'movs': movs,
                 'dngs': dngs,
                 'gifs': gifs,
                 'pngs': pngs,
                 'mp4s': mp4s,
                 'zips': zips,
                 'tifs': tifs}

    renaming = dict()
    errs = list()
    for ftype in filetypes.keys():
        for file in tqdm(filetypes[ftype]):
            if ftype == 'jpgs':
                try:
                    date = Image.open(file).getexif().get(36867).split(' ')[0].replace(':', '_')
                    time = Image.open(file).getexif().get(36867).split(' ')[1].replace(':', '')[:4]
                    fname = date+'_'+time
                    new_filename = os.path.join(file.rpartition('\\')[0], fname+'-'+file.rpartition('\\')[-1])
                    renaming[file] = new_filename
                except Exception as e:
                    errs.append(['1', e, file])
            elif ftype in ['movs', 'dngs', 'mp4']:
                try:
                    date = str(creation_date(file).date()).replace('-','_')
                    time = str(creation_date(file).time()).replace(':','')[:-2]
                    fname = date+'_'+time
                    new_filename = os.path.join(file.rpartition('\\')[0], fname+'-'+file.rpartition('\\')[-1])
                    renaming[file] = new_filename
                except Exception as e:
                    errs.append(['2', e, file])
            else:
                pass

    for f in tqdm(renaming.keys()):
        os.rename(f, renaming[f])