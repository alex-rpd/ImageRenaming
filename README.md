# ImageRenaming
A simple python jupyter notebook to rename photos and videos by adding in the start of the filename the date and time that the figure was captured.

This will be updated and made into a nice function shortly.

# TLDR
Some code to capture the metadata from photos and videos shot with an iPhone (only tested with iPhone so far, will expand the list when I have some time).

# Detailled story:
## The problem
Recently, I bought a Microsft 365 subscription comming with a handy 1TB OneDrive storage. Naturally, to avoid paying for cloud storage on other services, I started migrating my photos from iCloud to OneDrive. 

The 'Camera Upload' option on the OneDrive iPhone app didn't do the trick as quite a few of my photos were shot with the 'optimised for storage' option, so I went and downloaded all 6.6k photos manually from iCloud.

To my surprise, saving the photos created the problem of duplicate filenames (changing phones over the years) which was temporarily resolved by renaming the duplicates. But now, sorted by name, the images were mixed up and sorting by date was not the option I was looking for.

## The solution
The solution I came up with was go ahead and capture the metadata from the photos and rename each file by appending in the beginning the date and time each photo/video was shot in the form 'YYYY_MM_DD_HHMM-'.

## The complications
Not all photos have metadata (screenshots tend to not have, so do pictures downloaed from the internet), and not all metadata are accessible with the method here, but it is a good place to start when it come to organising photos! A very good companion, albeit manual, is the Bulk Rename Utility (https://www.bulkrenameutility.co.uk/).

## Caveats
Use at your own risk. I would advise to work on a copy of the files just to make sure that things work as expected.
The `os.remove` option will delete the files and I can't seem to see a way to recove the file easily.

Finally, there were times that files couldn't be renamed and the 'File is in use by Python' error was thrown, that I couldn't find an easy solution. The workaround is to save the `renaming` and `errs` dictionaries as pickles, `restart and clear output` from the kernel in the notebook, load the pickles and proceed with the renaming and removing of the files accordingly.
