# DankMemer-Farmer

A Discord self-bot that allows you to automate DankMemer tasks. It supports multiple accounts and can be easily configured using `config.json` and `.env` files.

## Prerequisites

- Node.js v12 or higher
- discord.js-selfbot-v13
- Winston

## Installation

1. Clone the repository:<br>
```sh
git clone https://github.com/MoleTheDev/DankMemer-Farmer.git
```
2. Install dependencies using:<br>
```sh
npm install discord.js-selfbot-v13 winston
```
3. Configure using `config.json` file or using `.env`
4. Start the bot:<br>
```sh
npm start
```

## Configuration
To configure the bot, you can either use the ```config.json``` file or define variables in a .env file.

Examples of how would they look like:
- `config.json`:
```js
{
  "tokens": ["token1"],
  "prefixes": ["!"]
}
```
- `.env`:
```
TOKENS=token1
PREFIXES=.
```

## License

MIT. See [LICENSE](LICENSE) for details.

## Contributions

We welcome contributions to this project. If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.
