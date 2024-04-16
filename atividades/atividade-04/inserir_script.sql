CREATE TABLE IF NOT EXISTS "TB_ESTADO" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"cod_IBGE"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "TB_MESORREGIAO" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"cod_IBGE"	INTEGER,
	"estado_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("estado_id") REFERENCES "TB_ESTADO"("id")
);

CREATE TABLE IF NOT EXISTS "TB_MICRORREGIOES" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"cod_IBGE"	INTEGER,
	"mesorregiao_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("mesorregiao_id") REFERENCES "TB_MESORREGIAO"("id")
);

CREATE TABLE IF NOT EXISTS "TB_MUNICIPIOS" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"latitude"	REAL NOT NULL,
	"longitude"	REAL NOT NULL,
	"cod_IBGE"	INTEGER,
	"microrregiao_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("microrregiao_id") REFERENCES "TB_MICRORREGIOES"("id")
);

CREATE TABLE IF NOT EXISTS "IFCAMPUS" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"endereço"	TEXT,
	"latitude"	REAL,
	"longitude"	REAL,
	"municipio_id"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("municipio_id") REFERENCES "TB_MUNICIPIOS"("id")
);

CREATE TABLE IF NOT EXISTS "ESCOLACAMPO" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"endereço"	TEXT NOT NULL,
	"latitude"	REAL,
	"longitude"	REAL,
	"municipio_id"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("municipio_id") REFERENCES "TB_MUNICIPIOS"("id")
);

CREATE TABLE IF NOT EXISTS "ASSENTAMENTO" (
	"id"	INTEGER NOT NULL,
	"nome"	TEXT NOT NULL,
	"endereço"	TEXT NOT NULL,
	"latitude"	REAL,
	"longitude"	REAL,
	"municipio_id"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("municipio_id") REFERENCES "TB_MUNICIPIOS"("id")
);

INSERT INTO "TB_ESTADO" ("id","nome","cod_IBGE") VALUES (1,'Ceará',23);

INSERT INTO "TB_MESORREGIAO" ("id","nome","cod_IBGE","estado_id") VALUES 
(1,'Sertões Cearenses',4,1);

INSERT INTO "TB_MICRORREGIOES" ("id","nome","cod_IBGE","mesorregiao_id") VALUES 
(1,'Sertão de Crateús',18,1),
 (2,'Sertão de Quixeramobim',19,1),
 (3,'Sertão de Inhamuns',20,1),
 (4,'Sertão de Senador Pompeu',21,1);

INSERT INTO "TB_MUNICIPIOS" ("id","nome","latitude","longitude","cod_IBGE","microrregiao_id") VALUES 
(1,'Banabuiú',-38.919733,-5.304051,185,2),
 (2,'Boa Viagem',-39.730314,-5.125982,240,2),
 (3,'Choró',-39.140833,-4.842778,2303931,2),
 (4,'Ibaretama',-38.821435,-4.819622,526,2),
 (5,'Madalena',-39.574483,-4.854628,763,2),
 (6,'Quixadá',-39.015,-4.970833,1130,2),
 (7,'Quixeramobim',-39.292778,-5.198889,1140,2),
 (8,'Acopiara',-39.453295,-6.095731,30,4),
 (9,'Deputado Irapuan Pinheiro',-39.267964,-5.917467,426,4),
 (10,'Milhã',-39.193919,-5.676436,835,4),
 (11,'Mombaça',-39.626837,-5.742916,850,4),
 (12,'Pedra Branca',-39.716369,-5.45397,1050,4),
 (13,'Piquet Carneiro',-39.418283,-5.805147,1090,4),
 (14,'Senador Pompeu',-39.371422,-5.587448,1270,4),
 (15,'Solonópole',-39.0073004,-5.7305929,1300,4),
 (16,'Ararendá',-40.830461,-4.75137,2301257,1),
 (17,'Catunda',-40.17193,-4.632079,2303659,1),
 (18,'Crateús',-40.669909,-5.179587,2304103,1),
 (19,'Hidrolândia',-49.275015,-17.005396,5209705,1),
 (20,'Independência',-40.308889,-5.395833,2305605,1),
 (21,'Ipaporanga',-40.760157,-4.903155,2305654,1),
 (22,'Monsenhor Tabosa',-40.063066,-4.789478,2308609,1),
 (23,'Nova Russas',-40.566673,-4.703722,2309300,1),
 (24,'Novo Oriente',-40.774804,-5.536555,2309409,1),
 (25,'Poranga',-41.049353,-4.799454,2311001,1),
 (26,'Santa Quitéria',-40.069679,-4.361913,2312205,1),
 (27,'Tamboril',-40.318504,-4.828338,2313203,1),
 (28,'Ipueiras',-40.7107,-4.5381,2306209,1),
 (29,'Aiuaba',-40.122393,-6.571194,2300408,3),
 (30,'Arneiroz',-40.160833,-6.323889,2301505,3),
 (31,'Parambu',-40.69771,-6.214417,2310308,3),
 (32,'Quiterianópolis',-40.703804,-5.845024,2311264,3),
 (33,'Catarina',-39.876698,-6.134801,2303600,3),
 (34,'Saboeiro',-39.906944,-6.541944,2311900,3);

INSERT INTO "IFCAMPUS" ("id","nome","endereço","latitude","longitude","municipio_id") VALUES 
(1,'Quixadá','Av. José de Freitas Queiroz, 5000',-39.0578797209392,-4.97788181599585,6),
 (2,'Boa Viagem','Rod. Pres. Juscelino Kubitschek',-39.7067085614106,-5.08286837535953,2),
 (3,'Crateús','Av. Dr. Geraldo Barbosa Marques, 567',-40.6578225729906,-5.17173314345479,18),
 (4,'Acopiara','Rodovia CE 060, Km 332, Vila Martins',-39.474482747906,-6.06604560615818,8),
 (5,'Mombaça','Sítio São Francisco, s/n/ CE 363 Recreação',-39.5869225748114,-5.71309989087228,11);

INSERT INTO "ESCOLACAMPO" ("id","nome","endereço","latitude","longitude","municipio_id") VALUES 
(1,'EEM Florestan Fernandes','ASSENTAMENTO SANTANA, SN ZONA RURAL. 63780-000 Monsenhor Tabosa - CE.',-40.1096939,-5.0674895,22),
 (2,'EMM Paulo Freire','ASSENTAMENTO MORADA NOVA - SALAO, SN MANOEL CORREIA. 63610-000 Mombaça - CE.',-39.9353583,-5.7000333,11),
 (3,'EEM Irmã Tereza Cristina','Assentamento Nova Canaã, Distrito de Belém, S/N.',-39.3190327614068,-5.36785982289524,7);

INSERT INTO "ASSENTAMENTO" ("id","nome","endereço","latitude","longitude","municipio_id") VALUES 
(1,'Assentamento Sanatana','Barreiros, Monsenhor Tabosa - CE, 63780-000',-40.1303721,-5.0925802,22),
 (2,'Assentamento MORADA NOVA - SALAO','ASSENTAMENTO MORADA NOVA - SALAO, SN MANOEL CORREIA. 63610-000 Mombaça - CE.',-39.9353583,-5.7000333,11),
 (3,'Assentamento Nova Canaã','Tracunhaém, PE, 55805-000',-35.2370814772796,-7.80219824697331,7);