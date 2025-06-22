CREATE TABLE galaxy_classification(
    galaxy_classification_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE, 
    description TEXT NOT NULL
); 


CREATE TABLE galaxy(
    galaxy_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    distance_from_earth_in_mpc DECIMAL(10, 2) NOT NULL,
    constellation VARCHAR(50) NOT NULL,
    galaxy_classification INT NOT NULL,
    FOREIGN KEY (galaxy_classification_id) REFERENCES galaxy_classification(galaxy_classification_id)
);

CREATE TABLE star(
    star_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    planets INT NOT NULL,
    constellation VARCHAR(50) NOT NULL,
    galaxy_id INT NOT NULL,
    FOREIGN KEY (galaxy) REFERENCES galaxy(galaxy_id)
); 

CREATE TABLE planet(
    planet_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    moons INT NOT NULL,
    has_life BOOLEAN NOT NULL,
    star_id INT NOT NULL,
    FOREIGN KEY (star_id) REFERENCES star(star_id)
); 

CREATE TABLE moon(zmoon_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    is_spherical BOOLEAN NOT NULL, 
    diameter_in_km DECIMAL(10, 2) NOT NULL,
    planet_id INT NOT NULL,
    FOREIGN KEY (planet_id) REFERENCES planet(planet_id)
); 

