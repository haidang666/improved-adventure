const express = require('express');
const sequelize = require('./config/database');
const userRoutes = require('./src/modules/user/user.routes');

const app = express();
const port = process.env.PORT || 3000;

(async () => {
  try {
    await sequelize.authenticate();
    await sequelize.sync();
    console.log('Connected to the database and synchronized models.');
  } catch (error) {
    console.error('Database connection error:', error);
  }
})();

app.use(express.json());

app.use('/api/users', userRoutes);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
