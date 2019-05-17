from semantic import *
test1 = '''
void main(){
  int a = 0;
  a +=1;
}
'''
test2 = '''
void main(){
  const int "hola" a;
  a int = 5;
}
'''
test3 = '''
import 'dart:io';

void main(){
  print("Enter your name : ");
  String name = stdin.readLineSync();
  int b;
  double a = 1 - 5 / 2;
  b = 0;
  b += 1;
  print(b);
  print(a);
  print(name);
}
'''
test4 = '''
import 'dart:io';

void main() {
    print("What's your name?");
    String name = stdin.readLineSync();
    print("Your Name is:");
    print(name);
    int year = 1997;
    if (year >= 2001) {
        print('21st century');
    } else if (year >= 1901) {
        print('20th century');
    }
    for (int month = 1; month <= 12; month++) {
        print(month);
        if(month < 5){
            print("hola");
        }else{
            print("no se puede");
        }
    }

    while (year < 2016) {
        year += 1;
    }
}
'''
test5 = '''
void main(){
  a String = 4;
  int b = 4 + "Hola";
}
'''
test6 = '''
void main(){
  for (int i = 1; i <= 12; i++) {
    for (int j = 1; j <= 12; j++) {
      if(j%3 == 0){
        if(i%6 == 0){
          print(j);
          print(i);
        }else{
          print("Nel");
        }
      }
    }
  }
}
'''
test7 = '''
void main () {
  // Comment on one line
}
'''
test8 = '''
void main() {
  /*
  Comment main(){
  dsdsads
  }
  */
}
'''
test9 = '''
void main(){
  String s = "hola";
  print("Hola Mundo");
}
'''
test10 = '''
void main(){
  int a = 0;
}
'''
test11 = '''
void main(){
  (true) while{
    break;
  }
}
'''
test12 = '''
import 'stdio:lib'
void main(){
}
'''

# Check tests
print("\nTest 1:")
try:
    yacc.parse(test1)
    try:
        salida = checkSemantic(test1)
        e = open("output/test1.py", "w+")
        e.write(salida)
        e.close()
        print("Compile complete")
    except:
        pass
except:
    pass

# print("\nTest 2:")
# try:
#     yacc.parse(test2)
#     try:
#         salida = checkSemantic(test2)
#         e = open("output/test2.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
# print("\nTest 3:")
# try:
#     yacc.parse(test3)
#     try:
#         salida = checkSemantic(test3)
#         e = open("output/test3.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
# print("\nTest 4:")
# try:
#     yacc.parse(test4)
#     try:
#         salida = checkSemantic(test4)
#         e = open("output/test4.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
# print("\nTest 5:")
# try:
#     yacc.parse(test5)
#     try:
#         salida = checkSemantic(test5)
#         e = open("output/test5.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
# print("\nTest 6:")
# try:
#     yacc.parse(test6)
#     try:
#         salida = checkSemantic(test6)
#         e = open("output/test6.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
#
# print("\nTest 7:")
# try:
#     yacc.parse(test7)
#     try:
#         salida = checkSemantic(test7)
#         e = open("output/test7.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
#
# print("\nTest 8:")
# try:
#     yacc.parse(test8)
#     try:
#         salida = checkSemantic(test8)
#         e = open("output/test8.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
#
# print("\nTest 9:")
# try:
#     yacc.parse(test9)
#     try:
#         salida = checkSemantic(test9)
#         e = open("output/test9.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
#
# print("\nTest 10:")
# try:
#     yacc.parse(test10)
#     try:
#         salida = checkSemantic(test10)
#         e = open("output/test10.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
#
# print("\nTest 11:")
# try:
#     yacc.parse(test11)
#     try:
#         salida = checkSemantic(test11)
#         e = open("output/test11.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
#
#
#
# print("\nTest 12:")
# try:
#     yacc.parse(test12)
#     try:
#         salida = checkSemantic(test12)
#         e = open("output/test12.py", "w+")
#         e.write(salida)
#         e.close()
#         print("Compile complete")
#     except:
#         pass
# except:
#     pass
