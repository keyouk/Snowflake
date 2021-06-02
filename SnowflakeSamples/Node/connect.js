require('dotenv').config();
const express = require('express');
const app = express();
const snowflake = require('snowflake-sdk');
const PORT = 3002;

snowflake.configure({ logLevel: 'trace' });

// Create a Connection object that we can use later to connect.
var connection = snowflake.createConnection({
  account: account,
  username: username,
  password: password,
});

connection.connect(function (err, conn) {
  if (err) {
    console.error('Unable to connect: ' + err.message);
  } else {
    console.log('Successfully connected to Snowflake.');
    // Optional: store the connection ID.
    connection_ID = conn.getId();
  }
});

connection.execute({
  sqlText: 'show databases',
  complete: function (err, stmt, rows) {
    if (err) {
      console.error(
        'Failed to execute statement due to the following error: ' + err.message
      );
    } else {
      console.log('Successfully executed statement: ' + stmt.getSqlText());
    }
  },
});