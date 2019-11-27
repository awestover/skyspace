var lastKeys = [];
var lastPublicKeys = [];

function keys()
{
  var p = biggerPrime(parseInt(Math.random()*100) + 11);
  var q = biggerPrime(p + parseInt(Math.random()*100) + 1);

  var n = p*q;
  var phi = (p-1) * (q-1);

  var e = biggerPrime(parseInt(Math.random()*10)+1);
  var d = betterModularInverse(e, phi);
  while (d == 1)
  {
    e = biggerPrime(parseInt(Math.random()*10)+1);
    d = betterModularInverse(e, phi);
  }

  lastKeys = [p, q, n, phi, e, d];
  lastPublicKeys = [n, e];
  return lastKeys;
}

function NseededGenKeys()
{
  var p = parseInt(document.getElementById("pnew").value);
  var q = parseInt(document.getElementById("qnew").value);
  var e = parseInt(document.getElementById("enew").value);
  return seededGenKeys(p,q,e);
}

function seededGenKeys(p, q, e)
{
  var n = p*q;
  var phi = (p-1) * (q-1);
  var d = betterModularInverse(e, phi);

  if (d==1)
  {
    alert("ERROR");
  }

  if (! isPrime(p) || ! isPrime(q)) 
  {
    alert("ERROR");
  }

  lastKeys = [p, q, n, phi, e, d];
  lastPublicKeys = [n, e];
  return lastKeys;

}


function modMult(a, b, mod)
{
  var answer = 0;
  for (var i = 0; i < b; i++)
  {
    answer = (answer + a) % mod;
  }
  return answer;
}


// actually there is a way faster way to do this
function modPower(a, b, mod)
{
  var answer = 1;
  for (var i = 0; i < b; i++)
  {
    answer = modMult(answer, a, mod) % mod;
  }
  return answer;
}

// O(logN)  :)
// take out recursion.. js is really bad with recurion
// to take out recursion probably need to calculate binary version of power...
function fastModPower(a, b, mod)
{
  if (b == 1)
  {
    return (a % mod);
  }
  else
  {
    var x = fastModPower(a, Math.floor(b/2), mod) % mod;
    if (b%2 == 0)
    {
      return ((x*x) % mod);
    }
    else
    {
      return (x*x*a) % mod; 
    }

  }
}


// could be more efficent with
// extended euclidean algorithm
function modularInverse(e, mod)
{
  var d = 1;
  while (modMult(e, d, mod) != 1)
  {
    d += 1;
  }
  return d;
}

function betterModularInverse(e, mod)
{
  if(!e || ! mod){alert("ERROR");}
  var t = 0; var nt = 1;
  var r = mod; var nr = e;
  while (nr != 0) {
    var q = parseInt(r/nr);

    var ts = [nt, t - q*nt];
    var rs = [nr, r - q*nr];

    t = ts[0]; nt = ts[1];
    r = rs[0]; nr = rs[1];
  }

  if (t < 0)
  {
    t += mod;
  }
  return t;

}

function formatKeys(keys)
{
  var p = keys[0];
  var q = keys[1];
  var n = keys[2];
  var phi = keys[3];
  var e = keys[4];
  var d = keys[5];
  return "p = " + p + " (secret)" + "<br>" + "q = " + q + " (secret)" + "<br>"
    + "n = p*q = " + n + " (not secret)" + "<br>" +
    "phi = (p-1)*(q-1) = " + phi + " (very secret)" + "<br>" + "e = " + e + " (not secret)" +
    "<br>" + "d = " + d + " so that e*d % phi = 1" + " (very secret)";
}


function encodeMessage()
{
  if (lastPublicKeys.length == 0)
  {
    alert("please set keys first");
    return (-1);
  }
  else {
    var e = lastPublicKeys[1];
    var n = lastPublicKeys[0];
    var message = parseInt(document.getElementById("m").value);
    return modPower(message, e, n);
  }
}

function decodeMessage()
{
  if (lastKeys.length == 0)
  {
    alert("please set keys first");
    return (-1);
  }
  else {
    var d = lastKeys[5];
    var n = lastPublicKeys[0];
    var message = parseInt(document.getElementById("encodedM").value);
    return modPower(message, d, n);
  }
}


function decToBinary(dec)
{
  var answer = "";
  while (dec > 0)
  {
    answer = dec % 2 + answer;
    dec = parseInt(dec / 2);
  }
  return answer;
}

function pad(str, padding)
{
  while (str.length < padding)
  {
    str = "0" + str;
  }
  return str;
}

function engToBinary(english)
{
  var answer = "";
  var a = "a".charCodeAt(0);
  for (var i = 0; i < english.length; i++)
  {
    answer += pad(decToBinary(english.charCodeAt(i) - a), 5);
  }
  return answer;
}

function binaryToDec(binary)
{
  var answer = 0;
  for (var i = 0; i < binary.length; i++)
  {
    if (binary[i] == "1")
    {
      answer += Math.pow(2, binary.length - i - 1);
    }
  }
  return answer;
}
