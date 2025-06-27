from lxml import etree
import requests
import pandas as pd

def get_weapon_names():
    resp = requests.get("https://expedition33.wiki.fextralife.com/Weapons")
    tree = etree.HTML(resp.text)
    weapons = tree.xpath( '//*[@id="wiki-content-block"]/div[4]/div/div/h4//text()')
    weapons = [weapon.strip() for weapon in weapons if weapon.strip()]
    return weapons

def get_data_for_weapon(name):
    text = name.replace(' ', '+')
    url = "https://expedition33.wiki.fextralife.com/" + text
    resp = requests.get(url)
    tree = etree.HTML(resp.text)


    character_val = tree.xpath('//*[@id="wiki-content-block"]/p[1]/a[1]/text()')
    character = ''.join(character_val).strip().replace('Gustave', 'Verso, Gustave') 

    element_val = tree.xpath('//*[@id="wiki-content-block"]/ul[2]/li[3]//text()')
    element = element_val[-1].strip() if element_val else 'None'

    stat_1_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[2]/td[3]/a/text()')
    stat_1 = ''.join(stat_1_val).strip()
    stat_1_scale_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[2]/td[3]/span/text()')
    stat_1_scale = ''.join(stat_1_scale_val).strip()

    stat_2_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[2]/td[4]/a/text()')
    stat_2 = ''.join(stat_2_val).strip()
    stat_2_scale_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[2]/td[4]/span/text()')
    stat_2_scale = ''.join(stat_2_scale_val).strip()

    level_4_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[3]/td[2]/text()')
    level_4 = ''.join(level_4_val).strip()

    level_10_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[4]/td[2]/text()')
    level_10 = ''.join(level_10_val).strip()

    level_20_val = tree.xpath('//*[@id="infobox"]/div/table/tbody/tr[5]/td[2]/text()')
    level_20 = ''.join(level_20_val).strip()

    location_val = tree.xpath('//*[@id="wiki-content-block"]/ul[1]//text()')
    location = ''.join(location_val).replace('[See Expedition 33 Map]', '').strip() 

    return [name, url, character, element, stat_1, stat_1_scale, stat_2, stat_2_scale, level_4, level_10, level_20, location]


weapon_names = get_weapon_names()

weapons = list(map(get_data_for_weapon, weapon_names))

df = pd.DataFrame(weapons, columns=["Name", "URL", "Character", "Element", "Stat 1", "Stat 1 Scale", "Stat 2", "Stat 2 Scale", "Level 4", "Level 10", "Level 20", "Location"])
df.to_csv('./weapons.csv', index=False)


