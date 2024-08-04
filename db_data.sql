CREATE DATABASE plantcompanion;

CREATE TABLE core_plants(
	id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL,
	name TEXT NOT NULL UNIQUE,
	zone TEXT NOT NULL,
	plant_family TEXT NOT NULL
);

CREATE TABLE companion_plants(
	id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL,
	name TEXT NOT NULL UNIQUE,
	zone TEXT NOT NULL,
	insect_modifier int NOT NULL,
	soil_modifier int NOT NULL,
	flower_modifier int NOT NULL,
	shade_modifier int NOT NULL
);

CREATE TABLE core_companion_plant_mappings (
    id SERIAL PRIMARY KEY,
	created_at TIMESTAMP NOT NULL,
    core_plant_id INTEGER NOT NULL,
    companion_plant_id INTEGER NOT NULL,
    FOREIGN KEY (core_plant_id) REFERENCES core_plants (id),
	FOREIGN KEY (companion_plant_id) REFERENCES companion_plants (id)
);