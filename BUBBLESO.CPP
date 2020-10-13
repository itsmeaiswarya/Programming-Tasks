#include<iostream.h>
#include<conio.h>
void main()
{clrscr();
 int a[30],n,t;
 cout<<"Enter no of elements in an array:";
 cin>>n;
 cout<<"Enter an array:";
  for(int i=0;i<n;i++)
  cin>>a[i];
   for(i=0;i<n-1;i++)
    {for(int j=0;j<n-1;j++)
     if(a[j]>a[j+1])
      {t=a[j];
       a[j]=a[j+1];
       a[j+1]=t; 
      }
    }
 cout<<"Sorted Array is:";
 for(i=0;i<n;i++)
  cout<<a[i]<<" ";
}
