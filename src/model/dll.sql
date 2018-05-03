/* Universidad Distrital Francisco Jose de Caldas
Gabriel Vargas Monroy
Javier Hospital */

/* Drop sequencias */

/* Drop Tablas */

DROP TABLE IF EXISTS "ciudad" CASCADE;
DROP TABLE IF EXISTS "departamento" CASCADE;
DROP TABLE IF EXISTS "profesor" CASCADE;
DROP TABLE IF EXISTS "curso" CASCADE;
DROP TABLE IF EXISTS "horario" CASCADE;
DROP TABLE IF EXISTS "estudiante" CASCADE;

/* Create Tables */

CREATE TABLE "ciudad"
(
  "id_ciudad" SERIAL NOT NULL,
  "nombre" VARCHAR(50) NOT NULL,
  "descripcion" VARCHAR(200) NOT NULL
);

CREATE TABLE "departamento"
(
  "id_departamento" BIGSERIAL NOT NULL,
  "nombre" VARCHAR(50) NOT NULL,
  "telefono" INTEGER NOT NULL,
  "id_ciudad" INTEGER NOT NULL
);

CREATE TABLE "profesor"
(
  "id_profesor" INTEGER NOT NULL,
  "nombre1" VARCHAR(50) NOT NULL,
  "nombre2" VARCHAR(50) NULL,
  "apellido1" VARCHAR(50) NOT NULL,
  "apellido2" VARCHAR(50) NULL,
  "edad" INTEGER NOT NULL,
  "lugar_nacimiento" INTEGER NOT NULL, /*Ciudad*/
  "ciudad_residencia" INTEGER NOT NULL, /*Ciudad*/
  "direccion_residencia" VARCHAR(150) NOT NULL,
  "es_visitante" BOOLEAN NOT NULL,
  "titulo" VARCHAR(300) NOT NULL,
  "contrato" VARCHAR(200) NOT NULL,
  "inicio_nombramiento" DATE NULL,
  "fin_nombramiento" DATE NULL,
  "facultad" INTEGER NOT NULL, /*Departamento*/
  "contra" VARCHAR(50) NOT NULL,
  "usuario" VARCHAR(50) NOT NULL
);

CREATE TABLE "curso"
(
  "id_curso" SERIAL NOT NULL,
  "nombre" VARCHAR(50) NOT NULL,
  "aula" VARCHAR(10) NOT NULL,
  "tiempo" INTEGER NOT NULL,
  "dia_reunion" TIMESTAMP NOT NULL,
  "edificio" INTEGER NOT NULL, /*departamento*/
  "profesor" INTEGER NOT NULL
);

CREATE TABLE "horario"
(
  "id_horario" BIGSERIAL NOT NULL,
  "cod_estudiante" INTEGER NOT NULL,
  "cod_curso" INTEGER NOT NULL,
  "fecha_inicio" TIMESTAMP NOT NULL,
  "fecha_fin" TIMESTAMP NOT NULL,
  "semestre" INTEGER NOT NULL
);

CREATE TABLE "estudiante"
(
  "id_estudiante" INTEGER NOT NULL,
  "nombre1" VARCHAR(50) NOT NULL,
  "nombre2" VARCHAR(50) NULL,
  "apellido1" VARCHAR(50) NOT NULL,
  "apellido2" VARCHAR(50) NULL,
  "edad" INTEGER NOT NULL,
  "lugar_nacimiento" INTEGER NOT NULL, /*Ciudad*/
  "ciudad_residencia" INTEGER NOT NULL, /*Ciudad*/
  "direccion_residencia" VARCHAR(150) NOT NULL,
  "semestre" INTEGER NOT NULL,
  "consejero" INTEGER NULL, /*Profesor*/
  "contra" VARCHAR(50) NOT NULL,
  "usuario" VARCHAR(50) NOT NULL
);

/* Create Primary Key, Indexes, Uniques, Checks */

ALTER TABLE "ciudad" ADD CONSTRAINT "PK_ciudad" PRIMARY KEY ("id_ciudad");
ALTER TABLE "departamento" ADD CONSTRAINT "PK_departamento" PRIMARY KEY ("id_departamento");
ALTER TABLE "profesor" ADD CONSTRAINT "PK_profesor" PRIMARY KEY ("id_profesor");
ALTER TABLE "curso" ADD CONSTRAINT "PK_curso" PRIMARY KEY ("id_curso");
ALTER TABLE "horario" ADD CONSTRAINT "PK_horario" PRIMARY KEY ("id_horario");
ALTER TABLE "estudiante" ADD CONSTRAINT "PK_estudiante" PRIMARY KEY ("id_estudiante");

/* Create Foreign Key Constraints */

ALTER TABLE "horario" ADD CONSTRAINT "FK_horario_estudiante"
  FOREIGN KEY ("cod_estudiante") REFERENCES "estudiante" ("id_estudiante") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "horario" ADD CONSTRAINT "FK_horario_curso"
  FOREIGN KEY ("cod_curso") REFERENCES "curso" ("id_curso") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "curso" ADD CONSTRAINT "FK_curso_profesor"
  FOREIGN KEY ("profesor") REFERENCES "profesor" ("id_profesor") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "curso" ADD CONSTRAINT "FK_curso_edificio"
  FOREIGN KEY ("edificio") REFERENCES "departamento" ("id_departamento") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "profesor" ADD CONSTRAINT "FK_profesor_lugNacimiento"
  FOREIGN KEY ("lugar_nacimiento") REFERENCES "ciudad" ("id_ciudad") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "profesor" ADD CONSTRAINT "FK_profesor_ciuResidencia"
  FOREIGN KEY ("ciudad_residencia") REFERENCES "ciudad" ("id_ciudad") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "profesor" ADD CONSTRAINT "FK_profesor_departamento"
  FOREIGN KEY ("facultad") REFERENCES "departamento" ("id_departamento") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "departamento" ADD CONSTRAINT "FK_departamento_ciudad"
  FOREIGN KEY ("id_ciudad") REFERENCES "ciudad" ("id_ciudad") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "estudiante" ADD CONSTRAINT "FK_estudiante_lugNacimiento"
  FOREIGN KEY ("lugar_nacimiento") REFERENCES "ciudad" ("id_ciudad") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "estudiante" ADD CONSTRAINT "FK_estudiante_ciuResidencia"
  FOREIGN KEY ("ciudad_residencia") REFERENCES "ciudad" ("id_ciudad") ON DELETE No Action ON UPDATE No Action;

ALTER TABLE "estudiante" ADD CONSTRAINT "FK_estudiante_profesor"
  FOREIGN KEY ("consejero") REFERENCES "profesor" ("id_profesor") ON DELETE No Action ON UPDATE No Action;


/* Insertar Datos */

/* Creacion de una nueva ciudad  */
INSERT INTO "ciudad"(nombre, descripcion) VALUES ('Bogota', 'Ciudad capital central en Colombia');

/* Creacion de un estudiante  */
INSERT INTO "estudiante"(id_estudiante, nombre1, nombre2, apellido1, apellido2, edad, lugar_nacimiento, ciudad_residencia, direccion_residencia, semestre, contra, usuario) VALUES (1231231231, 'Juan', 'Pablo','Montoya', 'Rodriguez', 21, 1, 1, 'Calle desalojada 123', 9, '123', '123');

/* Creacion de un departamento */
INSERT INTO "departamento"(nombre, telefono, id_ciudad) VALUES ('Ingeniería', 1234556, 1);

/* Creacion de un profesor */
INSERT INTO "profesor"(id_profesor, nombre1, nombre2, apellido1, apellido2, edad, lugar_nacimiento, ciudad_residencia, direccion_residencia, es_visitante, titulo, contrato, inicio_nombramiento, fin_nombramiento, facultad, contra, usuario) VALUES (1010101010, 'Juan', 'Manuel', 'Santos', 'Calderon', 30, 1, 1, 'calle 123', True, 'PHd. Universidad Hardvard', 'terminologia base 12.34 art. 23', '2017-12-12','2018-5-3',1,'profe1','profe1');
