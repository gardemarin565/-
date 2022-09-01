module.exports = async (bot,message,args,argsF) => {
    const {author, member, mentions} = message;
    const user = mentions.members.first()||member;
    const avatarURL = user.displayAvatarURL({size: 512});

    message.channel.send ({
        embeds: [{
            title: "Аватарка "+user.displayName,
            color: user.displayColor,
            description: `Различные форматы аватарки: [jpg](${user.displayAvatarURL({option:"jpg",size: 512})}), [jpeg](${user.displayAvatarURL({option:"jpeg",size: 512})}), [png](${user.displayAvatarURL({option:"png",size: 512})}), [gif](${user.displayAvatarURL({option:"gif",size: 512})})`,
            image: {
                url: avatarURL
            }
        }]
    })
};
module.exports.names = ["аватарка", "Аватарка"]; //У неё есть название