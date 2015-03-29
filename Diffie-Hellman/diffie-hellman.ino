void setup() {}

void loop() {
  Serial.begin(9600);
  long prime = getPrime(1000000000, 9999999999);
  Serial.println(prime);
  delay(1000);
}

int isPrime(long num) {
  int upper = sqrt(num);
  for (long cnum = 2; cnum <= upper; cnum++) {
    long mod = num % cnum;
    if (mod == 0) { 
      return 0;
    }
  }
  return 1;
}

long getPrime(long min, long max)  {
  while(true){
    long prime = random(min, max);
    if(isPrime(prime)) {
      return prime;
    }
  }
}
