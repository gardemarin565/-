module.exports = async (bot,message,args,argsF) => {
     
    if (!args[0]) return message.reply("Укажите время напоминания");
    const result = args[0].match(/^(\d|\d\d)(h|s|m)$/i);
    if (!args[0]) return message.reply("Укажите время напоминания");
    const time = result[1]*(result[2]=="s"?1000:result[2]=="m"?1000*60:result[2]=="h"?1000*60*60:1000);
    if(!args[1]) return message.reply("Укажите напоминание");
    setTimeout(() => {
        message.author.send({
            content: "Вам нужно было напомнить "+argsF.slice(1).join(" ")
        }).catch(err=>console.error(err))
    }, time);
    return message.reply("Ожидайте!");

};
module.exports.names = ["Напоминание", "напоминание"]; //У неё есть название