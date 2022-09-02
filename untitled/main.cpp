#include <iostream>
#include <cmath>

//int main(){
    //int num = 2;
    //const int constant_num = 11;
    // ++ post and ++ as prefix
    //variable  alongside ++ is going to be incremented as always
//    std::cout << "ok";
//    return 0;



//}
//int main() {
//
//
//    double x = 10, y = 5;
//    std::cout << (x +10) / (3*y);
//
//    return 0;
//}




//using namespace std;
//int main()
//
//{  double sales = 95000.25;
//    double State_Tax = 4;
//    int County_Tax = 2;
//    double Tax_Money =   sales * ((State_Tax + County_Tax)*0.01)   ;
//    cout << "Your sales this year is $ " << sales<< endl
//    << "Since State taxes are 4 percent"<< " County Taxes are 2 percent" <<endl
//    << "Your total taxes are $ "<< Tax_Money;

//}




//Reading input form the user:

//using namespace std;
//int main(){
//    cout <<" Enter 2 values you need to multiply with:  ";
//    double x;
//    double y;
//    cin >> x>> y;
//
//    cout << x * y;
//
//
//
//
//    return 0;
//}





//exercise: Temperature convertor

//using  namespace std;
//
//int main (){
//
//    cout << "Enter the temperature in fahrenheit to convert to celsius:   ";
//    double  tem_in_fahrenheit;
//    cin >> tem_in_fahrenheit;
//    cout << tem_in_fahrenheit<< " fahrenheit is ";
//    cout << (tem_in_fahrenheit-32)/ 1.8000<< " celsius"<<endl;
//    cout  << "65 to 80 fahrenheit is my paradise!!";
//    return 0;
//}


// cmath


//using namespace std;
//int main() {
//    double radius;
//
//    cout<<"Enter the radius to calculate the area of a circle:  ";
//    cin >> radius;
//    double area = 3.14* (pow( radius,2));
//    cout << "The area of the circle is "<< area;
//
//
//
//
//    return 0;
//}









//using namespace std;
//int main (){
//
//    double price = 99.99;
//    float interestrate = 3.67f;
//    long filesize = 90000l;
//    char letter = 'a';
//    bool isvalid = false;
//
//    int number = 1.2;
//    cout << number;
//
//    return 0;
//}







//number system
//binary and hex


//using namespace std;
//int main (){
//
//    //binary:
//    int number1 = 0b11111111;
//    int num2 = 0xff;
//            cout << number1 << endl<<num2;
//
//    return 0;
//}\









//narrowing and
// generating random numbers
//#include <cstdlib>
//#include <ctime>
//using namespace std;
//int main(){
//
////    int num =1'000'000;
////    short another = num;// big num to short will not work
////    //but short another = 100 which is 2 only bytes faster than declaring int another = 100
////    cout << another;
//
//
//    srand(  time(nullptr));// any seed
//    int random = (rand() % (5 - 3 +1) )+ 3; // (rand() % (max_limit - min_limit + 1)) + min_limit
//    cout<< random;
//// by changing our seed all the time with the time elapsed seconds
//    // since Jan 1 1970
//    return 0;
//}






//#include <iomanip>
//using namespace std;
//
//int main(){
////    cout << right<< setw(100)<< "good for you" << setw(4)<< "yes"; // 100 space to allocate the word
////           // can be
////     cout << fixed << setprecision(2)<<2000.566; // control desimal points
////
//      cout << left<< setw(16)<< "Course"<<setw(10) << "Students"<< endl<<left<< setw(16)
//      << "C++"<< setw(10) << "100"<< endl << left<< setw(16)<< "JavaScript"<< setw(10)<< "50";

//     return 0;//}










// sizeof()







// boolean
//#include <iomanip>
//using namespace std;
// int main(){
//     bool is_good = 0; //could be 1 and 0
//     cout <<   boolalpha <<is_good;
//
//
//
//
// }









// strings
#include <iomanip>
#include <cstring>
//using namespace std;
//int main(){
//
//    cout << "plz Enter your Street,city,State and ZipCode: "<<endl<<"Street: ";
//    string Street;
//    getline(cin ,Street );
//
//    cout << "City: ";
//    string city;
//    getline(cin ,city);
//
//    cout << "State:";
//    string State;
//    getline(cin ,State);
//
//    cout<< "ZipCode: ";
//    string ZipCode;
//    getline(cin ,ZipCode);
//    cout << Street <<endl
//    << city <<","<<State<<","<<ZipCode;
//
//
//    return 0;
//}







//// arrays
//using namespace std;
//
//int main(){
//  int age;
//  cout << "what your age is dude";
//  cin >> age;
//  if (age > 3)
//      cout <<"You are good, You are an adult.";
//  else if (age<= 3)
//      cout << "too bad man";
//  else
//      cout << "what are you doing ";
//
//
//
//
//    return 0;
//}





//using namespace std;
//void max(int& prie) {
//     prie = 6;
//
//}
//int main(){
//    int price = 15;
//    max(price);
//    cout << price;
//
//
//
//    return 0;
//
//
//










//using namespace std;
//
//void bubble_sort(int arr[],int size){
//    bool not_sorted = true;
//    while (not_sorted){
//        not_sorted = false;
//        for (int i = 0; i <size -1 ;i++)
//            if(arr[i]>arr[i+1]){
//                int temp = arr[i];
//                arr[i]  = arr[i+1];
//                arr[i+1] = temp;
//                not_sorted = true;
//            }
//    }
//
//}
//
//int main(){
//    int arr[] = {2,22,2222,4,9,8,65,489,8,4};
//    bubble_sort(arr,size(arr));
//    for (int i : arr){
//        cout<< i<<endl;
//    }
//    return 0;
//}













//
//using namespace std;
//int main(){
//
//    int arr[3] = {10,20,30};
//    int* prt = &arr[size(arr)-1];
//    while (prt >= &arr[0]) {
//        cout << *prt << endl;
//        prt--;
//
//
//    }









//
//
//
//using namespace std;
//
//int main(){
//    string c = "eren yeager";
//    int index = c.find(" ");
//    cout<<"last_name: "<<c.substr(0,index)<<endl<<"first_name: "
//    << c.substr(index+1);
//
//
//}
//
//
//



using namespace std;
struct Costumer{
    int ID;
    string Name;
    string Email;
};

int main(){
    Costumer costumer{6,"jj,","ll"};
    cout << costumer.Name;









    return 0;
}

