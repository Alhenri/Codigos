#include <stdio.h>
#include <math.h>


int main(){
    int n;
    double ite1=0, ite2=0, ite3=3;
    scanf("%d", &n);
    for (int x = 0; x < n; x++)
    {
        ite1 += (pow(-1, x)/((2*x)+1));
        
        ite2 += (2.0/(((4*x)+1)*((4*x)+3)));
        
        if(x < (n-1)){
            if(x%2==0){
                ite3+=(4.0/(((2*x)+2)*((2*x)+3)*((2*x)+4)));
            }else{
                ite3-=(4.0/(((2*x)+2)*((2*x)+3)*((2*x)+4)));
            }
        }
    }
    ite1 = 4*ite1;
    ite2 = 4*ite2;
    
    printf("%.6f - %.6f\n", ite1, ite1/M_PI);
    printf("%.6f - %.6f\n", ite2, ite2/M_PI);
    printf("%.6f - %.6f\n", ite3, ite3/M_PI);
    return 0;
}