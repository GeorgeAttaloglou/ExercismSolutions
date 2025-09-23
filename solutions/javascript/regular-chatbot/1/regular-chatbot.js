// @ts-check

/**
 * Given a certain command, help the chatbot recognize whether the command is valid or not.
 *
 * @param {string} command
 * @returns {boolean} whether or not is the command valid
 */

export function isValidCommand(command) {
  const yes = /chatbot/i;
  let split_command = command.split(/[,.\s]/);
  if (split_command[0].match(yes)){
    return true
  } else {
    return false
  }
}

/**
 * Given a certain message, help the chatbot get rid of all the emoji's encryption through the message.
 *
 * @param {string} message
 * @returns {string} The message without the emojis encryption
 */
export function removeEmoji(message) {
  const emoji = /emoji[0-9]*/gi
  let new_message = message.replace(emoji, "")
  return new_message
}

/**
 * Given a certain phone number, help the chatbot recognize whether it is in the correct format.
 *
 * @param {string} number
 * @returns {string} the Chatbot response to the phone Validation
 */
export function checkPhoneNumber(number) {
  if (/^\(\+[0-9][0-9]\) [0-9]{3}-[0-9]{3}-[0-9]{3}$/.test(number)){
    return "Thanks! You can now download me to your phone."
  } else {
    return "Oops, it seems like I can't reach out to " + number
  }
}

/**
 * Given a certain response from the user, help the chatbot get only the URL.
 *
 * @param {string} userInput
 * @returns {string[] | null} all the possible URL's that the user may have answered
 */
export function getURL(userInput) {
    return [
    'youtube.com',
    'theodinproject.com',
    'reddit.com',
    'notion.so'
  ].filter((domain) => userInput.includes(domain))
}

/**
 * Greet the user using the full name data from the profile.
 *
 * @param {string} fullName
 * @returns {string} Greeting from the chatbot
 */
export function niceToMeetYou(fullName) {
  return "Nice to meet you," + fullName.split(",")[1] + " " + fullName.split(",")[0]
}
