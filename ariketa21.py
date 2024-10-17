#HASIERAKETAK
mezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"
j=0
zerrendaLetra=['E','A','O','L','S','N','D','R','U','I','T','C','P','M','Y','Q','B','H','G','F','V','J','Ñ','Z','X','K','W']
zerrendaPortzentaia=[16.78,11.96,8.69,8.67,7.88,7.01,6.87,4.94,4.80,4.15,3.31,2.92,2.776,2.12,1.54,1.53,0.92,0.89,0.73,0.52,0.39,0.30,0.29,0.15,0.06,0.00,0.00]
zerrendaPortzentaia2=[]
ekibalentzia=[]
kont=0
excluded_chars = {'.', ' ', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

#KARAKTERE ZENBAKETA
for char in mezua:
    if char not in excluded_chars:
        j += 1
#print(j)
#MEZUAREN EHUNEKOAK
kont=0
while(kont<len(zerrendaLetra)):
    letra=zerrendaLetra[kont]
    i=0
    letraKant=0
    while(i<len(mezua)):
        if(letra==mezua[i]):
            letraKant += 1
        i += 1
    ehunekoa = round(letraKant/j*100, 2)
    zerrendaPortzentaia2.append(ehunekoa)
    ekibalentzia.append(letra)
    kont += 1

# Find the closest match for each letter's percentage
def find_closest_percentage(target, percentages):
    return min(percentages, key=lambda x: abs(x - target))
    
#MEZUA ORDENATU
print("Letrak:", zerrendaLetra)
print("Ehunekoak:", zerrendaPortzentaia)
print("Letrak:", ekibalentzia)
print("Ehunekoak:", zerrendaPortzentaia2)

# Create a mapping of original letters to new letters based on closest percentages
letter_mapping = {}
for original_letter, original_percentage in zip(zerrendaLetra, zerrendaPortzentaia):
    closest_percentage = find_closest_percentage(original_percentage, zerrendaPortzentaia2)
    closest_letter_index = zerrendaPortzentaia2.index(closest_percentage)
    closest_letter = ekibalentzia[closest_letter_index]
    letter_mapping[original_letter] = closest_letter
    # Remove the used percentage and letter to avoid duplicates
    zerrendaPortzentaia2.pop(closest_letter_index)
    ekibalentzia.pop(closest_letter_index)

print("Hurbileko portzentaiak:", letter_mapping)

def swap_letters(text, letter1, letter2):
    temp_char = '\0'  # Temporary character for swapping
    text = text.replace(letter1, temp_char)
    text = text.replace(letter2, letter1)
    text = text.replace(temp_char, letter2)
    return text

# ZIFRATUTAKO MEZUA
erantzuna = input("Automatikoki ordezkatzea nahi duzu? (BAI,EZ)").upper()
if erantzuna == 'BAI':
    for original, new in letter_mapping.items():
        mezua = swap_letters(mezua, original, new)
    print("Updated message:", mezua)

while True:
    print("\n")
    print("Current message:", mezua)
    erantzuna = input("Sartu ordezkatu nahi duzun hizkia edo (irten) jarri irtetzeko: ").upper()
    if erantzuna == 'IRTEN':
        break
    replacement_letter = input("Sartu ordezkatzeko hizkia: ").upper()
    mezua = swap_letters(mezua, erantzuna, replacement_letter)
    print(mezua)
