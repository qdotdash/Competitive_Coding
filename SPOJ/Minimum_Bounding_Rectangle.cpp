/*
The lowest x and y and the highest x and y in the whole points, circles and lines

Output :

3
1
p 3 3
3 3 3 3

2
c 10 10 20
c 20 20 10
-10 -10 30 30

1
l 0 0 100 20
0 0 100 20

*/

#include<iostream>

using namespace std;

int main(){
    int testcases, number_of_objects, x, y, r;
    char type_of_object;
    int x1, y1, x2, y2;
    int xmin=1001, ymin=1001, xmax=-1001, ymax=-1001;
    cin >> testcases;
    for(int i=0; i<testcases; i++){
        cin >> number_of_objects;
        xmin=1001, ymin=1001, xmax=-1001, ymax=-1001;
        for(int j=0; j<number_of_objects; j++){
            cin >> type_of_object;
            if(type_of_object=='p'){
                cin >> x >> y;
                if(x < xmin)
                    xmin = x;
                if(y < ymin)
                    ymin = y;
                if(x > xmax)
                    xmax = x;
                if(y > ymax)
                    ymax = y;
            }
            else if(type_of_object=='c'){
                cin >> x >> y >> r;
                int xmaxcirc, ymaxcirc, xmincirc, ymincirc;
                xmaxcirc = x + r;
                ymaxcirc = y + r;
                xmincirc = x - r;
                ymincirc = y - r;
                if(xmincirc < xmin)
                    xmin = xmincirc;
                if(ymincirc < ymin)
                    ymin = ymincirc;
                if(xmaxcirc > xmax)
                    xmax = xmaxcirc;
                if(ymaxcirc > ymax)
                    ymax = ymaxcirc;   
            }
            else{
                cin >> x1 >> y1 >> x2 >> y2;
                int xminline, xmaxline, yminline, ymaxline;
                xminline = x1;
                xmaxline = x2;
                yminline = y1;
                ymaxline = y2;
                if(x1>x2){
                    xminline = x2;
                    xmaxline = x1;
                }
                if(y1>y2){
                    yminline = y2;
                    ymaxline = y1;
                }
                if(xminline < xmin)
                    xmin = xminline;
                if(yminline < ymin)
                    ymin = yminline;
                if(xmaxline > xmax)
                    xmax = xmaxline;
                if(ymaxline > ymax)
                    ymax = ymaxline; 
                
            }
            
        }
        cout << xmin << " " << ymin << " " << xmax << " " << ymax;    
        if(i!=testcases-1){
            cout << "\n";  
        }  
    }
    return 0;
}