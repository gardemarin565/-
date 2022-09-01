const {IntentsBitField, Partials, Client} = require('discord.js'),
    config = require('./config.json');
config.cfg = {
    ...config.cfg,
    intents: new IntentsBitField(config.cfg.intents),
    partials: [Partials.Channel]
};

    
const bot = new Client(config.cfg);
bot.login(config.token);

const DiscordDB = require('simple-discord.db');
bot.Memory = new DiscordDB("Memory", bot);
bot.Memory.save();

require('./handlers')(bot);
require('./events')(bot);
