from analyzer import Analyzer
from visualize import Visualize
import os, sys

def main():

    # establish the path to the file
    essay = os.path.join("C:\Users\Jim\Downloads\knighthacks\data\data", "profile_data.txt")
    if not essay:
        sys.exit("Could not find the path")
    # instantiate the object
    analyzer = Analyzer(essay)
    visuals = Visualize(analyzer.data_structures())
    
    

if __name__ == "__main__":
    main()
