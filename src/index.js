const { Client } = require("discord.js-selfbot-v13");
const { tokens, prefixes } = require("./init");
const { farm } = require("./commands/farm");
const winston = require("winston"); // Debugging Library

const logger = winston.createLogger({
  transports: [
    new winston.transports.Console()
  ]
});

for (let i = 0; i < tokens.length; i++) {
    const client = new Client({
        checkUpdate: false
    });

    let farmInterval;

    client.once("ready", () => {
        logger.info(`Successfully logged into ${client.user.username}!`);
    });

    client.on("messageCreate", async msg => {
        if (msg.author.id !== client.user.id) return;

        const prefix = prefixes[i];
        const messages = ["beg", "dig", "hunt"];
        const interval = 46000;

        switch (msg.content) {
            case `${prefix}is_logined`:
                await msg.channel.send("Yes");
                break;

            case `${prefix}farm`:
                farmInterval = setInterval(() => farm(msg, messages, interval), interval);
                break;

            case `${prefix}stop`:
                clearInterval(farmInterval);
                logger.info("Stopped farming. In-progress commands may not be stopped yet.");
                break;
        }
    });

    client.login(tokens[i]).catch(err => {
        logger.error(`Error logging in: ${error.message}`, {
            location: 'index.js',
            function: 'client.login',
            error
        });
    });
}

module.exports = logger;
