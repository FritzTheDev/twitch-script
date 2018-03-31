const express = require('Express');
const app = express();
const bodyParser = require('body-parser');

app.get('/', (req, res)=> {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('TwitchScript Converter is running on port 3000!')
});
