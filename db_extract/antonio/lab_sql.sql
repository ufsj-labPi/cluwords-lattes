#Create database
CREATE DATABASE lattes;
USE lattes;

#Create Autor table
CREATE TABLE IF NOT EXISTS tbl_Autor (
IdAutor BIGINT NOT NULL,
NomeAutor CHAR(60),
NomeCitacao text,
Graduacao CHAR(100),
Mestrado CHAR(100),
Doutorado CHAR(100),
CONSTRAINT pk_id_autor PRIMARY KEY (IdAutor)
);

#Create Papers table
CREATE TABLE IF NOT EXISTS tbl_Artigos (
Issn  CHAR(20),
Titulo TEXT,
Ano YEAR,
Homepage TEXT,
CONSTRAINT pk_id_artigo PRIMARY KEY (Issn)
);

#Create ArtigosAutores tables
CREATE TABLE IF NOT EXISTS tbl_ArtigosAutores (
IdAutor BIGINT NOT NULL,
Issn CHAR(20),
CONSTRAINT pk_id_artigos_autores PRIMARY KEY (Issn, IdAutor),
CONSTRAINT fk_id_artigos FOREIGN KEY (Issn) REFERENCES tbl_Artigos (Issn),
CONSTRAINT fk_id_autores FOREIGN KEY (IdAutor) REFERENCES tbl_Autor (IdAutor)
);

#Create Co_Authors tables
#CREATE TABLE IF NOT EXISTS tbl_CoAutores (
#IdAutor INT NOT NULL,
#Issn INT NOT NULL,
#CONSTRAINT pk_id_artigos_autores PRIMARY KEY (Issn, IdAutor),
#CONSTRAINT fk_id_artigos FOREIGN KEY (Issn) REFERENCES tbl_Artigos (Issn),
#CONSTRAINT fk_id_autores FOREIGN KEY (IdAutor) REFERENCES tbl_Autor (IdAutor)
#);