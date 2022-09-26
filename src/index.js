const { Client } = require('discord.js-selfbot-v13');
const fs = require('fs');
const { configs, colors } = require("./init"); // Initlization File
const farm = require("./commands/farm");
const { execute } = require('./commands/farm');

const client = new Client({
  checkUpdate: false
});

// When we are ready
client.on('ready', async () => {
  console.log(colors.YELLOW(`[+] Logged into ${client.user.username}!`));
})

client.on("messageCreate", async msg => {
  if (msg.author.id !== client.user.id) return; // If the message is not from us, ignore it

  // if message is ping, send pong
  if (msg.content === "ping") {
    msg.channel.send("pong");
  }

  if (msg.content == "farm") {
    execute(msg); setTimeout(function() { execute(msg);}, 46000);
  }
});

client.login(configs.token);