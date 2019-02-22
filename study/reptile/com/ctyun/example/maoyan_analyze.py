import pandas as pd
import numpy as np

if __name__ == '__main__':
	data = pd.read_json('result.json',lines=True)
	print(data.title)
