db.produtos.updateMany(
  {},
  { $set: { valorUnitario: NumberDecimal("0.00") } },
  { upsert: true },
);

db.produtos.find({}, { _id: false, nome: true, valorUnitario: true });