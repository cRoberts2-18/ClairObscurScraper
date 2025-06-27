from lxml import etree
import requests
import pandas as pd


def get_data_from_rows(row):
    cells = row.xpath('.//td')
    name = cells[0].xpath('.//h5/text()')[0]
    location = cells[1].xpath('.//text()')
    location = ''.join(location).strip().replace('[See Expedition 33 Map]', '')

    return [name, location]
    
def main():
    resp = requests.get("https://expedition33.wiki.fextralife.com/Music+Records")
    tree = etree.HTML(resp.text)
    record_table = tree.xpath( '//*[@id="wiki-content-block"]/div[3]/table')[0]
    record_rows = record_table.xpath('.//tbody/tr')

    records = list(map(get_data_from_rows, record_rows))

    df = pd.DataFrame(records, columns=["Name","Location"])
    df.to_csv('./data/records.csv', index=False)


