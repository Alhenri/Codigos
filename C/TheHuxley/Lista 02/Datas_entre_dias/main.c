#include <stdio.h>

int main(){
    int d1, m1, a1, d2, m2, a2, diasTotais=0; 
    int limMes, flag=1;
    int df, mf, af;
    
    scanf("%d/%d/%d", &d1, &m1, &a1);
    scanf("%d/%d/%d", &d2, &m2, &a2);


    limMes = (a1==a2)?m2:12; // variavel que vai decidir ate onde contar

    // Contando os dias
    for(int j = m1; j <= limMes; j++)//calcula os meses e os dias que passaram do primeiro ano
    {   
        if(((j%2==1)&&(j<8))||((j%2==0)&&(j>=8)))//meses com 31 dias
        {   
            if(flag){ // executa somente no primeiro mês
                diasTotais += (31-d1);
                flag=0;
            }else{
                diasTotais += 31;
            }
            
        }else
        if(j==2)// mes com 28 ou 29 dias (fevereiro)
        {
            if(((a1%4==0)&&(a1%100!=0))||(a1%400==0))// se for de um ano bissexto
            {
                if(flag){ // executa somente no primeiro mês
                    diasTotais += (29-d1);
                    flag=0;
                }else{
                    diasTotais += 29;
                }
            }
            else
            {
                if(flag){ // executa somente no primeiro mês
                    diasTotais += (28-d1);
                    flag=0;
                }else{
                    diasTotais += 28;
                }
            }
        }
        else
        {
            if(flag){ // executa somente no primeiro mês
                diasTotais += (30-d1);
                flag=0;
            }else{
                diasTotais += 30;
            }
        }
    }

    //printf("dias ate o fim do ano: %d\n", diasTotais);
    for (int i = a1+1; i < a2; i++)//conta os dias entre anos inteiros
    {    
        diasTotais += 365;
        if(((i%4==0)&&(i%100!=0))||(i%400==0)) //anos bissextos
        {
            diasTotais += 1;
        }
    }

    //printf("dias ate o ano presente: %d\n", diasTotais);

    for(int l = 1; l <= m2; l++)//calcula os meses e os dias que passaram do ultimo ano
    {
        if(((l%2==1)&&(l<8))||((l%2==0)&&(l>=8)))//meses com 31 dias
        {   
            if(l==m2){ // quando chegar no ultimo
                diasTotais += d2;
            }else{
                diasTotais += 31;
            }
            
        }else
        if(l==2)// mes com 28 ou 29 dias (fevereiro)
        {
            if(((a2%4==0)&&(a2%100!=0))||(a2%400==0))// se for de um ano bissexto
            {   
                if(l==m2){ // executa somente no primeiro mês
                    diasTotais += d2;
                }else{
                    diasTotais += 29;
                }
            }
            else
            {
                if(l==m2){ // executa somente no primeiro mês
                    diasTotais += d2;
                }else{
                    diasTotais += 28;
                }
            }
        }
        else
        {
            if(l==m2){ // executa somente no primeiro mês
                diasTotais += d2;
            }else{
                diasTotais += 30;
            }
        }
    }
    
    //printf("dias do ultimo ano: %d\n", diasTotais);
    // Incrementando as datas
    int diasData, flag2=0, anoFinal;
    
    diasData = diasTotais/2; //dias que serão acrescidos na data final

    // preciso saber se vai sobrar um dia pela metade
    diasData++;
    if((diasTotais%2)==1){
        flag2=1;
    }
    
    
    // Iniciando a data
    df = d1;
    mf = m1;
    af = a1;
    
    int debug=diasData;

    flag=1;
    while (flag&&diasData>0) // descontar os dias ate completar um mes
    {
        if(((mf%2==1)&&(mf<8))||((mf%2==0)&&(mf>=8)))//meses com 31 dias
        {   
            if(df<31){
                df+=1;
                diasData-=1;
            }else
            {   
                flag=0;
            }
            
        }else
        if(mf==2)// mes com 28 ou 29 dias (fevereiro)
        {
            if((a1%4==0)&&((a1%400==0)||(a1%100!=0)))// se for de um ano bissexto
            {   

                if(df<29){
                    df+=1;
                    diasData-=1;
                }else
                {
                    flag=0;
                }
            }
            else
            {
                if(df<28){
                    df+=1;
                    diasData-=1;
                }else
                {
                    flag=0;
                }
            }
        }
        else
        {
            if(df<30){
                df+=1;
                diasData-=1;
            }else
            {
                flag=0;

            }
        }
    }
    if(flag==0){// se ele completou um mes
        if(mf==12){
            mf=1;
            af+=1;

        }else{
            mf+=1;
            diasData--;
        }
        df=1;
    }
    //printf("dias pra completar um mes: %d\n", debug-diasData);
    //printf("data an: %d/%d/%d\n", df, mf, af);
    debug= diasData;
    flag=1;
    while (flag&&diasData>0) // descontar os meses
    {
        
        if(((mf%2==1)&&(mf<8))||((mf%2==0)&&(mf>=8)))//meses com 31 dias
        {   
            if(diasData >=31){
                if(!(mf==12)){
                    diasData-=31;
                    mf+=1;
                }else
                {
                    diasData-=31;
                    df=1;
                    mf=1;
                    af+=1;
                    flag=0;
                }
            }else
            {
                flag=0;
            }

        }else
        if(mf==2)// mes com 28 ou 29 dias (fevereiro)
        {
            if((a1%4==0)&&((a1%400==0)||(a1%100!=0)))// se for de um ano bissexto
            {
                if(diasData >=29){
                    diasData-=29;
                    mf+=1;
                }else
                {
                    flag=0;
                }    
            }
            else
            {
                if(diasData >=28){
                    diasData-=28;
                    mf+=1;
                }else
                {
                    flag=0;
                }
            }
        }
        else
        {
            if(diasData >=30){
                diasData-=30;
                mf+=1;
            }else
            {
                flag=0;
            }
        }
    }

    //printf("dias pra completar o ano: %d\n", debug-diasData);
    

    flag=1;
    while (flag&&diasData>0) // descontar os anos
    {
        if((af%4==0)&&((af%400==0)||(af%100!=0))) //anos bissextos
        {
            if(diasData >= 366)
            {
                diasData -= 366;//desconta o valor do ano
                af+=1; // aumenta um ano
            }
            else // se ele ta num ano bissexto mas nao ta completo ele sai
            {
                flag=0;
            }
        }
        else // Não é bissexto
        {
            if(diasData >= 365)
            {
                diasData -= 365;//desconta o valor do ano
                af+=1; // aumenta um ano
            }
            else // se ele não ta completo ele sai
            {
                flag=0;
            }
        }  
    }

    //printf("antes: %02d/%02d/%d\n", df, mf, af);
    //printf("dias restantes: %d\n", diasData);
    flag=1;
    while(flag&&diasData>0) // incrementa os dias
    {
        if(((mf%2==1)&&(mf<8))||((mf%2==0)&&(mf>=8)))//meses com 31 dias
        {   
            if(diasData>=31) // se eu ainda tiver mes dentro
            {     
                mf+=1;
                diasData-=31;   
            }else // se eu não tiver mais mes dentro
            {
                df=diasData;
                flag=0;
            }
            
        }else
        if(mf==2)// mes com 28 ou 29 dias (fevereiro)
        {
            if((af%4==0)&&((af%400==0)||(af%100!=0)))// se for de um ano bissexto
            {
                if(diasData>=29) // se eu ainda tiver mes dentro
                {
                    mf+=1;
                    diasData-=29;
            
                }else // se eu não tiver mais mes dentro
                {
                    df=diasData;
                    flag=0;
                }
            }
            else
            {
                if(diasData>=28) // se eu ainda tiver mes dentro
                {
                    mf+=1;
                    diasData-=28;
            
                }else // se eu não tiver mais mes dentro
                {
                    df=diasData;
                    flag=0;
                }
            }
        }
        else
        {
            if(diasData>=30) // se eu ainda tiver mes dentro
            {
                mf+=1;
                diasData-=30;
            
            }else // se eu não tiver mais mes dentro
            {
                df=diasData;
                flag=0;
            }
        }
    }

    printf("%02d/%02d/%d ", df, mf, af);
    if(flag2){
        printf("12:00");
        }
    else{
        printf("00:00");
    }
}