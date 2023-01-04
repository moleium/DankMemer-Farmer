const winston = require('winston');
const dankId = '270904126974590976';

const logger = winston.createLogger({
  transports: [
    new winston.transports.Console()
  ]
});

let timesSent = 0;

const sendMessage = async (msg, command) => {
  try {
    timesSent++;
    await msg.channel.sendSlash(dankId, command);
    logger.info(`Used ${command}: <${timesSent}>`);
  } catch (error) {
    if (error.message === 'INTERACTION_TIMEOUT') {
      logger.warn('The Discord API did not respond within the expected time frame.');
    } else {
      logger.error(`An error occurred while sending message: ${error.message}`);
    }
  }
};

module.exports = {
    async farm(msg, messages, interval) {
        for (const command of messages) {
            await sendMessage(msg, command);
        }

        logger.info(`Sleeping for ${interval}ms`);
        await new Promise(resolve => setTimeout(resolve, interval));
    },

    timesSent
};
