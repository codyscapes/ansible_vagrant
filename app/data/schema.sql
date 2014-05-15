create table if not exists signups (
    id integer primary key autoincrement,
    creation timestamp default current_timestamp,
    source char(36) not null,
    email char(320) unique not null
);
