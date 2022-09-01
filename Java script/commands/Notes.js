module.exports = async (bot,message,args,argsF) => {
    const {content, author} = message;
    const memUser = bot.Memory.users.get(author.id);

    if(args[0]=="Просмотр") {
        let description = "";
        for (let i = 0; i < memUser.notes.length; i++) {
            const note = memUser.notes[i];
            description+=(i+1)+") "+note+"\n";
        }
        return message.reply ({
            embeds: [{
                title: "Записная книжка",
                description
            }]
        });
    }

    if(args[0]=="Удалить"){
        if(!args[1]||args[1]>memUser.notes.lenght) return message.reply("Укажите правильный номер записи.");
        memUser.notes.splice(args[1]-1,1);
        return message.reply ({
            embeds: [{
                title: "Записная книжка",
                description: "Запись удалена",
                color: "#BBC3A5"
            }]
        });
    }

    if(!argsF.join(" ")) return message.reply("Укажите новую запись");
    memUser.notes.push(argsF.join(" "));
    return message.reply ({
        embeds: [{
            title: "Записная книжка",
            description: "Запись добавлена"
        }]
    });

};
module.exports.names = ["заметка", "Заметка"]; //У неё есть название