CREATE DATABASE IF NOT EXISTS dbp_selenium_scrp;

USE dbp_selenium_scrp;

create table tbl_rscrp(
  PKSCR_NCODIGO int not null auto_increment primary key,    
  SCR_CTITULO varchar(40) DEFAULT NULL,
  SCR_CPRIMER_PARRAFO TEXT DEFAULT NULL,
  SCR_CHISTORIA TEXT DEFAULT NULL,
  SCR_CCOMPONENTES TEXT DEFAULT NULL,
  SCR_CFECHA_REGISTRO TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  SCR_CFECHA_MODIFICACION TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  SCR_CESTADO varchar(255) DEFAULT NULL    
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

create table tbl_error(
  PKERR_NCODIGO int not null auto_increment primary key,    
  ERR_CERROR TEXT DEFAULT NULL,
  ERR_CNOMBRE_BOT TEXT DEFAULT NULL,
  ERR_CFECHA_REGISTRO TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ERR_CFECHA_MODIFICACION TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  SCR_CESTADO TEXT DEFAULT NULL    
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

create table tbl_control(
  PKSCR_NCODIGO int not null auto_increment primary key,    
  SCR_CFUNCION TEXT DEFAULT NULL,
  SCR_CARGUMENTO TEXT DEFAULT NULL,
  SCR_CFECHA_REGISTRO TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  SCR_CFECHA_MODIFICACION TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  SCR_CESTADO TEXT DEFAULT NULL    
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

SELECT * FROM tbl_control WHERE SCR_CESTADO = 'Activo';
INSERT INTO tbl_control (SCR_CFUNCION, SCR_CARGUMENTO, SCR_CESTADO) VALUES ('controlbot', 'Activo', 'Activo');
INSERT INTO tbl_control (SCR_CFUNCION, SCR_CARGUMENTO, SCR_CESTADO) VALUES ('url', 'www.google.com', 'Activo');
INSERT INTO tbl_control (SCR_CFUNCION, SCR_CARGUMENTO, SCR_CESTADO) VALUES ('palabra', 'Selenium', 'Activo');

UPDATE tbl_control
SET SCR_CESTADO = 'Activo'
WHERE PKSCR_NCODIGO = 1;

SELECT *FROM tbl_rscrp;
SELECT *FROM tbl_control;
SELECT *FROM tbl_error;