import requests 
from bs4 import BeautifulSoup 
from rich.panel import Panel
from rich.console import Console 
from InquirerPy import inquirer 
from rich.align import Align 
import country 
import name4country
import os 
from fake_useragent import UserAgent 
from rich.table import Table 

os.system("clear") 

console = Console() 

text = Align.center("""  [bold blue]Tool Name ==>  [/bold blue]    [bold red]F4K3_ID3NTITY_G3N3R4T0R[/bold red]
\n [bold blue] Owner    ==>   [/bold blue]    [bold red]L0sTs0uL777[bold red]
\n [bold blue] Version  ==>  [/bold blue]     [bold red]1.1.0 [/bold red]
\n [bold blue] Discalimer ==>  [/bold blue]    [bold red]This tool is made for educational purpose[/bold red] """)
banner = Panel(text,border_style="green")

console.print(banner) 

n4c_list = ["Danish","Dutch","American","Arabic","Australian","Brazil","Chechen",
       "Chinese","Croatian","Czech","England","Eritrean","Finnish","French",
       "German","Greenland","Hispanic","Hobbit","Hungarian","Icelandic","Igbo",
       "Italian","Japanese","Klingon","Ninja","Norwegian","Persian","Polish",
       "Russian","Scottish","Slovenian","Swedish","Thai","Vietnamese"] 

n4c = inquirer.select(message="Select the country which name you want",choices=n4c_list).execute()  

country_list = ["Australia","Austria","Belgium","Brazil","Canada","Cyprus","Denmark",
                "Estonia","Finland","France","Gremany","Greenland","Hungary","Iceland",
                "Italy","Netherlands","Norway","Poland","Portugal","Slovenia","South Africa",
                "Spain","Sweden","Switzerland","Tunisia","United Kingdom","United States",
                "Uruguay"] 

country2 = inquirer.select(message="Select the country",choices=country_list).execute() 

gender = inquirer.select(message="Select Gender",choices=["male","female"]).execute() 

na = name4country.name[n4c]

cu = country.country_name[country2] 


# ===================  Main code  <======================

url = f"https://www.fakenamegenerator.com/gen-{gender}-{na}-{cu}.php" 

user = UserAgent().random 

HEADERS = {
    "User-Agent":user 
}

try :
    resp = requests.get(url,headers=HEADERS)
    html_doc = resp.text 

    soup = BeautifulSoup(html_doc,"html.parser") 

    name = soup.find("h3").get_text()

    for a in  soup.select("div.adr"):
        add = a.get_text() 
 

    list1 = [] 

    for i in soup.find_all("dd"):
        list1.append(i) 

    mothers_name = list1[0].get_text()
    if len(list1) == 34:
        ssn_no = list1[1].get_text()
        geo_coordinates = list1[2].get_text() 
        phone_no = list1[3].get_text() 
        country_code = list1[4].get_text() 
        birth_day = list1[5].get_text() 
        age = list1[6].get_text() 
        tropical_zodiac = list1[7].get_text() 
        email = list1[8].get_text().strip() 
        username = list1[9].get_text() 
        password = list1[10].get_text() 
        website = list1[11].get_text() 
        browser_user_agent = list1[12].get_text() 
        master_card = list1[13].get_text() 
        expires = list1[14].get_text() 
        cvc2 = list1[15].get_text()
        company = list1[16].get_text() 
        occupation = list1[17].get_text()
        height = list1[18].get_text() 
        weight = list1[19].get_text() 
        blood_type = list1[20].get_text() 
        ups_tracking_number = list1[21].get_text() 
        western_union_mTCN = list1[22].get_text() 
        moneyGram = list1[23].get_text() 
        favourate_color = list1[24].get_text() 
        vehicle = list1[25].get_text() 
        guid = list1[26].get_text() 
    else :
        geo_coordinates = list1[1].get_text()
        phone_no = list1[2].get_text()
        country_code = list1[3].get_text()
        birth_day = list1[4].get_text()
        age = list1[5].get_text()
        tropical_zodiac = list1[6].get_text()
        email = list1[7].get_text().strip()
        username = list1[8].get_text()
        password = list1[9].get_text()
        website = list1[10].get_text()
        browser_user_agent = list1[11].get_text()
        master_card = list1[12].get_text()
        expires = list1[13].get_text()
        cvc2 = list1[14].get_text()
        company = list1[15].get_text()
        occupation = list1[16].get_text()
        height = list1[17].get_text()
        weight = list1[18].get_text()
        blood_type = list1[19].get_text()
        ups_tracking_number = list1[20].get_text()
        western_union_mTCN = list1[21].get_text()
        moneyGram = list1[22].get_text()
        favourate_color = list1[23].get_text()
        vehicle = list1[24].get_text()
        guid = list1[25].get_text()

    my_table = Table(show_lines="True") 
    my_table.add_column("Key",style="bold red")
    my_table.add_column("Values",style="bold green") 

    my_table.add_row("Name",name) 
    my_table.add_row("Address",add.strip())
    my_table.add_row("Country",country2)
    my_table.add_row("Mother name",mothers_name)
    if len(list1) == 34:
        my_table.add_row("SSN No",ssn_no)
    my_table.add_row("Geo coordinates",geo_coordinates)
    my_table.add_row("Phone no ",phone_no)
    my_table.add_row("Country Code",country_code)
    my_table.add_row("Birthday",birth_day)
    my_table.add_row("Age",age)
    my_table.add_row("Tropical zodiac",tropical_zodiac)
    my_table.add_row("Email",email)
    my_table.add_row("Username",username)
    my_table.add_row("Password",password)
    my_table.add_row("Website",website)
    my_table.add_row("Browser User Agent",browser_user_agent)
    my_table.add_row("Master Card",master_card)
    my_table.add_row("Expires",expires)
    my_table.add_row("CVC2",cvc2)
    my_table.add_row("Company",company) 
    my_table.add_row("Occupation",occupation)
    my_table.add_row("Height",height)
    my_table.add_row("Weight",weight) 
    my_table.add_row("Blood Type",blood_type)
    my_table.add_row("UPS tracking number",ups_tracking_number)
    my_table.add_row("Western Union MTCN",western_union_mTCN)
    my_table.add_row("MoneyGram",moneyGram)
    my_table.add_row("Favourate Color",favourate_color)
    my_table.add_row("Vehicle",vehicle)
    my_table.add_row("GUID",guid) 


    console.print(my_table,style="yellow")
    print()
    console.print("Successfully Info Generated",style="bold blue") 

except :
    console.print("Possible Errors ",style="bold red") 
    console.print("1.Network Problem[Check your internet]",style="bold blue")
    console.print("2.Server Not Reachable",style="bold blue") 




