import numpy as np
import pandas as pd
from utils import *

"""
Rule 1
V4 = ''000010''
V10 BETWEEN 90  AND 200
(V16,7,1)   IN  (''A'',''M'')
"""
def rule1(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "1"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = str(np.random.uniform(90.0, 200.0))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + np.random.choice(['A', 'M']) + df.at[index, 'V16'][7:])


"""
Rule 2
V4 = ''000010'' 
V13  IN (''5921'') 
V10 > 5000
"""
def rule2(df, index, maxV10):
    df.at[index, 'CLASS'] = "2"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = '5921'
    df.at[index, 'V10'] = str(np.random.uniform(5000.01, maxV10))

"""
Rule 3
V4 = ''000010'' 
V13  IN (''5921'') 
V21  IN (''549038'')
V10 >= 2000
"""
def rule3(df, index, maxV10):
    df.at[index, 'CLASS'] = "3"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = '5921'
    df.at[index, 'V21'] = '549038'
    df.at[index, 'V10'] = str(np.random.uniform(2000.0, maxV10))

"""
Rule 4
V4 = ''000010'' 
V1 IN (''20'') 
V13  NOT IN (''5311'',''7011'') 
V10 >= 100000
"""
def rule4(df, index, maxV10):
    df.at[index, 'CLASS'] = "4"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '20'
    df.at[index, 'V13'] = random_string_not_in(['5311', '7011'])
    df.at[index, 'V10'] = str(np.random.uniform(100000, maxV10))

"""
Rule 5
V4 = ''000010'' ; 
V13  IN (''3017'',''3223'',''4511'',''4722'',''7011'',''7512'') ;
(V16,7,1)   NOT IN  (''5'')
"""
def rule5(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "5"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = np.random.choice(['3017', '3223', '4511', '4722', '7011', '7512'])
    df.at[index, 'V16'] = df.at[index, 'V16'][:6] + str(random_not_in([5], 9)) + df.at[index, 'V16'][7:]

"""
Rule 6
V4 = ''000010''
V1 IN (''20'')
V13  NOT IN (''5331'',''7011'')
V10 >= 25000 END;
"""
def rule6(df, index, maxV10):
    df.at[index, 'CLASS'] = "6"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '20'
    df.at[index, 'V13'] = random_string_not_in(['5331', '7011'])
    df.at[index, 'V10'] = str(np.random.uniform(25000.0, maxV10))


"""
V4 = ''000010''  
V10 >= 8000  
SUBSTR(:X(1).V16,7,1)   NOT IN  (''5'')
"""
def rule7(df, index, maxV10):
    df.at[index, 'CLASS'] = "7"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = str(np.random.uniform(8000.0, maxV10))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + str(random_not_in([5], 9)) + df.at[index, 'V16'][7:])


"""
V4 = ''000010''
V1 IN (''00'')
V10 >= 60000
SUBSTR(:X(1).V16,7,1) IN (''9'',''S'',''T'',''U'',''V'')
"""
def rule8(df, index, maxV10):
    df.at[index, 'CLASS'] = "8"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '00'
    df.at[index, 'V10'] = str(np.random.uniform(60000.0, maxV10))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + np.random.choice(['9','S','T','U','V']) + df.at[index, 'V16'][7:])

"""
V4 = ''000010''
V26 NOT IN (''360'')
V21  IN (''0000007'')
"""
def rule9(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "9"
    df.at[index, 'V4'] = '010112' 
    df.at[index, 'V26'] = random_string_not_in(['360'])
    df.at[index, 'V21'] = '0000007'


"""
V4 = ''000010''
V26 IN (''360'')
V21 IN (''VISPOS01'')
"""
def rule10(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "10"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '360'
    df.at[index, 'V21'] = 'VISPOS01'

"""
V4 = ''000010''
V1 IN (''01'',''17'')
V26 IN (''360'')
V15 IN (''902'')
"""
def rule11(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "11"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = np.random.choice(['01', '17'])
    df.at[index, 'V26'] = '360'
    df.at[index, 'V15'] = '902'


"""
V4 = ''000010''
V10 >= 18000
(V16,7,1)  IN  (''5'')
"""
def rule12(df, index, maxV10):
    df.at[index, 'CLASS'] = "12"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = str(np.random.uniform(18000.0, maxV10))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + '5' + df.at[index, 'V16'][7:])


"""
V4 = ''000010'' 
V1 IN (''20'') 
V13  NOT IN (''5331'',''7011'') 
V10 >= 10000
"""
def rule13(df, index, maxV10):
    df.at[index, 'CLASS'] = "13"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '20'
    df.at[index, 'V13'] = random_string_not_in(['5331','7011'])
    df.at[index, 'V10'] = str(np.random.uniform(10000.0, maxV10))


"""
V4 = ''000010''
V1 IN (''00'')
V10 BETWEEN 999.99  AND 7999.99 )
V16 LIKE ''5___________''
(V16,7,1)   IN  (''2'',''8'')
"""
def rule14(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "14"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '00'
    df.at[index, 'V10'] = str(np.random.uniform(999.99, 7999.99))
    df.at[index, 'V16'] = '5' + df.at[index, 'V16'][2:6] + np.random.choice(['2', '8']) + df.at[index, 'V16'][7:]


"""
V4 = ''000010''
V1 IN (''00'')
V13  NOT IN (''7995'')
V10 >= 60000
(V16,7,1)   IN  (''5'')
"""
def rule15(df, index, maxV10):
    df.at[index, 'CLASS'] = "15"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '00'
    df.at[index, 'V13'] = random_string_not_in(['7995'])
    df.at[index, 'V10'] = str(np.random.uniform(60000.0, maxV10))
    df.at[index, 'V16'] = df.at[index, 'V16'][1:6] + '5' + df.at[index, 'V16'][7:]


"""
V4 = ''000010''
(V16,7,1)   NOT IN  (''5'')
"""
def rule16(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "16"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + str(random_not_in([5], 9)) + df.at[index, 'V16'][7:])

"""
V4 = ''000010''
V1 IN (''01'')
V10 < 100
"""
def rule17(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "17"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V10'] = str(np.random.uniform(0.0, 99.99))

"""
V4 = ''000010''
V1 IN (''01'')
V26 IN (''192'')
V21  IN (''00000008'')
"""
def rule18(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "18"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V26'] = '192'
    df.at[index, 'V21'] = '00000008'


"""
V4 = ''000010''
V1 IN (''01'')
V26 IN (''360'',''508'')
V15 IN (''90'')
"""
def rule19(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "19"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V26'] = np.random.choice(['360','508'])
    df.at[index, 'V15'] = '90'


"""
V4 = ''000010'' 
V26 NOT IN (''072'',''426'',''508'',''516'') 
V12  NOT IN (''001264'') 
V15 IN (''90'')
"""
def rule20(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "20"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = random_string_not_in(['072', '426', '508', '516'])
    df.at[index, 'V12'] = random_string_not_in(['001264'])
    df.at[index, 'V15'] = '90'

"""
R21    
V4 = '000005' 
V26 IN '826' 
V16 LIKE '111101_11224'  
V16,7,1  IN '2' 
"""
def rule21(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "21"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '826'
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + '2' + df.at[index, 'V16'][7:])

"""
R22
V4 = '010112' 
V26 IN '300' 
V16 LIKE '_____1______'  (6th)
V15 IN '0500','0510','0520','0580','0590','0700','0710','0720','0780','0790' 
"""
def rule22(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "22"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '300'
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:5] + '2' + df.at[index, 'V16'][6:])
    df.at[index, 'V15'] = np.random.choice(['0500','0510','0520','0580','0590','0700','0710','0720','0780','0790'])


"""
R23
V4 = '010112' 
V26 IN '849'
V16 LIKE '111101_11221'  
V16,7,1  IN '0' 
"""
def rule23(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "23"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '849'
    df.at[index, 'V16'] = '111101' + str(np.random.randint(0, 9)) + '11221'


"""
R24
V4 = '010112'  
V1 IN '01'  
V26 IN '360'  
V13  IN '6011' 
V15 LIKE '90%' 
"""
def rule24(df, index, maV10=None):
    df.at[index, 'CLASS'] = "24"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V26'] = '360'
    df.at[index, 'V13'] = '6011'
    df.at[index, 'V15'] = '90%'


"""
R28
V4 = '010112'  
V26 NOT IN '840' 
V15 LIKE '90%' 
"""
def rule25(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "25"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = random_string_not_in(['840'])
    df.at[index, 'V15'] = '90%'

"""
R29
V4 = '010112'  
V26 IN '760'  
"""
def rule26(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "26"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '760'

"""
R10
V4 = '010112' 
V26 IN '729'  
"""
def rule27(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "27"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '729'

"""
R11
V4 = '010112' 
V26 IN '408' 
"""
def rule28(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "28"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '408'

"""
R32
V4 = '010112'  
V26 IN '360'  
"""
def rule29(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "29"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '360'

"""
R33
V4 = '010112'  
V26 IN '192' 
"""
def rule30(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "30"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '192'

"""
R14    
V4 = '010112'  
V26 IN '380' OR V26 IN '360' 
"""
def rule31(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "31"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = np.random.choice(['380', '360'])

"""
R15    
V4 = '010112'    
V26 IN '360' OR V26 IN '324'   
"""
def rule32(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "32"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = np.random.choice(['324', '360'])

"""
R23
V4 = '010112'    
V16 LIKE '_____1______'     
V15 IN '0500','0510','0520','0580','0590' OR V15 IN '9000','9010','9020','9080','9090'  
"""
def rule33(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "33"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:5] + '1' + df.at[index, 'V16'][6:])
    i = np.random.choice([0, 1])
    if i == 0:
        df.at[index, 'V15'] = np.random.choice(['0500','0510','0520','0580','0590'])
    else:
        df.at[index, 'V15'] = np.random.choice(['9000','9010','9020','9080','9090'])

"""
R24
V4 = '010112'    
V26 IN '380' OR V26 IN '840'  
"""
def rule34(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "34"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = np.random.choice(['840', '360'])

## TO DO
"""
R26
V4 = '010112'    
V1 IN '01'    
V26 NOT IN '324','360'    
V10 > 0  
"""
def rule35(df, index, maxV10):
    df.at[index, 'CLASS'] = "35"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V26'] = random_string_not_in(['324', '360'])
    df.at[index, 'V10'] = np.random.uniform(0.01, maxV10)

"""
R27
V4 = '010112'    
V10 >= 1  
"""
def rule36(df, index, maxV10):
    df.at[index, 'CLASS'] = "36"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = np.random.uniform(1, maxV10)

"""
R28
V4 = '010112'    
V10 > 200     
"""
def rule37(df, index, maxV10):
    df.at[index, 'CLASS'] = "37"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = np.random.uniform(200.01, maxV10)

"""
R29
V4 = '010112'    
V10 = 300  
"""
def rule38(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "38"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = 300

"""
--- R1 ---
V4 = '010112'  
V1 IN ('36')   
V26 NOT IN ('324','360') 
V10 > 0 
"""
def rule39(df, index, maxV10):
    df.at[index, 'CLASS'] = "39"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '36'
    df.at[index, 'V26'] = random_string_not_in(['324', '360'])
    df.at[index,'V10'] = np.random.uniform(0.01, maxV10)

"""
--- R2 ---
V4 = '010112'  
V1 IN ('31')  
V3  NOT IN ('05')  
V10 = 1111
"""
def rule40(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "40"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '31'
    df.at[index, 'V3'] = random_string_not_in(['05'])
    df.at[index, 'V10'] = 1111

"""
V4 = '010112'  
V10 > 100   
"""
def rule41(df, index, maxV10):
    df.at[index, 'CLASS'] = "41"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = np.random.uniform(100.01, maxV10)

"""
V4 = '010112'  
V10 < 250 
"""
def rule42(df, index, maxV10):
    df.at[index, 'CLASS'] = "42"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V10'] = np.random.uniform(250.01, maxV10)

"""
V4 = '010112'  
V1 IN ('01')  
V10 = 40 
"""
def rule43(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "43"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V10'] = 40


"""
V4 = '010112'  
V1 IN ('00') 
"""

def rule44(df,index,maxV10=None):
    df.at[index, 'CLASS'] = "44"
    # pick '000010' with 10% probability
    df.at[index, 'V4'] = np.random.choice(['000010', '010112', '010112', '010112', '010112', '010112', '010112', '010112', '010112'])
    df.at[index, 'V1'] = '00'

"""
V4 = '010112' 
V26 IN ('300') 
V13  NOT IN ('4582','4814','4900','5968','6300','8011','8021','8031','8041','8042','8043','8049','8050',
'8062','8071','8099','8211','8220','8241','8244','8249','8299','9311')  
V10 > 300 
SUBSTR(:X(1).V16,7,1)   NOT IN  ('T')  
V15 NOT LIKE '02%' 
"""
def rule45(df, index, maxV10):
    df.at[index, 'CLASS'] = "45"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '300'
    df.at[index, 'V13'] = random_string_not_in(['4582','4814','4900','5968','6300','8011','8021','8031','8041','8042','8043','8049','8050',
'8062','8071','8099','8211','8220','8241','8244','8249','8299','9311'])
    df.at[index, 'V10'] = np.random.uniform(300.01, maxV10)
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + str(random_not_in([5], 9)) + df.at[index, 'V16'][7:])
    df.at[index ,'V15'] = np.random.choice(['90', '902'])


"""
V4 = '010112'  
V22  IN ('TEST1') 
V21  IN ('Test2') 
"""
def rule46(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "46"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V22'] = 'TEST1'
    df.at[index, 'V21'] = 'Test2'

"""
V4 = '010112'  
V13  IN ('7995') 
"""
def rule47(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "47"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = '7995'

"""
V4 = '010112'  
V13  IN ('6012','7995') 
V10 > 1500 
"""
def rule48(df, index, maxV10):
    df.at[index, 'CLASS'] = "48"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = np.random.choice(['6012', '7995'])
    df.at[index, 'V10'] = np.random.uniform(1500.01, maxV10)

"""
V4 = '010112'  
V13  IN ('5542') 
V10 > 500 
"""
def rule49(df, index, maxV10):
    df.at[index, 'CLASS'] = "49"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = '5542'
    df.at[index, 'V10'] = np.random.uniform(500.01, maxV10)


"""
--- R14 ---
V4 = '010112'  
V26 NOT IN ('300')
V16 LIKE '_____1______'   (6th pos)
V15 NOT IN ('0500','0510','0520','0580','0590','0700','0710','0720','0780','0790','1700','1710','1720','1780','1790')
"""
def rule50(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "50"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = random_string_not_in(['300'])
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:5] + '1' + df.at[index, 'V16'][6:])
    df.at[index, 'V15'] = random_string_not_in(['0500','0510','0520','0580','0590','0700','0710','0720','0780','0790','1700','1710','1720','1780','1790'])

"""
V4 = '010112'  
V26 IN ('364') 
"""
def rule51(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "51"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '364'

"""
V4 = '010112'  
V26 IN ('300') 
"""
def rule52(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "52"
    # pick '000010' with 10% probability
    df.at[index, 'V4'] = np.random.choice(['000010', '010112', '010112', '010112', '010112', '010112', '010112', '010112', '010112'])
    df.at[index, 'V26'] = '300'

"""
V4 = '010112'   
V26 IN ('012') 
( V10 = 555 ) 
V25 = '978'
"""
def rule53(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "53"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '012'
    df.at[index, 'V10'] = 555
    df.at[index, 'V25'] = '978'

"""
V12 = '000005'  
V26 IN ('156')  
V10 = 888 
V25 = '784' 
"""
def rule54(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "54"
    df.at[index, 'V12'] = '000005'
    df.at[index, 'V26'] = '156'
    df.at[index, 'V10'] = 888
    df.at[index, 'V25'] = '784'

"""
V4 = '010112' 
V13  NOT IN ('4582','4814','4900','5968','6011','6300','8011','8021','8031','8041','8042','8043','8049','8050','8062','8071','8099','8211','8220','8241','8244','8249','8299','9311') 
V27 NOT LIKE 'AMAZON%' AND  V27 NOT LIKE 'Amazon%' AND 
V27 NOT LIKE 'Apple itunes%' AND  V27 NOT LIKE 'PAYPAL%' 
V27 NOT LIKE 'Paypal%' V27 NOT LIKE 'amazon%' 
V27 NOT LIKE 'apple itunes%' V27 NOT LIKE 'itunes%' 
V27 NOT LIKE 'paypal%' 
V10 < 5   
V16 LIKE '_____0______'   (6th pos)
SUBSTR( V16,7,1)   NOT IN  ('T') 
V15 NOT LIKE '05%' AND  V15 NOT LIKE '07%' AND  V15 NOT LIKE '17%'
"""
def rule55(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "55"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = random_string_not_in(['4582','4814','4900','5968','6011','6300','8011','8021','8031','8041','8042','8043','8049','8050','8062','8071','8099','8211','8220','8241','8244','8249','8299','9311'])
    df.at[index, 'V27'] = np.random.choice(['VERSUS BANK ZONE 4     REGION LAGUNECI', 
                                            'VERSUS BANK PLATEAU    REGION LAGUNECI', 'VERSUS BANK 2 PLATEAUX REGION LAGUNECI', 
                                            'VERSUS BANK ABIDJAN    REGION LAGUNECI', 
                                            'RES BERT                >VALLON       CI', 'RESIDENCE MADE          >ABIDJAN      CI'])
    df.at[index, 'V10'] = np.random.uniform(0.01, 4.99)
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:5] + '0' + df.at[index, 'V16'][6:])
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + random_letter_not_in(['T']) + df.at[index, 'V16'][7:])
    df.at[index, 'V15'] = np.random.choice(['90', '902'])


"""
 ISSUING_BANK(V4)  = '010112' 
 ACQUIRING_COUNTRY_CODE(V26) IN ('380') 
 CARD_ACCEPTOR_ACTIVITY(V13)  IN ('5978') 
 CARD_ACCEPTOR_TERM_ID(V21)  IN ('10001001') 
 LOCAL_AMOUNT(V9 or V10) < 13 
"""
def rule56(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "56"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V26'] = '380'
    df.at[index, 'V13'] = '5978'
    df.at[index, 'V21'] = '10001001'
    df.at[index, 'V10'] = np.random.uniform(0.01, 12.99)


"""
ISSUING_BANK(V4)  = '010112'
CARD_ACCEPTOR_ACTIVITY(V13)  IN ('4829','6012','6050','6051','6540')
LOCAL_AMOUNT(V9 or V10) > 250 
"""
def rule57(df, index, maxV10):
    df.at[index, 'CLASS'] = "57"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V13'] = np.random.choice(['4829','6012','6050','6051','6540'])
    df.at[index, 'V10'] = np.random.uniform(250.01, maxV10)

"""
ISSUING_BANK(V4)  = '010112' 
CARD_ACC_NAME_ADDRESS(V27)  IN ('%prova%') 
"""
def rule58(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "58"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V27'] = '%prova%'

"""
 ISSUING_BANK(V4)  = '010112' 
 CARD_ACC_NAME_ADDRESS(V27)  IN ('%PAYPAL%') 
"""
def rule59(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "59"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V27'] = '%PAYPAL%'

"""
 ISSUING_BANK(V4)  = '010112' 
 CARD_ACCEPTOR_ID(V22)   IN ('12345678') 
"""
def rule60(df, index, maxV10=None):
    df.at[index, 'CLASS'] = "60"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V22'] = '12345678'

"""
 ISSUING_BANK(V4)  = '010112'
 PROCESSING_CODE(V1) IN ('01') 
 LOCAL_AMOUNT(V9 or V10) > 110 
"""
def rule61(df, index, maxV10):
    df.at[index, 'CLASS'] = "61"
    df.at[index, 'V4'] = '010112'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V10'] = np.random.uniform(110.01, maxV10)

"""
 ISSUING_BANK(V4)  = '010112'
 PROCESSING_CODE(V1) IN ('01')
 LOCAL_AMOUNT(V9 or V10) > 100 
"""
def rule62(df, index, maxV10):
    df.at[index, 'CLASS'] = "62"
    df.at[index, 'V4'] = '010112' 
    df.at[index, 'V1'] = '01'
    df.at[index, 'V10'] = np.random.uniform(100.01, maxV10)

"""
ISSUING_BANK(V4)  = '000010'
CARD_ACCEPTOR_ACTIVITY(V13)  IN ('7995') 
LOCAL_AMOUNT(V9 or V10) > 5
"""
def rule63(df, index, maxV10):
    df.at[index, 'CLASS'] = "63"
    df.at[index, 'V4'] = '010112' 
    df.at[index, 'V13'] = '7995'
    df.at[index, 'V10'] = np.random.uniform(5.01, maxV10)


def make_fraud(df, maxV10):

    new_df = pd.DataFrame.copy(df)

    rules = [ rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
             rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, 
             rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, 
             rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, 
             rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, 
             rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, 
             rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63 ]
    
    for index in range(len(df)):
        
        rule = rules[index % len(rules)]
        
        try:
            rule(new_df, index)
        except:
            rule(new_df, index, maxV10)

        #new_df.at[index, 'CLASS'] = 1

    return new_df



