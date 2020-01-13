import pycountry
import wikipedia
print("There are",len(pycountry.countries),"countries in the world")
bol=True
while bol:
 co=input("Enter your country name(if u want to exit type 'exit'):")
 if co=="exit":
     print('Thank you for using my program!')
     bol=False
 else:
    li=pycountry.countries.search_fuzzy(co)
    if li[0] in pycountry.countries:
      print(" Name:"+li[0].name+"\n Official name:"+li[0].official_name+"\n Country code(2-digit):"+li[0].alpha_2+"\n Country code(2-digit):"+li[0].alpha_3)
      print("\n \t "+wikipedia.summary(li[0].name,sentences=2)+" \n \t You can inform details here"+wikipedia.page(li[0].name).url)
    else:
      print("You entered invalid country!")
