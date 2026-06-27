bool isPalindrome(int x) {
    if(x<0)
    return false;
    long long dup=x;
    long long r,sum=0;
    while(x>0)
    {
        r=x%10;
        sum=sum*10+r;
        x=x/10;
    }
    if(sum==dup) return true;
    else return false;
}