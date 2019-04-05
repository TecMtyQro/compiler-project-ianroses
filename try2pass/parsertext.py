from parser import *

testa = '''
void main(){
    // Este es un comentario
}
'''
testb = '''
void main(){
    /*
        Esto es un comentario void main(){

        }
    */
}
'''

# Test it out
test0 = '''
import 'dart:io';
import 'netflix:io';
void main(){
}
'''

test1 = '''
void main(){
  const int a = 16.33;
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
test13 = '''
//error
'''

# Check tests
try:
    print("\nTest A:")
    t = yacc.parse(testa)
    print(t.print_node())
except:
  print("Error on grammar")

try:
    print("\nTest B:")
    t = yacc.parse(testb)
    print(t.print_node())
except:
    print("Error on grammar")
#Ok
try:
    print("\nTest 0:")
    t = yacc.parse(test0)
    print(t.print_node())
except:
  print("Error on grammar")

#Dont Know
try:
    print("\nTest 1:")
    t = yacc.parse(test1)
    print(t.print_node())
except:
  print("Error on grammar")

#Error "hola" not valid
try:
    print("\nTest 2:")
    t = yacc.parse(test2)
    print(t.print_node())
except:
  print("Error on grammar")

#Valid
try:
    print("\nTest 3:")
    t = yacc.parse(test3)
    print(t.print_node())
except:
  print("Error on grammar")

#Valid
try:
    print("\nTest 4:")
    t = yacc.parse(test4)
    print(t.print_node())
except:
  print("Error on grammar")

#Error
try:
    print("\nTest 5:")
    t = yacc.parse(test5)
    print(t.print_node())
except:
  print("Error on grammar")

#Valid
try:
    print("\nTest 6:")
    t = yacc.parse(test6)
    print(t.print_node())
except:
  print("Error on grammar")

#Valid
try:
    print("\nTest 7:")
    t = yacc.parse(test7)
    print(t.print_node())
except:
  print("Error on grammar")

#Valid
try:
    print("\nTest 8:")
    t = yacc.parse(test8)
    print(t.print_node())
except:
  print("Error on grammar")

#Valid
try:
    print("\nTest 9:")
    t = yacc.parse(test9)
    print(t.print_node())
except:
  print("Error on grammar")

#Ok
try:
    print("\nTest 10:")
    t = yacc.parse(test10)
    print(t.print_node())
except:
  print("Error on grammar")

#Wrong loop must fail
try:
    print("\nTest 11:")
    t = yacc.parse(test11)
    print(t.print_node())
except:
  print("Error on grammar")

#Missing ; must fail
try:
    print("\nTest 12:")
    t = yacc.parse(test12)
    print(t.print_node())
except:
  print("Error on grammar")

#This must fail
try:
    print("\nTest 13:")
    t = yacc.parse(test13)
    print(t.print_node())
except:
  print("Error on grammar")
