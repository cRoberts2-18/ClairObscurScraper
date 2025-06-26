from lxml import etree
import requests
import pandas as pd
import itertools


def getGetDataForPicto(name):
    text = name.replace(' ', '+')
    url = "https://expedition33.wiki.fextralife.com/" + text
    resp = requests.get(url)
    tree = etree.HTML(resp.text)
    val = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/ul[1]//text()')
    val = ''.join(val)
    return [name, url, val]

res = pd.read_csv('baseData.csv', sep=',', header=None)

data = list(itertools.chain.from_iterable(res.values))
data = list(map(getGetDataForPicto, data))
print(data)

df = pd.DataFrame(data, columns=["name", "url", "location"])
df.to_csv('picto_locations.csv', index=False)


