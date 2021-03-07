const axios = require("axios");
const { response } = require("express");
const config = require("../config");

function getUserInfo(token) {
    axios({
        method: "get",
        url: `${config.config.apiUrl}/users/rafirabbani`,
        headers: {
          //Authorization: "Bearer" + token,
          accept: "application/json"
        }
      }).then((response) =>  {
        return response.data;
      });
      return response.get;
  }
let a = getUserInfo('a token');
console.log(a);
module.exports = {
  getUserInfo: getUserInfo
}