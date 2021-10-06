db.voos.count({
  $or: [
    { "aeroportoDestino.pais": "BRASIL" },
    { "aeroportoDestino.pais": "CHILE" },
    { "aeroportoDestino.pais": "ARGENTINA" },
  ],
});