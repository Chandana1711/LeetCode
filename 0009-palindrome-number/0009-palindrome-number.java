class Solution {
    public boolean isPalindrome(int x) {
       int digit,rev=0;
       int temp=x; 
      while(x>0){
           digit=x%10;
           rev=rev*10+digit;
           x/=10;
      }
      if(rev==temp)
       return true;
     else
      return false;

    }
}