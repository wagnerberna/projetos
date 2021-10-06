db.trips.aggregate([
  {
    $group: {
      _id: { $dayOfWeek: "$startTime" },
      somaDias: { $sum: 1 },
    },
  },
  {
    $project: {
      _id: 0,
      diaDaSemana: "$_id",
      total: "$somaDias",
    },
  },
  { $sort: { total: -1 } },
  { $limit: 1 },
]);
