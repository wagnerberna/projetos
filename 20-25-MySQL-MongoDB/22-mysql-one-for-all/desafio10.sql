DELIMITER $$
CREATE FUNCTION quantidade_musicas_no_historico(id INT)
RETURNS INT READS SQL DATA
BEGIN
DECLARE totalMusicas INT;
SELECT
COUNT(*)
FROM SpotifyClone.historicos AS h
WHERE h.usuario_id = id INTO totalMusicas;
RETURN totalMusicas;
END
$$
DELIMITER ;
