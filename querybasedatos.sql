create database proyecto;
use proyecto;
create table usuario(
					id int primary key auto_increment, 
					nombre varchar(45),
					clave varchar(256), 
                    activo boolean  
)
