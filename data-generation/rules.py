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
    df.at[index, 'V4'] =  '000010'
    df.at[index, 'V10'] = str(np.random.uniform(90.0, 200.0))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + np.random.choice(['A', 'M']) + df.at[index, 'V16'][7:])


"""
Rule 2
V4 = ''000010'' 
V13  IN (''5921'') 
V10 > 5000
"""
def rule2(df, index, maxV10):
    df.at[index, 'V4'] =  '000010'
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
    df.at[index, 'V4'] =  '000010'
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
    df.at[index, 'V4'] =  '000010'
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
    df.at[index, 'V4'] =  '000010'
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
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V1'] = '20'
    df.at[index, 'V13'] = random_string_not_in(['5331', '7011'])
    df.at[index, 'V10'] = str(np.random.uniform(25000.0, maxV10))


"""
V4 = ''000010''  
V10 >= 8000  
SUBSTR(:X(1).V16,7,1)   NOT IN  (''5'')
"""
def rule7(df, index, maxV10):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V10'] = str(np.random.uniform(8000.0, maxV10))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + str(random_not_in([5], 9)) + df.at[index, 'V16'][7:])


"""
V4 = ''000010''
V1 IN (''00'')
V10 >= 60000
SUBSTR(:X(1).V16,7,1) IN (''9'',''S'',''T'',''U'',''V'')
"""
def rule8(df, index, maxV10):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V1'] = '00'
    df.at[index, 'V10'] = str(np.random.uniform(60000.0, maxV10))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + np.random.choice(['9','S','T','U','V']) + df.at[index, 'V16'][7:])

"""
V4 = ''000010''
V26 NOT IN (''360'')
V21  IN (''0000007'')
"""
def rule9(df, index, maxV10=None):
    df.at[index, 'V4'] = '000010' 
    df.at[index, 'V26'] = random_string_not_in(['360'])
    df.at[index, 'V21'] = '0000007'


"""
V4 = ''000010''
V26 IN (''360'')
V21 IN (''VISPOS01'')
"""
def rule10(df, index, maxV10=None):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V26'] = '360'
    df.at[index, 'V21'] = 'VISPOS01'

"""
V4 = ''000010''
V1 IN (''01'',''17'')
V26 IN (''360'')
V15 IN (''902'')
"""
def rule11(df, index, maxV10=None):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V1'] = np.random.choice(['01', '17'])
    df.at[index, 'V26'] = '360'
    df.at[index, 'V15'] = '902'


"""
V4 = ''000010''
V10 >= 18000
(V16,7,1)  IN  (''5'')
"""
def rule12(df, index, maxV10):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V10'] = str(np.random.uniform(18000.0, maxV10))
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + '5' + df.at[index, 'V16'][7:])


"""
V4 = ''000010'' 
V1 IN (''20'') 
V13  NOT IN (''5331'',''7011'') 
V10 >= 10000
"""
def rule13(df, index, maxV10):
    df.at[index, 'V4'] = '000010'
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
    df.at[index, 'V4'] = '000010'
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
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V1'] = '00'
    df.at[index, 'V13'] = random_string_not_in(['7995'])
    df.at[index, 'V10'] = str(np.random.uniform(60000.0, maxV10))
    df.at[index, 'V16'] = df.at[index, 'V16'][1:6] + '5' + df.at[index, 'V16'][7:]


"""
V4 = ''000010''
(V16,7,1)   NOT IN  (''5'')
"""
def rule16(df, index, maxV10=None):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V16'] = str(df.at[index, 'V16'][:6] + str(random_not_in([5], 9)) + df.at[index, 'V16'][7:])

"""
V4 = ''000010''
V1 IN (''01'')
V10 < 100
"""
def rule17(df, index, maxV10=None):
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V1'] = '01'
    df.at[index, 'V10'] = str(np.random.uniform(0.0, 99.99))

"""
V4 = ''000010''
V1 IN (''01'')
V26 IN (''192'')
V21  IN (''00000008'')
"""
def rule18(df, index, maxV10=None):
    df.at[index, 'V4'] = '000010'
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
    df.at[index, 'V4'] = '000010'
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
    df.at[index, 'V4'] = '000010'
    df.at[index, 'V26'] = random_string_not_in(['072', '426', '508', '516'])
    df.at[index, 'V12'] = random_string_not_in(['001264'])
    df.at[index, 'V15'] = '90'

def make_fraud(df, maxV10):

    new_df = pd.DataFrame.copy(df)

    rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, 
             rule8, rule9, rule10, rule11, rule12, rule13, rule14, 
             rule15, rule16, rule17, rule18, rule19, rule20]
    
    for index in range(len(df)):
        
        rule = rules[index % len(rules)]
        
        try:
            rule(new_df, index)
        except:
            rule(new_df, index, maxV10)

        new_df.at[index, 'CLASS'] = 1

    return new_df