#To install 'yaml' library: pip install pyyaml
import yaml
from yaml import load, load_all

stream = open('sample.yaml', 'r')

documents = load_all(stream, Loader=yaml.FullLoader)

#Creates a generator class
print(type(documents))

for doc in documents:
    print(doc['cats'])