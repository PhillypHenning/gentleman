
CREATE TABLE IF NOT EXISTS POSTS(
    post_id int(20) PRIMARY KEY,
    post_url varchar(200) NOT NULL,
    post_date date,
);

CREATE TABLE IF NOT EXISTS CONDITIONS(
    cond_id integer PRIMARY KEY,
    cond_name text NOT NULL,
    cond_image text,
    cond_desc varchar(200),
    cond_unique text
);

CREATE TABLE IF NOT EXISTS PILOTS(
    pilot_id int(4) PRIMARY KEY,
    pilot_name text,
    is_unique boolean,
    ship_type text,
    pilot_skill int(2),
    points int(3),
    slots varchar(250)
    pilot_text varchar(250),
    pilot_image varchar(100),
    pilot_faction text
);

CREATE TABLE IF NOT EXISTS REFERENCE-CARDS(
    rc_id int(4) PRIMARY KEY,
    rc_title text,
    rc_num int(2),
    rc_image text
);

CREATE TABLE IF NOT EXISTS UPGRADES(
    upgrade_id int(4), PRIMARY KEY, 
    upgrade_name text, 
    upgrade_slot text,
    upgraade_unique boolean,
    points int(3),
    attack int(2),
    atk_range text,
    upgrade_text varchar(200),
    upgrade_image varchar(200)
);