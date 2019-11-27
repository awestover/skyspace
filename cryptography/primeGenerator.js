// kinda weird algorithm... not great... dont care...
function isPrime(n)
{
  if (n < 2)
  {
    alert("error in isPrime");
    return false;
  }
  if (n == 2 || n == 3)
  {
    return true;
  }
  if (n % 2 == 0 || n % 3 == 0)
  {
    return false;
  }
  var i = 5;
  while (i*i <= n)
  {
    if (n % i == 0)
    {
      return false;
    }
    i += 2
  }
  return true;
}

function biggerPrime(startPoint)
{
  startPoint = startPoint + startPoint % 2 + 1 // makes the number odd
  while (!isPrime(startPoint))
  {
    startPoint += 2;
  }
  return startPoint;
}
