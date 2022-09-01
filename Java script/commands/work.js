module.exports = async (bot,message,args,argsF) => {
    const {author, content} = message;
    const money = bot.Memory.users.get(author.id);
    let amount = Math.random() * (1000 - 50 + 1) + 50

    if(!args[0]) {
        money = money + amount

        message.channel.send ({
            content: `Вы поработали, и получили ${amount}`
        })
    }
};
module.exports.names = ["работать", "Работать"]; //У неё есть название