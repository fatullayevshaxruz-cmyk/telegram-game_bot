const TelegramBot = require('node-telegram-bot-api');
require("dotenv").config();

const {gameOptions, againOptions} = require('./options.js')

const bot = new TelegramBot(process.env.BOT_TOKEN, {polling: true});


const obj = {};


const startGame = async chatId => {
     await bot.sendMessage(chatId,
            "Kompyuter 0 dan 9 gacha son o'ylaydi siz o'sha sonni topishga harakat qiling"
        );
        const randomNumber = Math.floor(Math.random() * 10);
        obj[chatId] = randomNumber;
        await bot.sendMessage(chatId, "To'g'ri sonni toping",
            gameOptions
        )
}

const bootstrap = () => {

    bot.setMyCommands([
    {
        command: "/start",
        description: "Bot haqida malumot",
    },
    {
      command: "/info",
      description: "O'zingiz haqingizda malumot"  
    },

    {
      command: "/game",
      description: "O'yin o'ynash"  
    },
]);

    bot.on('message', async msg => {
    const text = msg.text;
    const chatId = msg.chat.id;

  // send a message to the chat acknowledging receipt of their message
  if (text === "/start") {
    return bot.sendMessage(
         chatId,
        `Assalomu Aleykum ${msg.from?.first_name} sizni oquv kursimizda korib turganimizdan xursandmiz`
    );
}

    if (text === "/info") {
         await bot.sendSticker(
            chatId,
             "https://tlgrm.eu/_/stickers/4dd/300/4dd300fd-0a89-3f3d-ac53-8ec93976495e/1.webp"

         );
         
         return bot.sendMessage(
            chatId,
            `Assalomu aleykum username bu ${msg.from?.username}, sizning u=ismingiz esa ${msg.from?.first_name} ${msg.from.last_name}`
        );
    }

    if (text === "/game") {
       return startGame(chatId )
    }

    bot.sendMessage(chatId, 
        'Uzur men sizning gapingizga tushunmayapman!! ):'
    );
});

    bot.on("callback_query", async msg=>{
        const data = msg.data;
        const chatId = msg.message.chat.id;

        if (data === "/again") {
            return startGame(chatId)
        }

        if (data == obj[chatId]) {
            await bot.sendSticker(
                chatId,
                "https://tlgrm.eu/_/stickers/4d6/8ea/4d68eab6-b229-358b-8d46-e5da083d2f40/1.webp"
            );

            return bot.sendMessage(chatId,
                `Tabriklaymiz siz to'g'ri topdingiz Kompyuter ${obj[chatId]} sonini tanlagan edi`
             )
        }
        else{
            await bot.sendSticker(
                chatId,
                "https://tlgrm.eu/_/stickers/4dd/300/4dd300fd-0a89-3f3d-ac53-8ec93976495e/10.webp"
            )
            return bot.sendMessage(chatId,
                `Siz noto'g'ri son tanladingiz tanlagan soningiz ${data}, kompyuter esa ${obj[chatId]} shu sonni tanlagan edi`,
                againOptions
            );
        }


    })
};
console.log("Bot tayyor");
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Bot ishlayapti');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log('Server portda ishlayapti:', PORT);
});
bootstrap();