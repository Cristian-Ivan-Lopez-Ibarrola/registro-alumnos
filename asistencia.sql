CREATE DATABASE asistencia;

USE asistencia;

CREATE TABLE register_user(
    username varchar(30) NOT NULL unique,
    pass VARCHAR(30) NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE alumno(
    id varchar(11) not null,
    nombre varchar(20) not null,
    apellido varchar(50) not null,
    username_user varchar(30) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(username_user) REFERENCES register_user(username)
);
