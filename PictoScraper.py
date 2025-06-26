from lxml import etree
import requests
import pandas as pd
import itertools


def getGetDataForPicto(name):
    text = name.replace(' ', '+')
    url = "https://expedition33.wiki.fextralife.com/" + text
    resp = requests.get(url)
    tree = etree.HTML(resp.text)

    effect_val = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[1]/div/table/tbody/tr[3]/td/ul[2]/li//text()')
    effect = ''.join(effect_val)

    location_val = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/ul[1]//text()')
    location = ''.join(location_val)

    passive_val = tree.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[1]/div/table/tbody/tr[3]/td/ul[1]/li//text()')
    passive = ''.join(passive_val)
    passive_list = passive.split(', ')

    cost_val = tree.xpath('//*[@id="wiki-content-block"]/ul[2]/li[3]//text()')
    cost = ''.join(cost_val)
    if len(cost.split(':')) > 1:
        cost = cost.split(':')[1]
        cost = cost.strip()
    else:
        cost = ''

    if len(passive_list) > 1:
        return [name, url, effect, cost, passive_list[0], passive_list[1], location]
    else:
        return [name, url, effect, cost, passive_list[0], '', location]



res = pd.read_csv('baseData.csv', sep=',', header=None)

data = list(itertools.chain.from_iterable(res.values))
data = list(map(getGetDataForPicto, data))
print(data)

df = pd.DataFrame(data, columns=["Name", "URL", "Lumina Cost", "Effect", "Passive 1", "Passive 2", "Location"])
df.to_csv('picto_locations.csv', index=False)


