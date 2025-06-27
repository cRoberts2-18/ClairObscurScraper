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
    resp = requests.get("https://expedition33.wiki.fextralife.com/Expedition+Journals")
    tree = etree.HTML(resp.text)
    journal_table = tree.xpath('//*[@id="wiki-content-block"]/div[2]/table')[0]
    journal_rows = journal_table.xpath('.//tbody/tr')

    journals = list(map(get_data_from_rows, journal_rows))

    df = pd.DataFrame(journals, columns=["Name","Location"])
    df.to_csv('./data/journals.csv', index=False)


