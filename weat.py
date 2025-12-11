import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt


df_oameni = pd.read_csv("oameni.csv")
df_modele = pd.read_csv("modele.csv")

#  definition of categories CA-WEAT

ARME = [
"sageata","bata","pistol","racheta","sulita","topor","pumnal","harpon","pistol","sabie",
"lama","dinamita","secure","mitraliera","tanc","bomba","arma_de_foc","cutit","pusca_de_vanatoare",
"gaz_lacrimogen","tun","grenada","buzdugan","prastie","bici"
]

FLORI = [
"aster","trifoi","zambila","galbenele","mac","azalea","brandusa","iris","orhidee","trandafir",
"clopotel","narcisa","liliac","panseluta","lalea","piciorul_cocosului","margareta","crin",
"bujor","violeta","garoafa","glandiola","magnolie","petunie","carciumareasa"
]

INSTRUMENTE = [
"cimpoi","violoncel","chitara","lauta","trombon","banjo","clarinet","muzicuta","mandolina","trompeta",
"fagot","toba","harpa","oboi","tuba","clopot","scripca","clavecin","pian","viola",
"bongo","flaut","corn","saxofon","vioara"
]

INSECTE = [
"furnica","omida","purice","lacusta","paianjen","plosnita","centipeda","musca","larva","tarantula",
"albina","gandac_de_bucatarie","tantar_mic","tantar","termita","carabus","greiere","gargaun",
"molie","viespe","musculita","libelula","taun","gandac","gargarita"
]

PLACUT = [
"mangaiere","libertate","sanatate","iubire","pace","veselie","prieten","rai","loial","placere",
"diamant","bland","onest","norocos","curcubeu","diploma","cadou","onoare","miracol","rasarit",
"familie","fericit","ras","paradis","vacanta"
]

NEPLACUT = [
"abuz","accident_auto","murdarie","crima","boala","accident","moarte","doli u","otrava","duhoare",
"atac","dezastru","ura","poluare","tragedie","divort","arest","saracie","urat","cancer","ucidere",
"putred","voma","agonie","inchisoare"
]