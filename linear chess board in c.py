#include<stdio.h>
int main()
{
    int t,h,p;
    scanf("%d",&t);
    while(t){
        scanf("%d%d",&h,&p);
        while(h>0 && p>0)
        {
            h=h-p;
            p=p/2;
        }
        if(h<=0)
        printf("1\n");
        else if(p<=0)
        printf("0\n");
        
        
        t--;
    }
    return 0;
}
