#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const userTasksCount = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (userTasksCount[task.userId]) {
          userTasksCount[task.userId]++;
        } else {
          userTasksCount[task.userId] = 1;
        }
      }
    });

    console.log(userTasksCount);
  } else {
    console.log('Error: Unable to fetch data');
  }
});
