DELIMITER $$
CREATE PROCEDURE albuns_do_artista(in nome VARCHAR(50))
BEGIN
SELECT 
ar.artista,
al.album
FROM SpotifyClone.artistas AS ar
INNER JOIN SpotifyClone.albuns AS al
ON ar.id = al.artista_id
WHERE ar.artista = nome
ORDER BY 2;
END
$$
DELIMITER ;
