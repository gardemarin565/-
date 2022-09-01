module.exports = async (bot,message,args,argsF) => {
    const {author, content} = message;
    const amount = bot.Memory.users.get(author.id);

    if(!args[0]) {
        message.reply ({
            content: `Ваш баланс составляет ${amount}`
        })
    }
};
module.exports.names = ["Баланс", "баланс"]; //У неё есть название