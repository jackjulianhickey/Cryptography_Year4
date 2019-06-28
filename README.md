# Cryptography_Year4
## Assignment 1: 
The Many-time pad (re-using a One Time Padon multiple ciphertexts):The purpose here is to see what goes wrong when a simple XOR cipher key is usedmore than once.This key (henceforth referred to as the OTP) was random, and as long as the longest plaintext, but it was re-used to encrypt multiple plaintexts into their corresponding ciphertexts.

## Assignment 2: 
Implement  a Python program  which  executes  the  CFB  mode  of  operation,  for  the following block cipher: The  block  cipher  performs encryption first by  XORing  a  4  byte plaintext input block with the last 4 bytes of your student id. E.g. Student id “R1020341” -> last 4 bytes = “0341” = 0x30333431. The result is then rotated left by 3. E.g. bytes [1,2,3,4] ->[4,1,2,3]
