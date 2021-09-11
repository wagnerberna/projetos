CREATE VIEW historico_reproducao_usuarios AS
SELECT
u.usuario,
c.cancao AS nome
FROM SpotifyClone.historicos AS h
INNER JOIN SpotifyClone.usuarios AS u
ON h.usuario_id = u.id
INNER JOIN SpotifyClone.cancoes AS c
ON h.cancao_id = c.id
ORDER BY 1,2;
