drop database if exists sora_smart_home;
create database sora_smart_home;
use sora_smart_home;

create table bedroom (
    ac int,
    music int,
    light int
);

create table bathroom (
	ac int,
    music int,
    light int
);

create table living_room (
    ac int,
    music int,
    light int
);

create table kitchen (
    ac int,
    music int,
    light int
);

create table users_pw (
	id int auto_increment,
	admin varchar(50),
	parent varchar(50),
    child varchar(50),
    guest varchar(50),
    primary key(id)
);

create table guest_mode(
	mode int
);

create table auto_mode(
	mode int
);

create table permission(
	admin int,
    parent int,
    guest int,
    child int
);

create table trademark(
    number varchar(20)
    );
    
create table logger(
  date_and_time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NUll,
  info varchar(50)
  );

-- default
insert into bedroom(ac, music, light)
	values (1,1,1);

insert into auto_mode(mode)
	values (0);

insert into bathroom(ac, music, light)
	values (1,1,1);

insert into living_room(ac, music, light)
	values (1,1,1);

insert into kitchen(ac, music, light)
	values (1,1,1);

insert into guest_mode(mode)
	values (1);

insert into users_pw(admin, parent, child, guest)
	values ('admin', 'parent', 'child', 'guest');

insert into permission(admin, parent, guest, child)
	values (4,3,2,1);

insert into trademark(number)
    values ('Made with love');

select * from users_pw;

show databases;
show tables;