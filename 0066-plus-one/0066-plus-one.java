class Solution {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length-1;i>=0;i--){
            int x=digits[i];
            x++;
            if(x<10){
                digits[i]=x;
                return digits;
            }
            digits[i]=0;
           

        }
         digits=new int[digits.length+1];
         if(digits[1]==0){
             digits[0]=1;
             
         }
          
         return digits; 
        
    }
}