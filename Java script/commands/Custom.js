const later = (delay, value) => 
    new Promise(resolve => setTimeout(resolve, delay, value));
module.exports = async (bot,message,args,argsF) => {
    const {channel, author, member, guild} = message;
    const options = {};
    message.reply("Напиши пожалуйста название своей роли")
    const filter = m => m.author == author;
    options.name = (await channel.awaitMessages({filter, max: 1})).first().content;
    channel.send("Напиши пожалуйста цвет своей роли в хекс-коде (#23daea), воспользуйся этим сайтом: https://htmlcolorcodes.com/");
    options.color = (awaitMessages({filter, max: 1})).first().content;
    channel.send("Создаю роль...");
    const role = await guild.roles.create(options);
    await member.roles.add(role);
    return channel.send("Роль выдана")    
};
module.exports.names = ["Кастом"];
