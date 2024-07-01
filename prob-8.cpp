long long greatest(string num)
{
    if (num.length() < 13)
        return 0;

    long long product = 1;
    unsigned int i;
    for (i=0; i<13; ++i) {
        product *= (num[i]-'0');
    }
    long long greatest_product = product;
   
    for (i=0; i+13<num.length(); ++i) {
        product = product/(num[i]-'0')*(num[i+13]-'0');
        if (greatest_product < product)
            greatest_product = product;
    }
    /* we return the greatest product below*/
    return greatest_product;
}
