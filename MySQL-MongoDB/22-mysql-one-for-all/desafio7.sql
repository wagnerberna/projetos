CREATE VIEW perfil_artistas AS
SELECT
ar.artista,
al.album,
COUNT(se.usuario_id) AS "seguidores"
FROM SpotifyClone.artistas AS ar
INNER JOIN SpotifyClone.albuns AS al
ON ar.id = al.artista_id
INNER JOIN SpotifyClone.seguidores AS se
ON ar.id = se.artista_id
GROUP BY al.id
ORDER BY 3 DESC, 1, 2;
