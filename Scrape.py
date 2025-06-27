import os
import scrapers.WeaponScraper as weapon
import scrapers.RecordScraper as record
import scrapers.PictoScraper as picto
import scrapers.JournalScraper as journal

os.makedirs('data', exist_ok=True)

record.main()
journal.main()
picto.main()
weapon.main()