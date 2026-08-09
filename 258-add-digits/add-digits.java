class Solution {
    public int addDigits(int num) {
        int k=0;
        int m =0;
        int sum=0;
        for (;num>9;){
            k=num%10;
            m=num/10;
            num=k+m;
        }
        return num;  
    }
}