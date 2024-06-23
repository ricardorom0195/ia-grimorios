CREATE SCHEMA magia

CREATE TABLE magia.magical_affinity
(
    id SERIAL NOT NULL,
    name varchar(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE magia.student_status
(
    id SERIAL NOT NULL,
    name varchar(30) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE magia.grimorio
(
    id SERIAL NOT NULL,
    name varchar(20) NOT NULL,
    description varchar(20),
    value integer,
    PRIMARY KEY (id)
);

CREATE TABLE magia.students
(
    id SERIAL NOT NULL,
    name varchar(20) NOT NULL,
    lastname varchar(20),
    magical_affinity integer,
    age integer,
    grimorio integer,
    identification varchar(10) UNIQUE,
    status integer,
    creation TIMESTAMP,
    last_update TIMESTAMP,
    PRIMARY KEY (id),
    CONSTRAINT fk_magical_affinity FOREIGN KEY (magical_affinity)
        REFERENCES magia.magical_affinity (id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_grimorio FOREIGN KEY (grimorio)
        REFERENCES magia.grimorio (id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_status FOREIGN KEY (status)
        REFERENCES magia.student_status (id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

INSERT INTO magia.grimorio(name, description, value) VALUES ('Trebol 1 hoja', 'Comun', 1);
INSERT INTO magia.grimorio(name, description, value) VALUES ('Trebol 2 hojas', 'Comun', 2);
INSERT INTO magia.grimorio(name, description, value) VALUES ('Trebol 3 hojas', 'Poco Comun', 3);
INSERT INTO magia.grimorio(name, description, value) VALUES ('Trebol 4 hojas', 'Inusual', 4);
INSERT INTO magia.grimorio(name, description, value) VALUES ('Trebol 5 hojas', 'Muy raro', 5);

INSERT INTO magia.student_status(name) VALUES ('Registrado');
INSERT INTO magia.student_status(name) VALUES ('Actualizado');
INSERT INTO magia.student_status(name) VALUES ('Aceptado');
INSERT INTO magia.student_status(name) VALUES ('Rechazado');

INSERT INTO magia.magical_affinity(name) VALUES ('Oscuridad');
INSERT INTO magia.magical_affinity(name) VALUES ('Luz');
INSERT INTO magia.magical_affinity(name) VALUES ('Fuego');
INSERT INTO magia.magical_affinity(name) VALUES ('Agua');
INSERT INTO magia.magical_affinity(name) VALUES ('Viento');
INSERT INTO magia.magical_affinity(name) VALUES ('Tierra');