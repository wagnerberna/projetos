const fetchCodeAPI = async () => {
  const endpoint = 'https://economia.awesomeapi.com.br/json/all';
  const dataInfo = await fetch(endpoint);
  const dataJson = await dataInfo.json();
  delete dataJson.USDT;
  const dataKeys = Object.keys(dataJson);
  // console.log(dataKeys);
  return dataKeys;
};

export default fetchCodeAPI;
