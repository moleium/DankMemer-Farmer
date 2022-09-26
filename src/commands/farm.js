// im coding this shit because WT servers are down :sob:😭
const { configs, colors } = require('../init')
const delay = ms => new Promise(resolve => setTimeout(resolve, ms))

module.exports = {
    name: 'farm',
    execute(msg) {
        msg.channel.sendSlash(configs.dank_id, "beg");
        console.log(colors.GREEN("[+] Used Beg"))

        msg.channel.sendSlash(configs.dank_id, "dig");
        console.log(colors.GREEN("[+] Used Dig"))

        console.log(colors.YELLOW("[+] Sleeping for 5s"))

        msg.channel.sendSlash(configs.dank_id, "hunt");
        console.log(colors.GREEN("[+] Used Hunt"))

        console.log(colors.YELLOW("[+] Sleeping for 46s\n"))
        //msg.channel.sendSlash(configs.dank_id, "deposit");
        //console.log(colors.GREEN("[+] DEPOSIT"))

    }
}