#include<iostream.h>
#include<conio.h>
void main()
{clrscr();
int a[20],b[20],c[30],m,n;
int k1=0,k2=0,k3=0;
cout<<"Enter no of elements in array1 & array2:";
cin>>m>>n;
cout<<"Enter sorted array1 values:";
for(int i=0;i<m;i++)
cin>>a[i];
cout<<"Enter sorted array2 values:";
for(i=0;i<n;i++)
cin>>b[i];
 while(k1<m&&k2<n)
  {if(a[k1]<b[k2])
   {c[k3]=a[k1];
   k3++;k1++;
   }
   else
   {c[k3]=b[k2];
   k3++;k2++;
   } }
 while(k1<m)
 {c[k3]=a[k1];
  k3++;k1++;
  }
 while(k2<n)
 {c[k3]=b[k2];
  k3++;k2++;
  }
 cout<<"Merge sorted array is: ";
 for(i=0;i<m+n;i++)
 cout<<c[i]<<" ";
}


