const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('<h1>Of all sad words of toungue and pen the saddest are these: Twitch Chat was right again!</h1>'));

app.listen(3000, () => console.log('Your server is running'));
