
CREATE TABLE IF NOT EXISTS POST(
    post_id int(5) NOT NULL,
    post_url varchar(40) NOT NULL,
    post_date date,
    PRIMARY KEY(post_id)
);

CREATE TABLE IF NOT EXISTS CONDITION(
    cond_id integer PRIMARY KEY,
    cond_name text NOT NULL,
    cond_image text,
    xws text,
    cond_desc text,
    cond_unique text
);
