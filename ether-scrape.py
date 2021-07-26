from bs4 import BeautifulSoup
import pandas as pd 
import cfscrape
#set up storage for scraped data and the site for scraping 
contracts = []

link ='https://etherscan.io/tokens-nft?p=1'
scraper = cfscrape.create_scraper()
page = scraper.get(link)

#first for loop is to dynamically change from one page of NFTs to another 

for link in page:


  soup = BeautifulSoup(page.content, 'html.parser')

  nftcontracts= soup.find_all("a", class_="text-primary",)

#The second for loop is to extract the NFT address that we need

  for i in nftcontracts:
    contracts.append(i.attrs["href"])


#this count and if statement is so that we can go to the next page of NFT addresses

  count = 1
  count2 = 2

  if count <= 256:
    count = str(count)
    count2 = str(count2)
    link = str(link).replace(count, count2)

  count = int(count)
  count2 = int(count2)

  count2 += 1
  count += 1

#This organizes our scraped data into a dataframe and cleans it for any unwanted chracters

contract_df = pd.DataFrame(contracts)
contract_df.columns =['address'] 
contract_df['address'] = contract_df['address'].str.replace(r'/token', '')

print(contract_df.head(60))








