db.voos.findOne({
  $or: [
    { "empresa.nome": "DELTA" },
    { "empresa.nome": "AMERICAN AIRLINES" },
  ],
  $and: [
    { "aeroportoOrigem.sigla": "SBGR" },
    { "aeroportoDestino.sigla": "KJFK" },
  ],
}, { _id: 0, vooId: 1 });