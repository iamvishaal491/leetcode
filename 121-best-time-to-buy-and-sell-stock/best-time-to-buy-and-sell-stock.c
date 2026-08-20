int maxProfit(int* a, int s) {
    int min=0;
    int pr=0;
    for(int i=1;i<s;i++){
        if(a[i]-a[min]>pr)
        pr=a[i]-a[min];
        if(a[i]<a[min])
        min=i;
    }
    return pr;
}