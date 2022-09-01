module.exports = async (bot,message,args,argsF) => {
    return message.reply({
        content: "Понг!"
    });
    
};
module.exports.names = ["пинг"];
module.exports.interaction = {
    name: 'пинг',
    description: 'Ответить на команду текстом "Понг!"',
    defaultPermission: true
};
