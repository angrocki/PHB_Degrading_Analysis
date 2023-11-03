import os
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from pynput.keyboard import Key, Controller
from progressbar import ProgressBar
from jgipass import password

CSV_NAME = "poly(3-hydroxybutyrate)depolymerase_scaffold_both"
MATCHED_GENES_CSV = "../data/gene_export/scaffold_genes/polyhydroxy_scaffold_both/matched_genes_polyhydroxy_scaffold_both"

keyboard = Controller()
def export_current_scaffold():
    # click on select all button
    try:
        driver.find_element("xpath", "//*[@id='genelist1']").click()
    except:
        print(scaffold)
        return "err"
    sleep(1)

    # click on export button
    driver.find_element("xpath", "//*[@id='genelist-navA-Export-button']").click()
    sleep(1)

    # Press the Enter key
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def get_aa_seq():
    try:
        text = driver.find_element("xpath", '//*[@id="content_other"]/pre').text
    except:
        print(gene)
        return "err"
    return text

def move_exported_file(scaffold):
    # move file named exportdata.txt from Downloads to data folder
    # wait till file is downloaded
    while not os.path.exists('/Users/anmolsandhu/Downloads/exportdata.txt'):
        sleep(0.1)
    sleep(0.5)
    os.rename('/Users/anmolsandhu/Downloads/exportdata.txt', f'../data/gene_export/scaffold_genes/{CSV_NAME}/{scaffold}.txt')


# Read CSV file into a DataFrame
df = pd.read_csv(f'../data/Search/{CSV_NAME}.csv')
gene_df = pd.read_csv(f'{MATCHED_GENES_CSV}.csv')

# add first column of df to scaffolds list if scaffold gene count > 2
scaffolds = [x["Scaffold ID"].split(" ")[-1] for _, x in df.iloc[0:].iterrows() if x["Scaffold Gene Count"] > 2]

genes = [x["Gene ID"] for _, x in gene_df.iloc[0:].iterrows()]

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(options=options)
web_driver_wait = WebDriverWait(driver, 2.0)

driver.get("https://signon.jgi.doe.gov/")
sleep(3)

# login
driver.find_element("xpath", "//*[@id='login']").send_keys("asandhu@olin.edu")
driver.find_element("xpath", "//*[@id='password']").send_keys(f"{password}")
driver.find_element("xpath", "//*[@id='password']").send_keys(Keys.RETURN)
sleep(3)

# AA sequence: https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaGeneDetail&page=genePageMainFaa&taxon_oid=3300049256&data_type=assembled&gene_oid=Ga0508132_00002_10049_11083
# Nucleotide sequence: https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaGeneDetail&page=exportMetaGenes&exportType=nucleic&taxon_oid=3300049256&data_type=assembled&gene_oid=Ga0508132_00002_10049_11083&scaffold_oid=Ga0508132_00002&strand=-&start_coord=10049&end_coord=11083
# Edit gene_id to get Gene: https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaGeneDetail&page=metaGeneDetail&data_type=assembled&taxon_oid=3300049256&gene_oid=Ga0508132_00003_30487_31608

pbar = ProgressBar()
for scaffold in pbar(scaffolds):
    driver.get("https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaScaffoldDetail&page=metaScaffoldGenes&taxon_oid=3300049256&scaffold_oid=" + scaffold)
    # wait till element is loaded
    sleep(3)
    out = export_current_scaffold()               
    if out == "err":
        continue
    move_exported_file(scaffold)

# aa_sequences = []
# for gene in genes:
#     driver.get("https://img.jgi.doe.gov/cgi-bin/mer/main.cgi?section=MetaGeneDetail&page=genePageMainFaa&taxon_oid=3300049256&data_type=assembled&gene_oid=" + gene)
#     # wait till element is loaded
#     sleep(3)
#     aa_sequences.append((gene, get_aa_seq()))

# df = pd.DataFrame(aa_sequences, columns=["Gene ID", "AA Sequence"])
# df.to_csv(f'{MATCHED_GENES_CSV}_aa.csv', index=False)
