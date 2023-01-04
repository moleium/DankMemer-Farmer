const fs = require("fs");
const dotenv = require("dotenv");

dotenv.config();

const loadConfig = fs.readFileSync("./config.json");
const config = JSON.parse(loadConfig);

const tokens = config.tokens || process.env.TOKENS.split(",");
const prefixes = config.prefixes || process.env.PREFIXES.split(",");
const dankId = '270904126974590976';

module.exports = {
    tokens,
    prefixes,
    dankId
};
