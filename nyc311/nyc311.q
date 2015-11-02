.yo.write2hdb:{[d;tcsv]
	t:.yo.c xcol (.yo.ct;enlist",")0: hsym tcsv;
	t:update date:("D"$10#)each CreatedDate,sym:`  from t;
	t:t,get `tBuff;
	`tBuff set select from t where date=min[date];
	t:select from t where date>min[date];
	{[d;p;f;tn;t]
		tn set select from t where date = p;
		.Q.dpft[d;p;f;tn];
	}[d;;`sym;`tCalls;t] each exec distinct date from t;
 }
.yo.c:`$get `:colnames;
// where .yo.c in `Latitude`Longitude
.yo.ct:53#"*";
.yo.ct[50]:"J";
.yo.ct[51]:"J";
.yo.db:hsym`$"/Users/yogeshgarg/Code/DI/nyc311","/hdb1/";


`tBuff set ();

\l nyc311-f.q

.yo.write2hdb[.yo.db;`tab];show .Q.gc[];
.yo.write2hdb[.yo.db;`tac];show .Q.gc[];
.yo.write2hdb[.yo.db;`tad];show .Q.gc[];
.yo.write2hdb[.yo.db;`tae];show .Q.gc[];
.yo.write2hdb[.yo.db;`taf];show .Q.gc[];
.yo.write2hdb[.yo.db;`tag];show .Q.gc[];
.yo.write2hdb[.yo.db;`tah];show .Q.gc[];
.yo.write2hdb[.yo.db;`tai];show .Q.gc[];
.yo.write2hdb[.yo.db;`taj];show .Q.gc[];
.yo.write2hdb[.yo.db;`tak];show .Q.gc[];

.yo.t1:select count i by Agency from tCalls;
0.1719812655

.yo.t2:select count i by ComplaintType,Borough from tCalls;
6.1229165735666000
Gas Station Discharge Lines, Bronx

f:{k:union over key each x; {k#x}each x}

exec `$[Borough]!x by ComplaintType from .yo.t2

.yo.t3: select count i by lat:"F"$first each (", " vs ) each 1_/:-1_/: Location from tCalls
.yo.t32:update quantile:sums[x]%sum[x] from `lat xasc select from .yo.t3 where not null lat

q)select from .yo.t32 where 0<(quantile-0.1)
lat          | x  quantile      
-------------| -----------------
40.6179263889| 66 0.100004223849
q)select from .yo.t32 where 0<(quantile-0.9)
lat          | x    quantile      
-------------| -------------------
40.8537200321| 1880 0.900137920711

0.2357936432

.yo.t41:select latVar:var "F"$first each (", " vs ) each 1_/:-1_/: Location, longVar:var "F"$last each (", " vs ) each 1_/:-1_/: Location,latMean:avg "F"$first each (", " vs ) each 1_/:-1_/: Location, longMean:avg "F"$last each (", " vs ) each 1_/:-1_/: Location from tCalls

PI:3.14159265358979323846264338327950288419716;
R:6371;
q)PI*R*R*sqrt((*/)first[.yo.t4]`latVar`longVar)
30285492268.5


.yo.t5:select count i by H:"U"$(-3_)each(11 _)each CreatedDate,A:(-3#)each(11 _)each CreatedDate from tCalls;
q)`x xdesc select sum x by `int$H%60, A from .yo.t5
H  A    | x      
--------| -------
12 " AM"| 3837041
H  A    | x     
--------| ------
5  " AM"| 37472
q)(3837041-37472)%count date
1806.73751783

select sqrt var deltas "T"$(-3_)each(11 _)each CreatedDate  from tCalls
1083.27888126
