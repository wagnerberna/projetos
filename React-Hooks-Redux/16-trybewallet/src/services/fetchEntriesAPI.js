const fetchEntriesAPI = async () => {
  const endpoint = 'https://economia.awesomeapi.com.br/json/all';
  const dataInfo = await fetch(endpoint);
  const dataJson = await dataInfo.json();
  delete dataJson.USDT;
  const dataEntries = Object.entries(dataJson);
  // console.log(dataEntries);
  return dataEntries;
};

export default fetchEntriesAPI;
