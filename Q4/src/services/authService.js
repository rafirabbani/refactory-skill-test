const config = require("../config/index");

function redirectUri() {
  return `${config.config.oauthUrl}/authorize?client_id=${config.config.clientId}`;
}
module.exports = {
  redirectUri: redirectUri
};