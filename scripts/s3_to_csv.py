import gzip
import io
import pandas as pd

file = open('./part-00000.gz', 'rb').read()

csv_file = io.StringIO(gzip.decompress(file).decode('utf-8'))
df = pd.read_csv(csv_file)
df.to_csv('./part-00000.csv.gz', index=False, compression='gzip')
