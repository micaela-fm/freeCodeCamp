INSERT INTO galaxy_classification (name, description) 
VALUES ('Spiral', 'A galaxy with a central bulge and spiral arms'), 
       ('Elliptical', 'A galaxy with an ellipsoidal shape'), 
       ('Lenticular', 'A galaxy that is a cross between a spiral and an elliptical galaxy'),
       ('Irregular', 'A galaxy that does not fit into the other two categories');

INSERT INTO galaxy (name, description, distance_from_earth_in_mpc, constellation, galaxy_classification)
VALUES ('Milky Way', 'The galaxy that contains our solar system', 0.0, 'Sagittarius', 1),
       ('Andromeda', 'The nearest spiral galaxy to the Milky Way', 2.537, 'Andromeda', 1),
       ('Messier 87', 'A supergiant elliptical galaxy in the Virgo constellation', 53.5, 'Virgo', 2),
       ('Large Magellanic Cloud', 'A satellite galaxy of the Milky Way', 0.163, 'Dorado', 3), 
       ('Small Magellanic Cloud', 'A satellite galaxy of the Milky Way', 0.2, 'Tucana', 3), 
       ('Triangulum', 'A spiral galaxy in the constellation Triangulum', 3.07, 'Triangulum', 1);

INSERT INTO star (name, planets, constellation, galaxy_id) 
VALUES ('Sun', 8, 'None', 1),
       ('Proxima Centauri', 1, 'Centaurus', 2),
       ('Alpha Centauri A', 1, 'Centaurus', 2),
       ('Alpha Centauri B', 1, 'Centaurus', 2),
       ('Barnard''s Star', 1, 'Ophiuchus', 2),
       ('Wolf 359', 1, 'Leo', 2);

INSERT INTO planet (name, moons, has_life, star_id)
VALUES ('Mercury', 0, FALSE, 1),
       ('Venus', 0, FALSE, 1),
       ('Earth', 1, TRUE, 1),
       ('Mars', 2, FALSE, 1),
       ('Jupiter', 79, FALSE, 1),
       ('Saturn', 82, FALSE, 1),
       ('Uranus', 27, FALSE, 1),
       ('Neptune', 14, FALSE, 1),
       ('Proxima Centauri b', 0, FALSE, 2),
       ('Alpha Centauri A b', 0, FALSE, 3),
       ('Alpha Centauri B b', 0, FALSE, 4),
       ('Barnard''s Star b', 0, FALSE, 5),
       ('Wolf 359 b', 0, FALSE, 6);

INSERT INTO moon (name, is_spherical, diameter_in_km, planet_id)
VALUES ('Moon', TRUE, 3474.8, 3),
       ('Phobos', TRUE, 22.4, 4),
       ('Deimos', TRUE, 12.4, 4),
       ('Io', TRUE, 3642, 5),
       ('Europa', TRUE, 3121.6, 5),
       ('Ganymede', TRUE, 5262.4, 5),
       ('Callisto', TRUE, 4800, 5),
       ('Mimas', TRUE, 396.4, 6),
       ('Enceladus', TRUE, 504.2, 6),
       ('Tethys', TRUE, 1062, 6),
       ('Dione', TRUE, 1122.8, 6),
       ('Rhea', TRUE, 1527.6, 6),
       ('Titan', TRUE, 5150, 6),
       ('Iapetus', TRUE, 1468.6, 6),
       ('Umbriel', TRUE, 1169.4, 7),
       ('Titania', TRUE, 1577.8, 7),
       ('Oberon', TRUE, 1522.8, 7),
       ('Triton', TRUE, 2706.8, 8),
       ('Nereid', TRUE, 340, 8),
       ('Proxima Centauri b', FALSE, 0, 9),
       ('Alpha Centauri A b', FALSE, 0, 10),
       ('Alpha Centauri B b', FALSE, 0, 11),
       ('Barnard''s Star b', FALSE, 0, 12),
       ('Wolf 359 b', FALSE, 0, 13);