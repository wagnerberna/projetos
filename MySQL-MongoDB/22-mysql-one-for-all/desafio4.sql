CREATE VIEW top_3_artistas AS
SELECT
a.artista,
COUNT(s.usuario_id) AS seguidores
FROM SpotifyClone.seguidores AS s
INNER JOIN artistas AS a
ON s.artista_id = a.id
GROUP BY 1
ORDER BY 2 DESC, 1
LIMIT 3;
