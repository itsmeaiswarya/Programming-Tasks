#include<iostream.h>
#include<conio.h>
void main()
{clrscr();
 int a[30],n,t,sm,loc;
 cout<<"Enter no of elements:";
 cin>>n;
 cout<<"Enter each elements:";
 for(int i=0;i<n;i++)
 cin>>a[i];
 for(i=0;i<n-1;i++)
 { sm=a[i];
   loc=i;
   for(int j=i;j<n;j++)
    if(a[j]<sm)
    {sm=a[j];
     loc=j;
    }
     t=a[i];
     a[i]=a[loc];
     a[loc]=t;
 }
   cout<<"Sorted Array is: ";
   for(int k=0;k<n;k++)
    cout<<a[k]<<endl;

}
