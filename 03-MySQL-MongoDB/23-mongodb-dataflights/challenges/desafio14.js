db.voos.count({
  $nor: [
    { "aeroportoOrigem.pais": "BRASIL" },
  ],
});