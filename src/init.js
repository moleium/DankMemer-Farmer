const clc = require("cli-color")
const fs = require('fs');

// Laod Config
const LoadConfig = fs.readFileSync('./config.json');

// Load Elements
const config = JSON.parse(LoadConfig)
var token = config["token"]
var dank_id = config["dankCommands"]["dank_id"]
var configs = {
    token,
    dank_id
}

// Colors
var GREEN = clc.green;
var RED = clc.red.bold;
var YELLOW = clc.yellowBright;
var BLUE = clc.blue;

var colors = {
    GREEN,
    RED,
    YELLOW,
    BLUE
};

console.log(colors.YELLOW("[+] Initlization file loaded"))
console.log(colors.YELLOW(`\t[-] USER TOKEN   ${token}\n\t[-] DANKMEMER ID ${dank_id}`))

// Export
module.exports = {
    configs,
    colors
}