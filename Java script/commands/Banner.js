module.exports = async (bot,message,args,argsF) => {
    const {author, member, mentions} = message;
    const user = mentions.members.first()||member;
    const bannerURL = user.bannerURL({size: 512});

    message.channel.send ({
        embeds: [{
            title: "Баннер "+user.displayName,
            color: user.displayColor,
            image: {
                url: bannerURL
            }
        }]
    })
};
module.exports.names = ["баннер", "Баннер"]; //У неё есть название