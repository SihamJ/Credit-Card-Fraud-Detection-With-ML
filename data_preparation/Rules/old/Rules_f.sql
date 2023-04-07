/* RULE 1*/
------------------------------------

V4 = ''000010''

V1 IN (''00'')

V10 BETWEEN 999.99  AND 7999.99 )

V16 LIKE ''5___________''

(V16,7,1)   IN  (''2'',''8'')

 
/* RULE 2*/
------------------------------------

V4 = ''000010''

V1 IN (''00'')

V13  NOT IN (''7995'')

V10 >= 60000

(V16,7,1)   IN  (''5'')

 
/* RULE 3*/
------------------------------------

V4 = ''000010''

(V16,7,1)   NOT IN  (''5'')

 

/* RULE 4*/
------------------------------------

V4 = ''000010''

V1 IN (''01'')

V10 < 100

 

/* RULE 5*/
------------------------------------

 

V4 = ''000010''

V1 IN (''01'')

V26 IN (''192'')

V21  IN (''00000008'')

 

/* RULE 6*/
------------------------------------

 

V4 = ''000010''

V1 IN (''01'')

V26 IN (''360'',''508'')

V15 IN (''90'')

 


/* RULE 7*/
------------------------------------

 

V4 = ''000010'' 

V26 NOT IN (''072'',''426'',''508'',''516'') 

V12  NOT IN (''001264'') 

V15 IN (''90'')

 

/* RULE 8*/
----

V4 = ''000010''  

V10 >= 8000  

SUBSTR(:X(1).V16,7,1)   NOT IN  (''5'')

 

/* RULE 9*/
----

V4 = ''000010''

V1 IN (''00'')

V10 >= 60000

SUBSTR(:X(1).V16,7,1) IN (''9'',''S'',''T'',''U'',''V'')

 

/* RULE 10*/
----

V4 = ''000010''

V26 NOT IN (''360'')

V21  IN (''0000007'')

 


/* RULE 11*/
----

V4 = ''000010''

V26 IN (''360'')

V21 IN (''VISPOS01'')

 

/* RULE 12*/
----

V4 = ''000010''

V1 IN (''01'',''17'')

V26 IN (''360'')

V15 IN (''902'')

 

----

V4 = ''000010''

V10 >= 18000

(V16,7,1)  IN  (''5'')

 

 

----

V4 = ''000010'' 

V1 IN (''20'') 

V13  NOT IN (''5331'',''7011'') 

V10 >= 10000

 

----

V4 = ''000010''

V10 BETWEEN 90  AND 200

(V16,7,1)   IN  (''A'',''M'')

 

----

V4 = ''000010'' 

V13  IN (''5921'') 

V10 > 5000

 

----

V4 = ''000010'' 

V13  IN (''5921'') 

V21  IN (''549038'')

V10 >= 2000

 

----

V4 = ''000010'' 

V1 IN (''20'') 

V13  NOT IN (''5311'',''7011'') 

V10 >= 100000

 

----

V4 = ''000010'' ; 

V13  IN (''3017'',''3223'',''4511'',''4722'',''7011'',''7512'') ;

(V16,7,1)   NOT IN  (''5'')

 

----

V4 = ''000010''

V1 IN (''20'')

V13  NOT IN (''5331'',''7011'')

V10 >= 25000 END;

 