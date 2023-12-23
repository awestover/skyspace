const iv = CryptoJS.enc.Hex.parse('6ed541b6ca008267aec855b643fe4dfc');

function getPassword(){
  return document.getElementById("password").value;
}

function clickEnc(){
  let plaintext = document.getElementById("inputtext").value;
  console.log(plaintext);
  console.log(ENC(plaintext));
  appendText(ENC(plaintext));
}
function clickDec(){
  let ciphertext = document.getElementById("inputtext").value;
  console.log(ciphertext);
  console.log(DEC(ciphertext));
  appendText(DEC(ciphertext));
}

function ENC(plaintext){
  const key = CryptoJS.PBKDF2(getPassword(), '', { keySize: 192 / 32, iterations: 10000 });
  const encrypted = CryptoJS.AES.encrypt(plaintext, key, { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
  const encryptedHex = encrypted.ciphertext.toString(CryptoJS.enc.Hex);
  return encryptedHex;
}

function DEC(ciphertext){
  const key = CryptoJS.PBKDF2(getPassword(), '', { keySize: 192 / 32, iterations: 10000 });
  const encryptedCiphertext = CryptoJS.enc.Hex.parse(ciphertext);
  const decrypted = CryptoJS.AES.decrypt(
    { ciphertext: encryptedCiphertext },
    key,
    { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 }
  ).toString(CryptoJS.enc.Utf8);
  return decrypted;
}

function appendText(text) {
      const displayDiv = document.getElementById("display");
      const newTextElement = document.createElement("p");
      newTextElement.textContent = text;

      const copyButton = document.createElement("button");
      copyButton.textContent = "Copy";
      copyButton.setAttribute("class", "copyBtn");
      copyButton.setAttribute("data-clipboard-text", text);

      const containerDiv = document.createElement("div");
      containerDiv.setAttribute("class", "containerDiv"); // Adding class for word-wrap
      containerDiv.appendChild(newTextElement);
      containerDiv.appendChild(copyButton);

      // Insert new elements at the beginning
      if (displayDiv.firstChild) {
        displayDiv.insertBefore(containerDiv, displayDiv.firstChild);
      } else {
        displayDiv.appendChild(containerDiv);
      }

      const divider = document.createElement("hr"); // Create divider element
      divider.setAttribute("class", "divider"); // Add class for styling
      displayDiv.insertBefore(divider, displayDiv.firstChild);
    }


// Initialize ClipboardJS
document.addEventListener('DOMContentLoaded', function() {
  new ClipboardJS('.copyBtn');
});


