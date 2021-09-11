CREATE VIEW top_2_hits_do_momento AS
SELECT
c.cancao,
COUNT(h.cancao_id) AS "reproducoes"
FROM SpotifyClone.cancoes AS c
INNER JOIN SpotifyClone.historicos AS h
ON c.id = h.cancao_id
GROUP BY 1
ORDER BY 2 DESC, 1
LIMIT 2;
