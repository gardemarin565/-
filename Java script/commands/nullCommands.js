module.exports = async (bot,message,args,argsF) => {
    return message.reply({
        content: "Понг!"
    });
    
};
module.exports.names = ["пинг"];
module.exports.interaction = {
    name: 'пинг',
    description: 'Просто проверочная команда, ничего больше',
    defaultPermission: true
};
