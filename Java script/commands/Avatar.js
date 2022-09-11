module.exports = async (bot,message,args,argsF) => {
    const {author, member, mentions} = message;
    const user = mentions.members.first()||member;
    const avatarURL = user.displayAvatarURL({size: 512});

    message.channel.send ({
        embeds: [{
            title: "Аватарка "+user.displayName,
            color: user.displayColor,
            description: `Различные форматы аватарки: [jpg](${user.displayAvatarURL({extension:"jpg",size: 512})}), [jpeg](${user.displayAvatarURL({extension:"jpeg",size: 512})}), [png](${user.displayAvatarURL({extension:"png",size: 512})}), [gif](${user.displayAvatarURL({extension:"gif",size: 512})})`,
            image: {
                url: avatarURL
            }
        }]
    })
};
module.exports.names = ["аватарка", "Аватарка"];
