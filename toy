#include <stdio.h>
#include <inttypes.h>
#include <string.h>

uint8_t function(uint8_t input)
    uint8_t tmp;
    uint8_t in = input;

    tmp= in + ((in<<2)^(in>>6));
    in = tmp + ((in<<4)^(in>>4));

    return in;

}

void toy_cipher(uint8_t *ct, uint8_t *key, uint8_t *pt)
{
    uint8_t l1,l2,l3,r1,r2,r3;

    l1= pt[0]^key[0];
    r1= pt[1]^key[1];

    //round1
    r2= function(r1)^l1;
    l2=r1;

    //round2
    l3=function(r2)^l2;
    r3=r2;

    ct[0]=l3;
    ct[1]=r3;

}

void main()
{

    uint8_t pt[2] = {0x9c, 0x63};
    uint8_t key[2] = {0x37, 0xae};
    uint8_t ct[2] = {0, };

    toy_cipher(ct, key, pt);
   
    printf("ciphertext : %02x %02x \n", ct[0], ct[1]); //result -> ct : e14b
}
