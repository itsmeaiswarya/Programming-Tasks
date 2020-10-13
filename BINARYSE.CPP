#include<iostream.h>
#include<conio.h>
void main()
{clrscr();
 int a[20],n,data;
 cout<<"Enter no of elements:";
 cin>>n;
 cout<<"Enter a sorted array:";
  for(int i=0;i<n;i++)
   cin>>a[i];
   cout<<"Enter data to find in array:";
   cin>>data;
    int f=0;
    int l=n-1;
    int mid=(f+l)/2;
   while(f<=l&&a[mid]!=data)
   { if(a[mid]<data)
     f=mid+1;
     else
     l=mid-1;
     mid=(f+l)/2;
    }
   if(a[mid]==data)
   cout<<"Found at "<<mid;
   else
   cout<<"Not found.";
}
