import configuration from '/data/configuration.json'
import prices from '/data/price_history.json'
import orders from '/data/orders.json'
import logs from '/data/log.json'


export const getConfigurationData = () => {
  return configuration;
};

export const getPricesData = () => {
  return prices;
};

export const getOrdersData = () => {
  return orders;
};

export const getLogsData = () => {
  return logs;
};