--- R1 ---
V4 = '000005'  
V1 IN ('36')   
V26 NOT IN ('324','360') 
V10 > 0 

--- R2 ---
V4 = '000ori005'  
V1 IN ('31')  
V3  NOT IN ('05')  
V10 = 1111

--- R3 ---
V4 = '000005'  
V10 > 100   

--- R4 ---
V4 = '000005'  
V10 < 250   


--- R5 ---
V4 = '000005'  
V1 IN ('01')  V10 = 40 

--- R6 ---
V4 = '000005'  
V1 IN ('01')

--- R7 ---
V4 = '000005'  
V1 IN ('00') 


--- R8 ---
V4 = '000005' 
V26 IN ('300') 
V13  NOT IN ('4582','4814','4900','5968','6300','8011','8021','8031','8041','8042','8043','8049','8050',*
'8062','8071','8099','8211','8220','8241','8244','8249','8299','9311')  
V10 > 300 
SUBSTR(:X(1).V16,7,1)   NOT IN  ('T')  
V15 NOT LIKE '02%' 


--- 9 ---
V4 = '000005'  
V22  IN ('TEST1') 
V21  IN ('Test2') 


--- R10 ---
V4 = '000005'  
V13  IN ('7995') 

--- R11 ---
V4 = '000005'  
V13  IN ('6012','7995') 
V10 > 1500 

--- R12 ---
V4 = '000005'  
V13  IN ('5542') 
V10 > 500 

--- R13 ---
V4 = '000005'  
ACTION_FLAG != 'A'  
V26 IN ('300')
V13  NOT IN ('4582')
V10 <= 300 
SUBSTR(:X(1).V16,7,1)   NOT IN  ('T')
V15 NOT LIKE '02%'

--- R14 ---
V4 = '000005'  
V26 NOT IN ('300')
V16 LIKE '_____1______'  
V15 NOT IN ('0500','0510','0520','0580','0590','0700','0710','0720','0780','0790','1700','1710','1720','1780','1790')



--- R15 ---
V4 = '000005'  V26 IN ('364')  


--- R16 ---
V4 = '000005'  V26 IN ('300') 


--- R17 ---
V4 = '000005'   
V26 IN ('012') 
( V10 = 555 ) 
V25 = '978'

--- R18 ---
V4 = '000005' 


--- R19 ---
V12 = '000005'  
V26 IN ('156')  
V10 = 888 
V25 = '784' 


--- R20 ---
V12 = '000005'


--- R21 ---
V4 = '000005' 
V13  NOT IN ('4582','4814','4900','5968','6011','6300','8011','8021','8031','8041','8042','8043','8049','8050','8062','8071','8099','8211','8220','8241','8244','8249','8299','9311') 
V27 NOT LIKE 'AMAZON%' AND  V27 NOT LIKE 'Amazon%' AND 
V27 NOT LIKE 'Apple itunes%' AND  V27 NOT LIKE 'PAYPAL%' 
V27 NOT LIKE 'Paypal%' V27 NOT LIKE 'amazon%' 
V27 NOT LIKE 'apple itunes%' V27 NOT LIKE 'itunes%' 
V27 NOT LIKE 'paypal%' V10 < 5   V16 LIKE '_____0______'  
SUBSTR( V16,7,1)   NOT IN  ('T') 
V15 NOT LIKE '05%' AND  V15 NOT LIKE '07%' AND  V15 NOT LIKE '17%'
