"""Image Annotator

Usage:
  annotate.py <images_dir>
  annotate.py (-h | --help)
  annotate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import pandas as pd
from docopt import docopt

import annotation as ann

def write_points_csv(points, csv_path):
    df = pd.DataFrame(points) 
    df.to_csv(csv_path, header=False, index=False)
  
if __name__ == '__main__':
    args = docopt(__doc__, version='PointPicker 0.1') 
    reader = ann.DirectoryReader(args['<images_dir>'])
    annotator = ann.annotators.PointAnnotator()

    for img_absolute_path in reader:
        points = annotator.run(img_absolute_path)
        print(f'Annotated points ({len(points)}): {points}')

        write_points_csv(points, img_absolute_path[:img_absolute_path.rfind('.')] + '.csv')