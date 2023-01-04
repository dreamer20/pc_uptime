DROP TABLE IF EXISTS uptime;

CREATE TABLE uptime (
    id INTEGER NOT NULL DEFAULT 1,
    total_uptime INTEGER NOT NULL,
    last_update VARCHAR NOT NULL DEFAULT NOW()
);

INSERT INTO uptime (total_uptime) VALUES (0);