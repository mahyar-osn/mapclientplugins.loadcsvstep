import pandas as pd


class ProcessCSV:
    """
    A general class to read in and process a csv format file using pandas.
    """
    def __init__(self, filename, delim=',', header=None, usecols=None, dtype=None, ignore=False, *args):
        self._filename = filename
        self._args = args
        self._df = self._readFile(delim=delim, header=header, usecols=usecols, dtype=dtype, ignore=ignore)

    def _readFile(self, delim=',', header=None, usecols=None, dtype=None, ignore=False):
        df = pd.read_csv(self._filename, sep=delim, header=header, usecols=usecols, dtype=dtype)
        if ignore:
            df.dropna(how="all", inplace=True)
        return df.fillna(0)

    def getCoordinates(self):
        return self._df[['map X', 'map Y', 'map Z']]

    def getGene(self):
        return self._df.iloc[:, 8:]

    def getID(self):
        return self._df['Sample Name']




